"Program Management Kontak"

class Kontak:
    def __init__(self):
        self.kontak = []
    def melihat_kontak(self):
        # Melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"\n{num}. {item['Nama']} ({item['Email']})")
        else:
            print("Kontak masih kosong")
            return 1

    def menambahkan_kontak(self):
        # Menambahkan kontak
        Nama = input("Masukkan nama kontak yang baru: ")
        Email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'Nama': Nama, 'Email': Email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            hapus = int(input("Masukkan nama kontak yang ingin dihapus: "))
            del self.kontak[hapus - 1]
            print(f"Kontak yang dimaksud berhasil dihapus")

kontak_kantor = Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3, atau 4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()
    elif pilihan == '2':
        kontak_kantor.menambahkan_kontak()
    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()
    elif pilihan == '4':
        #Keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")