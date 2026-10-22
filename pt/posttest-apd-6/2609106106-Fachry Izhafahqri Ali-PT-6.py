import os

data_cuaca = {
    1: {"kota": "Samarinda", "suhu": 30, "kondisi": "Cerah", "tanggal": 15}
}
id_berikutnya = 2  # ID otomatis untuk data baru

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

        # CREATE dan UPDATE (input datanya sama, jadi digabung)
        if pilihan == "1" or pilihan == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            id_dipilih = 0

            if pilihan == "1":
                print("=== TAMBAH DATA CUACA ===")
            else:
                print("=== UBAH DATA CUACA ===")
                if not data_cuaca:
                    print("Tidak ada data yang bisa diubah.")
                    input("\nTekan Enter untuk kembali ke menu...")
                    continue

                for id_data, d in data_cuaca.items():
                    print(f"ID {id_data}. {d['kota']} - {d['kondisi']} ({d['suhu']}°C, tgl {d['tanggal']})")

                while True:
                    try:
                        id_dipilih = int(input("Masukkan ID data yang ingin diubah: "))
                    except ValueError:
                        print("Input harus berupa angka!")
                        continue
                    if id_dipilih in data_cuaca:
                        break
                    print("ID data tidak ditemukan.")

           
            while True:
                kota = input("Masukkan nama kota: ").strip()
                if kota != "":
                    kota = kota.title()
                    break
                print("Input tidak boleh kosong!")

            # Input suhu (angka, -90 sampai 60)
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
                data_cuaca[id_berikutnya] = data_baru
                print(f"Data cuaca berhasil ditambahkan dengan ID {id_berikutnya}!")
                id_berikutnya += 1
            else:
                data_cuaca[id_dipilih] = data_baru
                print("Data berhasil diganti!")

            input("\nTekan Enter untuk kembali ke menu...")

        # READ
        elif pilihan == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== LIHAT DATA CUACA ===")

            if not data_cuaca:
                print("Data cuaca masih kosong.")
            else:
                for id_data, d in data_cuaca.items():
                    print(f"\nID       : {id_data}")
                    print(f"Kota     : {d['kota']}")
                    print(f"Suhu     : {d['suhu']} °C")
                    print(f"Kondisi  : {d['kondisi']}")
                    print(f"Tanggal  : {d['tanggal']}")
            input("\nTekan Enter untuk kembali ke menu...")

        # DELETE
        elif pilihan == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== HAPUS DATA CUACA ===")

            if not data_cuaca:
                print("Tidak ada data yang bisa dihapus.")
            else:
                for id_data, d in data_cuaca.items():
                    print(f"ID {id_data}. {d['kota']} - {d['kondisi']} ({d['suhu']}°C, tgl {d['tanggal']})")

                while True:
                    try:
                        id_dipilih = int(input("Masukkan ID data yang ingin dihapus: "))
                    except ValueError:
                        print("Input harus berupa angka!")
                        continue
                    if id_dipilih in data_cuaca:
                        break
                    print("ID data tidak ditemukan.")

                del data_cuaca[id_dipilih]
                print("Data cuaca berhasil dihapus!")
            input("\nTekan Enter untuk kembali ke menu...")

        # KELUAR
        elif pilihan == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Mohon maaf dan terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            input("\nTekan Enter untuk kembali ke menu...")

except (KeyboardInterrupt, EOFError):
    print("\n\nProgram dihentikan. Terima kasih!")