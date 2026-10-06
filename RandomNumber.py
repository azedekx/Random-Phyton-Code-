import random

def generate_random_numbers(count=100, min_val=1, max_val=1000):
    """
    Menghasilkan daftar bilangan bulat acak.
    
    Args:
        count: Jumlah bilangan yang akan dibuat (default: 100)
        min_val: Nilai minimum (default: 1)
        max_val: Nilai maksimum (default: 1000)
    
    Returns:
        List berisi bilangan bulat acak
    """
    return [random.randint(min_val, max_val) for _ in range(count)]


def linear_search(numbers, target):
    """
    Melakukan pencarian linear dengan melacak jumlah perbandingan.
    
    Args:
        numbers: Daftar bilangan untuk dicari
        target: Nilai yang dicari
    
    Returns:
        Tuple (indeks bilangan, jumlah perbandingan)
        Mengembalikan (-1, jumlah perbandingan) jika tidak ditemukan
    """
    comparisons = 0
    
    for index, number in enumerate(numbers):
        comparisons += 1  # Track setiap perbandingan
        
        if number == target:
            return index, comparisons
    
    # Jika tidak ditemukan setelah memeriksa semua elemen
    return -1, comparisons

def calculate_statistics(numbers, target, index, comparisons):
    """
    Menghitung statistik pencarian.
    
    Args:
        numbers: Daftar bilangan
        target: Nilai yang dicari
        index: Indeks hasil pencarian (-1 jika tidak ditemukan)
        comparisons: Jumlah perbandingan yang dilakukan
    
    Returns:
        Dictionary berisi informasi statistik
    """
    total_elements = len(numbers)
    comparison_percentage = (comparisons / total_elements) * 100
    
    stats = {
        'ditemukan': index != -1,
        'indeks': index,
        'nilai': numbers[index] if index != -1 else None,
        'total_perbandingan': comparisons,
        'total_elemen': total_elements,
        'persentase_perbandingan': comparison_percentage,
        'efisiensi': f"{comparison_percentage:.2f}%"
    }
    
    return stats

def main():
    print("=" * 80)
    print("PROGRAM LINEAR SEARCH DENGAN TRACKING PERBANDINGAN")
    print("=" * 80)
    print()
    
    print("[STEP 1] Menghasilkan 100 bilangan bulat acak (1-1000)...")
    numbers = generate_random_numbers(100, 1, 1000)
    print(f"[OK] Berhasil menghasilkan {len(numbers)} bilangan acak")
    print()
    
    print("[STEP 2] Daftar 100 Bilangan Acak:")
    print("-" * 80)
    
    for i in range(0, len(numbers), 10):
        row = numbers[i:i+10]
        row_str = " ".join(f"{num:4d}" for num in row)
        print(f"[{i:3d}-{min(i+9, len(numbers)-1):3d}]: {row_str}")
    
    print()
    print("=" * 80)
    print()
    
    print("[STEP 3] Statistik Daftar:")
    print("-" * 80)
    print(f"Total Elemen:      {len(numbers)}")
    print(f"Nilai Minimum:     {min(numbers)}")
    print(f"Nilai Maksimum:    {max(numbers)}")
    print(f"Rata-rata:         {sum(numbers) / len(numbers):.2f}")
    print(f"Nilai Unik:        {len(set(numbers))}")
    print()
    print("=" * 80)
    print()
    
    while True:
        try:
            user_input = input("[STEP 4] Masukkan nilai yang ingin dicari (atau 'keluar' untuk berhenti): ").strip()
            
            if user_input.lower() in ['keluar', 'exit', 'quit', 'q']:
                print("\n[OK] Terima kasih telah menggunakan program ini!")
                break
            
            try:
                target = int(user_input)
            except ValueError:
                print("[ERROR] Input tidak valid! Silakan masukkan bilangan bulat.")
                print()
                continue
            
           
            print()
            print(f"Mencari nilai: {target}")
            print("-" * 80)
            
            index, comparisons = linear_search(numbers, target)
            stats = calculate_statistics(numbers, target, index, comparisons)
            
            
            if stats['ditemukan']:
                print(f"[OK] DITEMUKAN!")
                print(f"  Indeks:             {stats['indeks']}")
                print(f"  Nilai:              {stats['nilai']}")
                print(f"  Perbandingan:       {stats['total_perbandingan']} dari {stats['total_elemen']}")
                print(f"  Efisiensi:          {stats['efisiensi']}")
                
                
                print()
                print(f"  Elemen sekitar (±2 posisi dari indeks {stats['indeks']}):")
                start = max(0, stats['indeks'] - 2)
                end = min(len(numbers), stats['indeks'] + 3)
                
                for i in range(start, end):
                    if i == stats['indeks']:
                        print(f"    [{i:3d}]: {numbers[i]:4d}  ← TARGET")
                    else:
                        print(f"    [{i:3d}]: {numbers[i]:4d}")
            else:
                print(f"[NOT FOUND] TIDAK DITEMUKAN!")
                print(f"  Nilai yang dicari:  {target}")
                print(f"  Perbandingan:       {stats['total_perbandingan']} dari {stats['total_elemen']}")
                print(f"  Efisiensi:          {stats['efisiensi']}")
                print()
                print("  Program memeriksa SEMUA elemen tanpa menemukan target.")
            
            print()
            print("=" * 80)
            print()
        
        except KeyboardInterrupt:
            print("\n\n[OK] Program dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"[ERROR] Error: {e}")
            print()


if __name__ == "__main__":
    main()