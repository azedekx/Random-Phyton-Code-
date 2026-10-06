import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from pathlib import Path
import subprocess
import platform

class PlaylistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Music Playlist Player")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        
        # Variables
        self.playlist = []
        self.current_index = -1
        self.is_playing = False
        self.is_paused = False
        self.current_process = None
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        """Membuat widget UI"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="🎵 My Playlist", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Playlist listbox with scrollbar
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.playlist_box = tk.Listbox(list_frame, height=12, width=70, 
                                      yscrollcommand=scrollbar.set,
                                      font=("Arial", 10))
        self.playlist_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.playlist_box.yview)
        self.playlist_box.bind('<<ListboxSelect>>', self.on_select)
        
        # Current playing info
        self.info_label = ttk.Label(main_frame, text="No song selected", 
                                   font=("Arial", 9, "italic"),
                                   foreground="gray")
        self.info_label.grid(row=2, column=0, columnspan=4, pady=5)
        
        # Control buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=4, pady=10)
        
        # Add button
        add_btn = ttk.Button(button_frame, text="➕ Tambah", command=self.add_song)
        add_btn.grid(row=0, column=0, padx=5)
        
        # Remove button
        remove_btn = ttk.Button(button_frame, text="❌ Hapus", command=self.remove_song)
        remove_btn.grid(row=0, column=1, padx=5)
        
        # Clear button
        clear_btn = ttk.Button(button_frame, text="🗑️ Hapus Semua", command=self.clear_playlist)
        clear_btn.grid(row=0, column=2, padx=5)
        
        # Playback controls frame
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=4, pady=10)
        
        # Play button
        play_btn = ttk.Button(control_frame, text="▶️ Play", command=self.play_song)
        play_btn.grid(row=0, column=0, padx=5)
        
        # Pause button
        pause_btn = ttk.Button(control_frame, text="⏸️ Pause", command=self.pause_song)
        pause_btn.grid(row=0, column=1, padx=5)
        
        # Stop button
        stop_btn = ttk.Button(control_frame, text="⏹️ Stop", command=self.stop_song)
        stop_btn.grid(row=0, column=2, padx=5)
        
        # Previous button
        prev_btn = ttk.Button(control_frame, text="⏮️ Sebelumnya", command=self.prev_song)
        prev_btn.grid(row=0, column=3, padx=5)
        
        # Next button
        next_btn = ttk.Button(control_frame, text="⏭️ Selanjutnya", command=self.next_song)
        next_btn.grid(row=0, column=4, padx=5)
        
        # Volume control frame
        volume_frame = ttk.Frame(main_frame)
        volume_frame.grid(row=5, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(volume_frame, text="🔊 Volume:").pack(side=tk.LEFT, padx=5)
        
        self.volume_slider = ttk.Scale(volume_frame, from_=0, to=100, 
                                      orient=tk.HORIZONTAL, 
                                      command=self.set_volume)
        self.volume_slider.set(70)
        self.volume_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.volume_label = ttk.Label(volume_frame, text="70%", width=4)
        self.volume_label.pack(side=tk.LEFT)
        
    def add_song(self):
        """Menambah lagu ke playlist"""
        file_path = filedialog.askopenfilename(
            title="Pilih file lagu",
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac"), 
                      ("MP3 files", "*.mp3"),
                      ("All files", "*.*")]
        )
        
        if file_path:
            song_name = os.path.basename(file_path)
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, song_name)
            messagebox.showinfo("Sukses", f"Lagu '{song_name}' ditambahkan!")
    
    def remove_song(self):
        """Menghapus lagu yang dipilih"""
        try:
            index = self.playlist_box.curselection()[0]
            song_name = self.playlist_box.get(index)
            self.playlist.pop(index)
            self.playlist_box.delete(index)
            messagebox.showinfo("Sukses", f"Lagu '{song_name}' dihapus!")
        except IndexError:
            messagebox.showwarning("Peringatan", "Silakan pilih lagu untuk dihapus!")
    
    def clear_playlist(self):
        """Menghapus semua lagu"""
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus semua lagu?"):
            self.playlist.clear()
            self.playlist_box.delete(0, tk.END)
            self.stop_song()
            messagebox.showinfo("Sukses", "Semua lagu telah dihapus!")
    
    def play_song(self):
        """Memutar lagu yang dipilih"""
        try:
            if not self.is_playing:
                index = self.playlist_box.curselection()[0]
                song_path = self.playlist[index]
                
                # Stop previous playback if any
                if self.current_process:
                    try:
                        self.current_process.terminate()
                    except:
                        pass
                
                # Play using system media player
                if platform.system() == 'Windows':
                    self.current_process = subprocess.Popen(
                        ['start', '', song_path], 
                        shell=True
                    )
                elif platform.system() == 'Darwin':  # macOS
                    self.current_process = subprocess.Popen(
                        ['open', song_path]
                    )
                else:  # Linux
                    self.current_process = subprocess.Popen(
                        ['xdg-open', song_path]
                    )
                
                self.current_index = index
                self.is_playing = True
                self.is_paused = False
                self.playlist_box.selection_clear(0, tk.END)
                self.playlist_box.selection_set(index)
                self.playlist_box.see(index)
                self.update_info()
                messagebox.showinfo("Info", f"Memutar: {os.path.basename(song_path)}")
            else:
                messagebox.showinfo("Info", "Lagu sedang diputar!")
        except IndexError:
            messagebox.showwarning("Peringatan", "Silakan pilih lagu untuk diputar!")
        except Exception as e:
            messagebox.showerror("Error", f"Tidak dapat memutar lagu: {str(e)}")
    
    def pause_song(self):
        """Menjeda/Melanjutkan lagu"""
        if self.is_playing:
            self.is_paused = not self.is_paused
            status = "dijeda" if self.is_paused else "dilanjutkan"
            messagebox.showinfo("Info", f"Lagu {status}")
            self.update_info()
        else:
            messagebox.showinfo("Info", "Tidak ada lagu yang diputar!")
    
    def stop_song(self):
        """Menghentikan pemutaran lagu"""
        if self.is_playing:
            if self.current_process:
                try:
                    self.current_process.terminate()
                except:
                    pass
            self.is_playing = False
            self.is_paused = False
            self.current_index = -1
            self.current_process = None
            self.update_info()
    
    def next_song(self):
        """Memutar lagu berikutnya"""
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.playlist_box.selection_clear(0, tk.END)
            self.playlist_box.selection_set(self.current_index)
            self.playlist_box.see(self.current_index)
            self.play_song()
    
    def prev_song(self):
        """Memutar lagu sebelumnya"""
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.playlist_box.selection_clear(0, tk.END)
            self.playlist_box.selection_set(self.current_index)
            self.playlist_box.see(self.current_index)
            self.play_song()
    
    def on_select(self, event):
        """Update info ketika lagu dipilih"""
        self.update_info()
    
    def set_volume(self, value):
        """Mengatur volume (informasi saja, kontrol volume melalui sistem)"""
        self.volume_label.config(text=f"{int(float(value))}%")
    
    def update_info(self):
        """Update informasi lagu yang sedang dimainkan"""
        if self.is_playing:
            if self.current_index >= 0 and self.current_index < len(self.playlist):
                song_name = os.path.basename(self.playlist[self.current_index])
                status = "⏸️ Dijeda" if self.is_paused else "▶️ Sedang diputar"
                self.info_label.config(
                    text=f"{status}: {song_name}",
                    foreground="green"
                )
        else:
            try:
                index = self.playlist_box.curselection()[0]
                song_name = os.path.basename(self.playlist[index])
                self.info_label.config(text=f"📍 Dipilih: {song_name}", foreground="blue")
            except IndexError:
                self.info_label.config(text="No song selected", foreground="gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlaylistApp(root)
    root.mainloop()
