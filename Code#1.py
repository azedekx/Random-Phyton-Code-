"""
Program Sistem Akademik Universitas
Simulasi pengelolaan data 100 mahasiswa dengan sorting dan binary search
"""

import random
from typing import List, Dict, Tuple, Optional


class SistemAkademik:
    """Kelas untuk mengelola sistem akademik universitas"""
    
    def __init__(self):
        self.mahasiswa: List[Dict[str, any]] = []
    
    # ============ INISIALISASI DATA ============
    def generate_data_mahasiswa(self, jumlah: int = 100) -> None:
        """
        Generate data dummy untuk mahasiswa
        
        Args:
            jumlah: Jumlah mahasiswa yang akan dibuat (default: 100)
        """
        nama_depan = [
            "Budi", "Siti", "Ahmad", "Dewi", "Rudi", "Rina", "Bambang", "Sari",
            "Hendra", "Linda", "Yudi", "Nita", "Dedi", "Eka", "Fajar", "Gita",
            "Hari", "Iis", "Joko", "Kusuma", "Lia", "Maman", "Nanda", "Oscar",
            "Priya", "Qonita", "Roni", "Sinta", "Tika", "Usman", "Viki", "Wina",
            "Xander", "Yani", "Zain", "Amir", "Bella", "Citra", "Dian", "Erwin"
        ]
        
        nama_belakang = [
            "Wijaya", "Kusuma", "Rahman", "Santoso", "Pratama", "Setiawan",
            "Handoko", "Suryanto", "Hermawan", "Prabowo", "Irawan", "Gunawan",
            "Haryanto", "Firmansyah", "Gunawan", "Hidayat", "Ikhsan", "Jatmiko",
            "Kusuma", "Kurniawan", "Luthfiman", "Maulana", "Nugroho", "Oktavian",
            "Pratama", "Qothrunnada", "Ramadhani", "Suryadi", "Tanjung", "Usman",
            "Verdianto", "Wibisono", "Ximenes", "Yunus", "Zainal", "Aziz",
            "Basuki", "Cahyo", "Darmawan", "Efendi"
        ]
        
        self.mahasiswa = []
        
        for i in range(jumlah):
            nim = f"20{random.randint(20, 24):02d}{random.randint(1000, 9999)}"
            nama = random.choice(nama_depan) + " " + random.choice(nama_belakang)
            nilai = round(random.uniform(50, 100), 2)
            
            self.mahasiswa.append({
                "NIM": nim,
                "Nama": nama,
                "Nilai Akhir": nilai
            })
    
    # ============ QUICK SORT ============
    def quick_sort_by_nilai(self, data: List[Dict] = None) -> List[Dict]:
        """
        Implementasi Quick Sort untuk mengurutkan mahasiswa berdasarkan Nilai Akhir
        
        Args:
            data: List mahasiswa yang akan diurutkan (default: self.mahasiswa)
            
        Returns:
            List mahasiswa yang sudah terurut
        """
        if data is None:
            data = self.mahasiswa
        
        if len(data) <= 1:
            return data
        
        # Pilih pivot (elemen tengah)
        pivot_index = len(data) // 2
        pivot = data[pivot_index]
        
        # Partisi
        less = []
        equal = []
        greater = []
        
        for item in data:
            if item["Nilai Akhir"] < pivot["Nilai Akhir"]:
                less.append(item)
            elif item["Nilai Akhir"] == pivot["Nilai Akhir"]:
                equal.append(item)
            else:
                greater.append(item)
        
        # Gabungkan hasil
        return self.quick_sort_by_nilai(less) + equal + self.quick_sort_by_nilai(greater)
    
    def quick_sort_by_nim(self, data: List[Dict] = None) -> List[Dict]:
        """
        Implementasi Quick Sort untuk mengurutkan mahasiswa berdasarkan NIM
        
        Args:
            data: List mahasiswa yang akan diurutkan
            
        Returns:
            List mahasiswa yang sudah terurut berdasarkan NIM
        """
        if data is None:
            data = self.mahasiswa
        
        if len(data) <= 1:
            return data
        
        pivot_index = len(data) // 2
        pivot = data[pivot_index]
        
        less = []
        equal = []
        greater = []
        
        for item in data:
            if item["NIM"] < pivot["NIM"]:
                less.append(item)
            elif item["NIM"] == pivot["NIM"]:
                equal.append(item)
            else:
                greater.append(item)
        
        return self.quick_sort_by_nim(less) + equal + self.quick_sort_by_nim(greater)
    
    # ============ BINARY SEARCH ============
    def binary_search_by_nim(self, sorted_data: List[Dict], target_nim: str) -> Optional[Dict]:
        """
        Implementasi Binary Search untuk mencari mahasiswa berdasarkan NIM
        
        Args:
            sorted_data: List mahasiswa yang sudah terurut berdasarkan NIM
            target_nim: NIM yang dicari
            
        Returns:
            Dictionary mahasiswa jika ditemukan, None jika tidak
        """
        left = 0
        right = len(sorted_data) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_nim = sorted_data[mid]["NIM"]
            
            if mid_nim == target_nim:
                return sorted_data[mid]
            elif mid_nim < target_nim:
                left = mid + 1
            else:
                right = mid - 1
        
        return None
    
    # ============ PENCARIAN BINER DENGAN INPUT USER ============
    def cari_mahasiswa(self) -> None:
        """
        Fungsi untuk mencari mahasiswa berdasarkan input NIM dari user
        Menggunakan binary search pada data yang sudah diurutkan berdasarkan NIM
        """
        print("\n" + "="*70)
        print("PENCARIAN MAHASISWA BERDASARKAN NIM (BINARY SEARCH)")
        print("="*70)
        
        # Buat salinan dan urutkan berdasarkan NIM
        mahasiswa_sorted_by_nim = self.quick_sort_by_nim(self.mahasiswa.copy())
        
        # Minta input NIM dari user
        target_nim = input("\nMasukkan NIM yang dicari: ").strip()
        
        # Lakukan binary search
        hasil = self.binary_search_by_nim(mahasiswa_sorted_by_nim, target_nim)
        
        # Tampilkan hasil
        if hasil:
            print("\n✓ Mahasiswa ditemukan!")
            print(f"  NIM        : {hasil['NIM']}")
            print(f"  Nama       : {hasil['Nama']}")
            print(f"  Nilai Akhir: {hasil['Nilai Akhir']}")
        else:
            print("\n✗ Nilai tidak ditemukan")
    
    # ============ ANALISIS NILAI ============
    def analisis_nilai(self) -> None:
        """
        Menampilkan analisis nilai mahasiswa:
        - Mahasiswa dengan nilai tertinggi
        - Mahasiswa dengan nilai terendah
        - Rata-rata nilai
        """
        print("\n" + "="*70)
        print("ANALISIS NILAI AKHIR")
        print("="*70)
        
        if not self.mahasiswa:
            print("Data mahasiswa kosong!")
            return
        
        # Cari nilai tertinggi
        mahasiswa_tertinggi = max(self.mahasiswa, key=lambda x: x["Nilai Akhir"])
        
        # Cari nilai terendah
        mahasiswa_terendah = min(self.mahasiswa, key=lambda x: x["Nilai Akhir"])
        
        # Hitung rata-rata
        total_nilai = sum(m["Nilai Akhir"] for m in self.mahasiswa)
        rata_rata = total_nilai / len(self.mahasiswa)
        
        # Tampilkan hasil
        print("\n1. NILAI TERTINGGI:")
        print(f"   NIM        : {mahasiswa_tertinggi['NIM']}")
        print(f"   Nama       : {mahasiswa_tertinggi['Nama']}")
        print(f"   Nilai Akhir: {mahasiswa_tertinggi['Nilai Akhir']}")
        
        print("\n2. NILAI TERENDAH:")
        print(f"   NIM        : {mahasiswa_terendah['NIM']}")
        print(f"   Nama       : {mahasiswa_terendah['Nama']}")
        print(f"   Nilai Akhir: {mahasiswa_terendah['Nilai Akhir']}")
        
        print(f"\n3. RATA-RATA NILAI: {rata_rata:.2f}")
    
    # ============ TAMPILKAN DATA ============
    def tampilkan_data(self, data: List[Dict] = None, judul: str = "") -> None:
        """
        Menampilkan data mahasiswa dalam format tabel
        
        Args:
            data: List mahasiswa yang akan ditampilkan
            judul: Judul untuk ditampilkan
        """
        if data is None:
            data = self.mahasiswa
        
        if not data:
            print("Data kosong!")
            return
        
        if judul:
            print("\n" + "="*70)
            print(judul)
            print("="*70)
        
        # Header
        print(f"\n{'NO.':<5} {'NIM':<15} {'NAMA':<30} {'NILAI AKHIR':<15}")
        print("-" * 70)
        
        # Data
        for i, m in enumerate(data, 1):
            print(f"{i:<5} {m['NIM']:<15} {m['Nama']:<30} {m['Nilai Akhir']:<15.2f}")
    
    # ============ MAIN PROGRAM ============
    def jalankan(self) -> None:
        """Menjalankan program sistem akademik"""
        print("\n" + "="*70)
        print("SISTEM AKADEMIK UNIVERSITAS")
        print("Simulasi Pengelolaan Data 100 Mahasiswa")
        print("="*70)
        
        # 1. Inisialisasi data
        print("\n[1] Menginisialisasi data 100 mahasiswa...")
        self.generate_data_mahasiswa(100)
        print("✓ Data mahasiswa berhasil dibuat")
        
        # 2. Tampilkan data awal (10 baris pertama)
        print("\n[2] Menampilkan 10 data mahasiswa pertama (sebelum sorting):")
        self.tampilkan_data(self.mahasiswa[:10])
        
        # 3. Sorting berdasarkan Nilai Akhir
        print("\n[3] Melakukan Sorting (Quick Sort) berdasarkan Nilai Akhir...")
        self.mahasiswa = self.quick_sort_by_nilai(self.mahasiswa)
        print("✓ Data mahasiswa berhasil diurutkan")
        
        # Tampilkan data setelah sorting
        print("\nData setelah sorting (10 data pertama dengan nilai terendah):")
        self.tampilkan_data(self.mahasiswa[:10])
        
        print("\n(10 data terakhir dengan nilai tertinggi):")
        self.tampilkan_data(self.mahasiswa[-10:])
        
        # 4. Binary Search
        print("\n[4] Pencarian Mahasiswa (Binary Search)")
        self.cari_mahasiswa()
        
        # 5. Analisis Nilai
        print("\n[5] Analisis Nilai Mahasiswa")
        self.analisis_nilai()
        
        # 6. Menu tambahan
        self.menu_tambahan()
    
    def menu_tambahan(self) -> None:
        """Menu untuk operasi tambahan"""
        while True:
            print("\n" + "="*70)
            print("MENU TAMBAHAN")
            print("="*70)
            print("1. Cari mahasiswa lagi (Binary Search)")
            print("2. Tampilkan analisis nilai")
            print("3. Tampilkan semua data mahasiswa")
            print("4. Keluar")
            print("-" * 70)
            
            pilihan = input("Pilih menu (1-4): ").strip()
            
            if pilihan == "1":
                self.cari_mahasiswa()
            elif pilihan == "2":
                self.analisis_nilai()
            elif pilihan == "3":
                self.tampilkan_data(judul="DATA SEMUA 100 MAHASISWA (TERURUT BERDASARKAN NILAI AKHIR)")
            elif pilihan == "4":
                print("\nTerima kasih telah menggunakan Sistem Akademik Universitas!")
                print("Program selesai.")
                break
            else:
                print("✗ Pilihan tidak valid. Silakan coba lagi.")


def main():
    """Fungsi utama untuk menjalankan program"""
    sistem = SistemAkademik()
    sistem.jalankan()


if __name__ == "__main__":
    main()
