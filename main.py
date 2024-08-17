"Program Management Kontak"

kontak1 = {"Nama" : "RRQ", "Email" : "rrq@python.com"}
kontak2 = {"Nama" : "Evos", "Email" : "evos@python.com"}
kontak3 = {"Nama" : "Onic", "Email" : "onic@python.com"}

kontak = [kontak1, kontak2, kontak3]

def melihat_kontak():
    # Melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f"\n{num}. {item['Nama']} ({item['Email']})")
    else:
        print("Kontak masih kosong")
        return 1

def menambahkan_kontak():
    # Menambahkan kontak
    Nama = input("Masukkan nama kontak yang baru: ")
    Email = input("Masukkan email kontak yang baru: ")
    kontak_baru = {'Nama': Nama, 'Email': Email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")

def menghapus_kontak():
    # Menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        hapus = int(input("Masukkan nama kontak yang ingin dihapus: "))
        del kontak[hapus - 1]
        print(f"Kontak yang dimaksud berhasil dihapus")

while True:
    print("\nMenu Kontak")
    print("1. Melihat Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3, atau 4): ")

    if pilihan == '1':
        melihat_kontak()
    elif pilihan == '2':
        menambahkan_kontak()
    elif pilihan == '3':
        menghapus_kontak()
    elif pilihan == '4':
        #Keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")