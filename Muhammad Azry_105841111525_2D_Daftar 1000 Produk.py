# -*- coding: utf-8 -*-
import random
import time
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
from typing import List
import numpy as np

class Product:
    """Kelas untuk mewakili produk dengan id, nama, dan harga"""
    def __init__(self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"
    
    def __str__(self):
        return f"ID: {self.id}, Nama: {self.name}, Harga: Rp{self.price:,.0f}"


def create_products(count: int = 1000) -> List[Product]:
    """
    Membuat daftar produk dengan data acak (tidak berurutan).
    """
    product_names = [
        'Sepatu', 'Baju', 'Gadget', 'Laptop', 'Smartphone', 'Headphone',
        'Tas', 'Jam Tangan', 'Kacamata', 'Sarung Tangan', 'Topi', 'Jaket',
        'Celana', 'Sandal', 'Dompet', 'Ikat Pinggang', 'Sarung', 'Boneka',
        'Mainan', 'Buku', 'Pensil', 'Spidol', 'Penghapus', 'Penggaris',
        'Kalkulator', 'Kompas', 'Gunting', 'Double Tape', 'Stapler', 'Kertas'
    ]
    
    products = []
    ids = list(range(1, count + 1))
    random.shuffle(ids)
    
    for i in range(count):
        product_id = ids[i]
        name = random.choice(product_names) + f" #{i+1}"
        price = random.uniform(50000, 5000000)
        products.append(Product(product_id, name, price))
    
    return products

def merge_sort(products: List[Product], key='id') -> List[Product]:
    """
    Mengurutkan daftar produk menggunakan Merge Sort.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(products) <= 1:
        return products
    
    def merge(left: List[Product], right: List[Product]) -> List[Product]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            left_val = getattr(left[i], key)
            right_val = getattr(right[j], key)
            
            if left_val <= right_val:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort_recursive(arr: List[Product]) -> List[Product]:
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        
        return merge(left, right)
    
    return merge_sort_recursive(products)

def binary_search(products: List[Product], target_id: int, key='id') -> tuple:
    """
    Mencari produk menggunakan Binary Search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(products) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_val = getattr(products[mid], key)
        
        if mid_val == target_id:
            return products[mid], iterations
        elif mid_val < target_id:
            left = mid + 1
        else:
            right = mid - 1
    
    return None, iterations

def sequential_search(products: List[Product], target_id: int, key='id') -> tuple:
    """
    Mencari produk menggunakan Sequential Search.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    iterations = 0
    
    for product in products:
        iterations += 1
        if getattr(product, key) == target_id:
            return product, iterations
    
    return None, iterations

def create_visualizations(products_original, products_sorted, search_targets, 
                         binary_results, sequential_results, merge_sort_time):
    """Membuat visualisasi untuk hasil pengurutan dan pencarian."""
    try:
        fig = plt.figure(figsize=(16, 12))
        fig.suptitle('Visualisasi Analisis Algoritme Sorting dan Searching', 
                     fontsize=16, fontweight='bold')
        
        # SUBPLOT 1: Perbandingan Data Asli vs Terurut
        ax1 = plt.subplot(2, 3, 1)
        original_ids = [p.id for p in products_original[:100]]
        sorted_ids = [p.id for p in products_sorted[:100]]
        x = range(100)
        
        ax1.plot(x, original_ids, 'ro-', label='Data Asli (Acak)', alpha=0.6, markersize=3)
        ax1.plot(x, sorted_ids, 'bs-', label='Data Terurut', alpha=0.6, markersize=3)
        ax1.set_xlabel('Indeks Produk')
        ax1.set_ylabel('ID Produk')
        ax1.set_title('Data Asli vs Terurut (100 Produk)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # SUBPLOT 2: Distribusi Harga
        ax2 = plt.subplot(2, 3, 2)
        prices = [p.price for p in products_sorted]
        ax2.hist(prices, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
        ax2.set_xlabel('Harga Produk (Rp)')
        ax2.set_ylabel('Jumlah Produk')
        ax2.set_title('Distribusi Harga 1000 Produk')
        ax2.grid(True, alpha=0.3, axis='y')
        
        # SUBPLOT 3: Perbandingan Waktu Pencarian
        ax3 = plt.subplot(2, 3, 3)
        target_labels = [f"ID {t}" for t in search_targets]
        binary_times = [r[3] * 1000000 for r in binary_results]  # microseconds
        sequential_times = [r[3] * 1000000 for r in sequential_results]
        
        x_pos = np.arange(len(target_labels))
        width = 0.35
        
        ax3.bar(x_pos - width/2, binary_times, width, label='Binary Search', 
                color='green', alpha=0.7)
        ax3.bar(x_pos + width/2, sequential_times, width, label='Sequential Search', 
                color='red', alpha=0.7)
        
        ax3.set_xlabel('Target Pencarian')
        ax3.set_ylabel('Waktu (µs)')
        ax3.set_title('Perbandingan Waktu Pencarian')
        ax3.set_xticks(x_pos)
        ax3.set_xticklabels(target_labels)
        ax3.legend()
        ax3.grid(True, alpha=0.3, axis='y')
        
        # SUBPLOT 4: Perbandingan Iterasi
        ax4 = plt.subplot(2, 3, 4)
        binary_iterations = [r[2] for r in binary_results]
        sequential_iterations = [r[2] for r in sequential_results]
        
        ax4.bar(x_pos - width/2, binary_iterations, width, label='Binary Search', 
                color='green', alpha=0.7)
        ax4.bar(x_pos + width/2, sequential_iterations, width, label='Sequential Search', 
                color='red', alpha=0.7)
        
        ax4.set_xlabel('Target Pencarian')
        ax4.set_ylabel('Jumlah Iterasi')
        ax4.set_title('Perbandingan Jumlah Iterasi')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(target_labels)
        ax4.legend()
        ax4.grid(True, alpha=0.3, axis='y')
        
        # SUBPLOT 5: Total Waktu
        ax5 = plt.subplot(2, 3, 5)
        total_binary = sum(binary_times)
        total_sequential = sum(sequential_times)
        
        methods = ['Binary\nSearch', 'Sequential\nSearch']
        times = [total_binary, total_sequential]
        colors = ['green', 'red']
        
        bars = ax5.bar(methods, times, color=colors, alpha=0.7, width=0.5)
        ax5.set_ylabel('Total Waktu (µs)')
        ax5.set_title('Total Waktu Eksekusi (4 Pencarian)')
        ax5.grid(True, alpha=0.3, axis='y')
        
        for bar, time_val in zip(bars, times):
            height = bar.get_height()
            ax5.text(bar.get_x() + bar.get_width()/2., height,
                    f'{time_val:.0f}µs', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        # SUBPLOT 6: Analisis Kompleksitas
        ax6 = plt.subplot(2, 3, 6)
        ax6.axis('off')
        
        complexity_text = f"""
ANALISIS KOMPLEKSITAS

Merge Sort:
  Time:  O(n log n)
  Space: O(n)
  Waktu: {merge_sort_time:.6f}s

Binary Search:
  Time:  O(log n)
  Space: O(1)
  Iter:  {np.mean(binary_iterations):.1f}

Sequential Search:
  Time:  O(n)
  Space: O(1)
  Iter:  {np.mean(sequential_iterations):.0f}

Speedup: {(total_sequential/total_binary if total_binary > 0 else 1):.1f}x
        """
        
        ax6.text(0.05, 0.95, complexity_text, transform=ax6.transAxes,
                fontsize=9, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        output_path = r'c:\Users\lenovo\.vscode\.vscode\MyProject\sorting_visualization.png'
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        print(f"[OK] Visualisasi disimpan: {output_path}")
        plt.close()
        return True
    except Exception as e:
        print(f"[!] Error visualisasi: {e}")
        return False


def create_complexity_chart():
    """Membuat grafik perbandingan kompleksitas."""
    try:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle('Perbandingan Kompleksitas Algoritme', fontsize=14, fontweight='bold')
        
        n_values = [10, 50, 100, 500, 1000, 5000, 10000]
        merge_sort_ops = [n * np.log2(n) for n in n_values]
        binary_search_ops = [np.log2(n) for n in n_values]
        sequential_search_ops = [n for n in n_values]
        
        # Linear Scale
        ax1.plot(n_values, merge_sort_ops, 'bo-', linewidth=2, markersize=8, 
                 label='Merge Sort O(n log n)')
        ax1.plot(n_values, binary_search_ops, 'go-', linewidth=2, markersize=8, 
                 label='Binary Search O(log n)')
        ax1.plot(n_values, sequential_search_ops, 'ro-', linewidth=2, markersize=8, 
                 label='Sequential Search O(n)')
        
        ax1.set_xlabel('Ukuran Dataset (n)')
        ax1.set_ylabel('Jumlah Operasi (relative)')
        ax1.set_title('Skala Linear')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Log Scale
        ax2.loglog(n_values, merge_sort_ops, 'bo-', linewidth=2, markersize=8, 
                   label='Merge Sort O(n log n)')
        ax2.loglog(n_values, binary_search_ops, 'go-', linewidth=2, markersize=8, 
                   label='Binary Search O(log n)')
        ax2.loglog(n_values, sequential_search_ops, 'ro-', linewidth=2, markersize=8, 
                   label='Sequential Search O(n)')
        
        ax2.set_xlabel('Ukuran Dataset (n)')
        ax2.set_ylabel('Jumlah Operasi (relative)')
        ax2.set_title('Skala Logaritmik (Log-Log)')
        ax2.legend()
        ax2.grid(True, alpha=0.3, which='both')
        
        plt.tight_layout()
        output_path = r'c:\Users\lenovo\.vscode\.vscode\MyProject\complexity_comparison.png'
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        print(f"[OK] Grafik kompleksitas disimpan: {output_path}")
        plt.close()
        return True
    except Exception as e:
        print(f"[!] Error grafik kompleksitas: {e}")
        return False

def main():
    print("=" * 80)
    print("PROGRAM PENGURUTAN DAN PENCARIAN PRODUK DENGAN VISUALISASI")
    print("=" * 80)
    print()
    
    # Step 1: Membuat 1000 produk
    print("[STEP 1] Membuat 1000 objek produk dengan data acak...")
    products_original = create_products(1000)
    print(f"Berhasil membuat {len(products_original)} produk")
    print(f"  Contoh 3 produk pertama:")
    for i in range(3):
        print(f"    - {products_original[i]}")
    print()
    
    # Step 2: Merge Sort
    print("[STEP 2] Mengurutkan dengan Merge Sort berdasarkan ID...")
    start_time = time.time()
    products_sorted = merge_sort(products_original.copy(), key='id')
    merge_sort_time = time.time() - start_time
    
    print(f"[OK] Pengurutan selesai dalam {merge_sort_time:.6f} detik")
    print(f"  5 produk pertama setelah diurutkan:")
    for i in range(5):
        print(f"    - {products_sorted[i]}")
    print()
    
    # Step 3: Binary Search
    print("[STEP 3] Pencarian dengan Binary Search...")
    search_targets = [42, 500, 999, 1]
    binary_results = []
    
    print(f" Target: {search_targets}")
    total_binary_time = 0
    
    for target_id in search_targets:
        start_time = time.time()
        product, iterations = binary_search(products_sorted, target_id, key='id')
        elapsed_time = time.time() - start_time
        binary_results.append((target_id, product, iterations, elapsed_time))
        total_binary_time += elapsed_time
        
        status = "[OK] Ditemukan" if product else "[X] Tidak ditemukan"
        print(f"    ID {target_id}: {status} | Iterasi: {iterations} | Waktu: {elapsed_time:.8f}s")
    
    print(f"  Total Binary Search: {total_binary_time:.8f}s")
    print()
    
    # Step 4: Sequential Search
    print("[STEP 4] Pencarian dengan Sequential Search...")
    print(f"  Target: {search_targets}")
    sequential_results = []
    total_sequential_time = 0
    
    for target_id in search_targets:
        start_time = time.time()
        product, iterations = sequential_search(products_original, target_id, key='id')
        elapsed_time = time.time() - start_time
        sequential_results.append((target_id, product, iterations, elapsed_time))
        total_sequential_time += elapsed_time
        
        status = "[OK] Ditemukan" if product else "[X] Tidak ditemukan"
        print(f"    ID {target_id}: {status} | Iterasi: {iterations} | Waktu: {elapsed_time:.8f}s")
    
    print(f"  Total Sequential Search: {total_sequential_time:.8f}s")
    print()
    
    # Step 5: Perbandingan
    print("[STEP 5] PERBANDINGAN HASIL")
    print("=" * 80)
    print(f"{'Target ID':<12} {'Binary Iter':<15} {'Binary Time':<18} {'Seq Iter':<15} {'Seq Time':<18}")
    print("-" * 78)
    
    for i, target_id in enumerate(search_targets):
        b_iter = binary_results[i][2]
        b_time = binary_results[i][3]
        s_iter = sequential_results[i][2]
        s_time = sequential_results[i][3]
        print(f"{target_id:<12} {b_iter:<15} {b_time:<18.8f} {s_iter:<15} {s_time:<18.8f}")
    
    print()
    print(f"Binary Search total:     {total_binary_time:.8f}s")
    print(f"Sequential Search total: {total_sequential_time:.8f}s")
    
    if total_binary_time > 0:
        improvement = (total_sequential_time - total_binary_time) / total_sequential_time * 100
        speedup = total_sequential_time / total_binary_time
        print(f"Peningkatan kecepatan:   {improvement:.2f}% | Speedup: {speedup:.1f}x")
    print()
    
    # Step 6: Analisis Kompleksitas
    print("[STEP 6] ANALISIS KOMPLEKSITAS WAKTU ASIMTOTIK (BIG O)")
    print("=" * 80)
    print()
    
    analysis = """
MERGE SORT (Pengurutan):
    |- Time Complexity:    O(n log n) - Best, Average, Worst case
    |- Space Complexity:   O(n) - Memerlukan array tambahan
    |- Waktu eksekusi:     {:.6f}s (untuk {} produk)
   - Karakteristik:      Stabil, Divide & Conquer

BINARY SEARCH (Pencarian - Array Terurut):
    |- Time Complexity:    O(log n) - Best, Average, Worst case
    |- Space Complexity:   O(1) - Hanya menggunakan pointer
    |- Rata-rata iterasi:  {:.1f} iterasi
   - Karakteristik:      Memerlukan data terurut, Sangat cepat

SEQUENTIAL SEARCH (Pencarian - Array Acak):
    |- Time Complexity:    O(n) - Worst case
    |- Space Complexity:   O(1) - Hanya menggunakan pointer
    |- Rata-rata iterasi:  {:.0f} iterasi
   - Karakteristik:      Bekerja pada data acak, Lebih lambat

PERBANDINGAN:
  • Binary Search {:.1f}x lebih cepat dari Sequential Search
  • Sorted data dengan Binary Search = Optimal untuk banyak pencarian
  • Trade-off: Waktu pengurutan vs efisiensi pencarian
    """.format(
        merge_sort_time, len(products_original),
        np.mean([r[2] for r in binary_results]),
        np.mean([r[2] for r in sequential_results]),
        (total_sequential_time / total_binary_time) if total_binary_time > 0 else 1
    )
    print(analysis)
    print()
    
    # Step 7: Visualisasi
    print("[STEP 7] MEMBUAT VISUALISASI...")
    print("=" * 80)
    print()
    
    print("Membuat grafik perbandingan dan distribusi data...")
    success1 = create_visualizations(products_original, products_sorted, search_targets,
                                     binary_results, sequential_results, merge_sort_time)
    
    print("Membuat grafik analisis kompleksitas...")
    success2 = create_complexity_chart()
    
    print()
    print("=" * 80)
    if success1 and success2:
        print("[OK] Program selesai! Semua visualisasi telah dibuat.")
    else:
        print("[OK] Program selesai! Beberapa visualisasi mungkin gagal.")
    print("=" * 80)


if __name__ == "__main__":
    main()
