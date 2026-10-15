import os

data_cuaca = [
    {"kota": "Samarinda", "suhu": 30, "kondisi": "Cerah", "tanggal": 15}
]

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SISTEM PENCATATAN CUACA ===")
        print("1. Tambah Data Cuaca (Create)")
        print("2. Lihat Data Cuaca (Read)")
        print("3. Ubah Data Cuaca (Update)")
        print("4. Hapus Data Cuaca (Delete)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1" or pilihan == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            nomor = 0

            if pilihan == "1":
                print("=== TAMBAH DATA CUACA ===")
            else:
                print("=== UBAH DATA CUACA ===")
                if len(data_cuaca) == 0:
                    print("Tidak ada data yang bisa diubah.")
                    input("\nTekan Enter untuk kembali ke menu...")
                    continue

                for i, d in enumerate(data_cuaca, start=1):
                    print(f"{i}. {d['kota']} - {d['kondisi']} ({d['suhu']}°C, tgl {d['tanggal']})")

                while True:
                    try:
                        nomor = int(input("Pilih nomor data yang ingin diubah: "))
                    except ValueError:
                        print("Input harus berupa angka!")
                        continue
                    if 1 <= nomor <= len(data_cuaca):
                        break
                    print("Nomor data tidak ditemukan.")

            while True:
                kota = input("Masukkan nama kota: ").strip()
                if kota != "":
                    kota = kota.title()
                    break
                print("Input tidak boleh kosong!")

            while True:
                try:
                    suhu = int(input("Masukkan suhu (°C): "))
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                if -90 <= suhu <= 60:
                    break
                print("Suhu harus antara -90 sampai 60.")

            while True:
                kondisi = input("Masukkan kondisi cuaca: ").strip()
                if kondisi != "":
                    kondisi = kondisi.capitalize()
                    break
                print("Input tidak boleh kosong!")

            while True:
                try:
                    tanggal = int(input("Masukkan tanggal (1-31): "))
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                if 1 <= tanggal <= 31:
                    break
                print("Tanggal harus antara 1 sampai 31.")

            data_baru = {"kota": kota, "suhu": suhu, "kondisi": kondisi, "tanggal": tanggal}

            if pilihan == "1":
                data_cuaca.append(data_baru)
                print("Data cuaca berhasil ditambahkan!")
            else:
                data_cuaca[nomor - 1] = data_baru
                print("Data berhasil diganti!")

            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== LIHAT DATA CUACA ===")

            if len(data_cuaca) == 0:
                print("Data cuaca masih kosong.")
            else:
                for i, d in enumerate(data_cuaca, start=1):
                    print(f"\nData ke-{i}")
                    print(f"Kota     : {d['kota']}")
                    print(f"Suhu     : {d['suhu']} °C")
                    print(f"Kondisi  : {d['kondisi']}")
                    print(f"Tanggal  : {d['tanggal']}")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== HAPUS DATA CUACA ===")

            if len(data_cuaca) == 0:
                print("Tidak ada data yang bisa dihapus.")
            else:
                for i, d in enumerate(data_cuaca, start=1):
                    print(f"{i}. {d['kota']} - {d['kondisi']} ({d['suhu']}°C, tgl {d['tanggal']})")

                while True:
                    try:
                        nomor = int(input("Pilih nomor data yang ingin dihapus: "))
                    except ValueError:
                        print("Input harus berupa angka!")
                        continue
                    if 1 <= nomor <= len(data_cuaca):
                        break
                    print("Nomor data tidak ditemukan.")

                data_cuaca.pop(nomor - 1)
                print("Data cuaca berhasil dihapus!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Mohon maaf dan terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            input("\nTekan Enter untuk kembali ke menu...")

except (KeyboardInterrupt, EOFError):
    print("\n\nProgram dihentikan. Terima kasih!")