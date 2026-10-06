#Kalkulator sederhana


def tambah(x, y):
    return x + y


def kurang(x, y):
    return x - y


def kali(x, y):
    return x * y


def bagi(x, y):
    if y == 0:
        return "Error: tidak bisa dibagi dengan 0"
    return x / y


def main():
    print("Pilih Operasi")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan not in ("1", "2", "3", "4"):
        print("Pilihan tidak valid.")
        return

    try:
        angka1 = float(input(""))
        angka2 = float(input(""))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if pilihan == "1":
        hasil = tambah(angka1, angka2)
        operator = "+"
    elif pilihan == "2":
        hasil = kurang(angka1, angka2)
        operator = "-"
    elif pilihan == "3":
        hasil = kali(angka1, angka2)
        operator = "*"
    else:
        hasil = bagi(angka1, angka2)
        operator = "/"

    print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")


if __name__ == "__main__":
    main()