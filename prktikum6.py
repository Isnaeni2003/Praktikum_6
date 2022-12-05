
print("_______________ Khaerunnisa Isnaeni Lestari______________")
print("PROGRAM MENAMPILKAN DAFTAR MAHASISWA")
print("====================================")

data = []

def show() :
		if len(data) <= 0:
			print("===========MENAMPILKAN DATA MAHASISWA==========")
			print("BELUM ADA DATA")
		else :
			for x in range(len(data)) :
				print("=================================")
				print("  No  |  Nama  |  NIM  |  Nilai  |")
				print("==================================")
				for i, x in enumerate (data):
					print(f" {i}   |   {x['Nama']}   |   {x['NIM']}   |   {x['Nilai']}   |")


def insert() :
	print("========TAMBAH DATA MAHASISWA=======")
	nama = input("Nama Mahasiswa : ")
	nim = input("NIM Mahasiswa : ")
	nilai = input("Nilai Mahasiswa : ")
	main = {"Nama":nama, "NIM":nim, "Nilai":nilai}
	data.append(main)
	print("=================================")
	print("  No  |  Nama  |  NIM  |  Nilai  |")
	print("==================================")
	for i, x in enumerate (data):
		print(f" {i}   |   {x['Nama']}   |   {x['NIM']}   |   {x['Nilai']}   |")

def edit () :
	print("=========EDIT DATA MAHASISWA========")
	baris = int(input("Masukkan Nomor yang diubah : "))
	kolom = input("Pilih Nama, NIM atau Nilai : ")
	nilai = input("Masukkan perubahan : ")
	data[baris][kolom] = nilai
	print("==================================")
	print("  No  |  Nama  |  NIM  |  Nilai  |")
	print("==================================")
	for i, x in enumerate (data):
		print(f" {i}   |   {x['Nama']}   |   {x['NIM']}   |   {x['Nilai']}   |")

def delete ():
	print("=========MENGHAPUS DATA MAHASISWA=========")
	x = int(input("Masukkan nomor yang dihapus : "))
	data.pop(x)
	print("Data telah dihapus")

def exit () :
	print("========HALAMAN KELUAR=======")

		
def show_menu () :
	print("\n")
	print("______________Menu___________")
	print("[1] Show Data")
	print("[2] Insert Data")
	print("[3] Edit Data")
	print("[4] Delete Data")
	print("[5] Exit")

	menu = int(input("PILIH MENU : "))
	print("\n")

	if menu == 1 :
		show()
	elif menu == 2 :
		insert()
	elif menu == 3 :
		edit()
	elif menu == 4 :
		delete()
	elif menu == 5 :
		exit()
	else:
		print("Salah Pilih!")

while(True):
	show_menu()
	a = input("Apa anda ingin menampilkan menu (y/t) : ")
	if a == "t":
		break
	









