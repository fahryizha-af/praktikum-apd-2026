import os

data_cuaca = {
    1: {"kota": "Samarinda", "suhu": 30, "kondisi": "Cerah", "tanggal": 15}
}
id_berikutnya = 2
SUHU_MIN = -90
SUHU_MAX = 60
TANGGAL_MIN = 1
TANGGAL_MAX = 31

def input_kota():
    while True:
        try:
            kota = input("Masukkan nama kota: ").strip()
            if kota == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            print(e)
        else:
            return kota.title()

def input_kondisi():
    while True:
        try:
            kondisi = input("Masukkan kondisi cuaca: ").strip()
            if kondisi == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            print(e)
        else:
            return kondisi.capitalize()

def input_data_cuaca():
    kota = input_kota()
    suhu = input_angka("Masukkan suhu (°C): ", SUHU_MIN, SUHU_MAX)
    kondisi = input_kondisi()
    tanggal = input_angka("Masukkan tanggal (1-31): ", TANGGAL_MIN, TANGGAL_MAX)
    return {"kota": kota, "suhu": suhu, "kondisi": kondisi, "tanggal": tanggal}

def input_angka(label, minimum, maksimum):
    while True:
        try:
            angka = int(input(label))
        except ValueError:
            print("Input harus berupa angka!")
        else:
            if minimum <= angka <= maksimum:
                return angka
            print(f"Nilai harus antara {minimum} sampai {maksimum}.")

def input_id(aksi):
    while True:
        try:
            id_pilih = int(input(f"Masukkan ID data yang ingin {aksi}: "))
            if id_pilih not in data_cuaca:
                raise KeyError(id_pilih)
        except ValueError:
            print("Input harus berupa angka!")
        except KeyError:
            print("ID data tidak ditemukan.")
        else:
            return id_pilih

def daftar_ringkas():
    for id_data, d in data_cuaca.items():
        print(f"ID {id_data}. {d['kota']} - {d['kondisi']} ({d['suhu']}°C, tgl {d['tanggal']})")

def tambah_cuaca():
    global id_berikutnya
    print("=== TAMBAH DATA CUACA ===")
    data_cuaca[id_berikutnya] = input_data_cuaca()
    print(f"Data cuaca berhasil ditambahkan dengan ID {id_berikutnya}!")
    id_berikutnya += 1

def lihat_cuaca():
    print("=== LIHAT DATA CUACA ===")
    if len(data_cuaca) <= 0:
        print("Data cuaca masih kosong.")
    else:
        for id_data, d in data_cuaca.items():
            print(f"\nID       : {id_data}")
            print(f"Kota     : {d['kota']}")
            print(f"Suhu     : {d['suhu']} °C")
            print(f"Kondisi  : {d['kondisi']}")
            print(f"Tanggal  : {d['tanggal']}")

def ubah_cuaca():
    print("=== UBAH DATA CUACA ===")
    if len(data_cuaca) <= 0:
        print("Tidak ada data yang bisa diubah.")
    else:
        daftar_ringkas()
        id_dipilih = input_id("diubah")
        data_cuaca[id_dipilih] = input_data_cuaca()
        print("Data berhasil diganti!")

def hapus_cuaca():
    print("=== HAPUS DATA CUACA ===")
    if len(data_cuaca) <= 0:
        print("Tidak ada data yang bisa dihapus.")
    else:
        daftar_ringkas()
        id_dipilih = input_id("dihapus")
        del data_cuaca[id_dipilih]
        print("Data cuaca berhasil dihapus!")


def tampilkan_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENCATATAN CUACA ===")
    print("1. Tambah Data Cuaca (Create)")
    print("2. Lihat Data Cuaca (Read)")
    print("3. Ubah Data Cuaca (Update)")
    print("4. Hapus Data Cuaca (Delete)")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        if pilihan == "1":
            tambah_cuaca()
        elif pilihan == "2":
            lihat_cuaca()
        elif pilihan == "3":
            ubah_cuaca()
        elif pilihan == "4":
            hapus_cuaca()
        elif pilihan ==  "5":
            print("Mohon maaf dan terima kasih!")
            exit()
        else:
            raise ValueError("Pilihan tidak valid, silakan coba lagi.")
    except ValueError as e:
        print(e)
    input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    try:
        while True:
            tampilkan_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram dihentikan. Terima kasih!")
    finally:
        print("Data tidak disimpan ke file dan akan hilang saat program ditutup.")
