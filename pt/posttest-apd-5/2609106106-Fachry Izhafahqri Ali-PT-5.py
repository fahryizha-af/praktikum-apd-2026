import os

data_cuaca = [
    ["Samarinda", 30, "Cerah", 15]
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENCATATAN CUACA ===")
    print("1. Tambah Data Cuaca (Create)")
    print("2. Lihat Data Cuaca (Read)")
    print("3. Ubah Data Cuaca (Update)")
    print("4. Hapus Data Cuaca (Delete)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    # CREATE
    if pilihan == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== TAMBAH DATA CUACA ===")
        kota = input("Masukkan nama kota: ")
        suhu = int(input("Masukkan suhu (°C): "))
        kondisi = input("Masukkan kondisi cuaca: ")
        tanggal = int(input("Masukkan tanggal: "))

        data_baru = [kota, suhu, kondisi, tanggal]
        data_cuaca.append(data_baru)

        print("Data cuaca berhasil ditambahkan!")
        input("\nTekan Enter untuk kembali ke menu...")

    # READ
    elif pilihan == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LIHAT DATA CUACA ===")

        if len(data_cuaca) == 0:
            print("Data cuaca masih kosong.")
        else:
            for i in range(len(data_cuaca)):
                print("\nData ke-", i + 1)
                print("Kota     :", data_cuaca[i][0])
                print("Suhu     :", data_cuaca[i][1], "°C")
                print("Kondisi  :", data_cuaca[i][2])
                print("Tanggal  :", data_cuaca[i][3])
        input("\nTekan Enter untuk kembali ke menu...")

    # UPDATE
    elif pilihan == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== UBAH DATA CUACA ===")

        if len(data_cuaca) == 0:
            print("Tidak ada data yang bisa diubah.")
        else:
            for i in range(len(data_cuaca)):
                print(i + 1, ".", data_cuaca[i])

            nomor = int(input("Pilih nomor data yang ingin diubah: "))

            if nomor >= 1 and nomor <= len(data_cuaca):
                kota = input("Masukkan nama kota baru: ")
                suhu = int(input("Masukkan suhu baru: "))
                kondisi = input("Masukkan kondisi cuaca baru: ")
                tanggal = int(input("Masukkan tanggal baru: "))

                # Mengganti data lama dengan data baru
                data_cuaca[nomor - 1] = [kota, suhu, kondisi, tanggal]

                print("Data berhasil diganti!")
            else:
                print("Nomor data tidak ditemukan.")
        input("\nTekan Enter untuk kembali ke menu...")

    # DELETE
    elif pilihan == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== HAPUS DATA CUACA ===")

        if len(data_cuaca) == 0:
            print("Tidak ada data yang bisa dihapus.")
        else:
            for i in range(len(data_cuaca)):
                print(i + 1, ".", data_cuaca[i][0],
                      "-", data_cuaca[i][2])

            nomor = int(input("Pilih nomor data yang ingin dihapus: "))

            if nomor >= 1 and nomor <= len(data_cuaca):
                data_cuaca.pop(nomor - 1)
                print("Data cuaca berhasil dihapus!")
            else:
                print("Nomor data tidak ditemukan.")
        input("\nTekan Enter untuk kembali ke menu...")

    # KELUAR
    elif pilihan == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Mohon maaf dan terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")