import math

def masukan_angka():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    return angka1, angka2

def penjumlahan(angka1, angka2):
    return angka1 + angka2

def pengurangan(angka1, angka2):
    return angka1 - angka2

def pengalian(angka1, angka2):
    return angka1 * angka2

def pembagian(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Pembagian dengan nol tidak diperbolehkan"

def modulus(angka1, angka2):
    return angka1 % angka2

def eksponensial(angka1, angka2):
    return angka1 ** angka2

def akar_kuadrat(angka):
    return math.sqrt(angka)

def kalkulator():
    while True:
        print("\n--- Kalkulator Sederhana ---")
        print("Pilih Menu:")
        print("0 - Masukkan angka")
        print("1 - Penjumlahan")
        print("2 - Pengurangan")
        print("3 - Pengalian")
        print("4 - Pembagian")
        print("5 - Modulus")
        print("6 - Eksponensial (pangkat)")
        print("7 - Akar Kuadrat (hanya satu angka)")
        print("8 - Keluar")
        
        pilihan = input("Input pilihan Anda: ")

        if pilihan == "0":
            angka1, angka2 = masukan_angka()
        elif pilihan == "1":
            print(f"Hasil Penjumlahan: {penjumlahan(angka1, angka2)}")
        elif pilihan == "2":
            print(f"Hasil Pengurangan: {pengurangan(angka1, angka2)}")
        elif pilihan == "3":
            print(f"Hasil Pengalian: {pengalian(angka1, angka2)}")
        elif pilihan == "4":
            print(f"Hasil Pembagian: {pembagian(angka1, angka2)}")
        elif pilihan == "5":
            print(f"Hasil Modulus: {modulus(angka1, angka2)}")
        elif pilihan == "6":
            print(f"Hasil Eksponensial: {eksponensial(angka1, angka2)}")
        elif pilihan == "7":
            angka = float(input("Masukkan satu angka untuk akar kuadrat: "))
            print(f"Hasil Akar Kuadrat: {akar_kuadrat(angka)}")
        elif pilihan == "8":
            print("Terima kasih telah menggunakan kalkulator.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

kalkulator()
