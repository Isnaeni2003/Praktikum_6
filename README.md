# Praktikum_6
## Fungsi Def
Apa itu fungsi (def) pada python?
Fungsi pada python adalah kumpulan perintah atau baris kode yang dikelompokkan menjadi satu kesatuan untuk kemudian bisa dipanggil atau digunakan berkali-kali. Sebuah fungsi bisa menerima parameter, bisa mengembalikan suatu nilai, dan bisa dipanggil berkali-kali secara independen. Dengan fungsi kita bisa memecah program besar yang kita tulis, menjadi bagian-bagian kecil dengan tugasnya masing-masing. Juga, fungsi akan membuat kode program kita menjadi lebih “reusable” dan lebih terstruktur.
## Fungsi Lambda
Apa itu fungsi lambda pada python?
Lambda expression di Python adalah sebuah ekspresi untuk membuat fungsi, lambda sendiri berasal dari teori kalkulus, yakni Lambda Calculus yang dikenalkan oleh Alonzo Church di tahun 1930. Berkat lambda, kita bisa membuat fungsi tanpa nama atau dikenal juga dengan anonymous function, Intinya, lambda digunakan untuk membuat fungsi dalam satu baris ekspresi.Lambda bisa memiliki lebih dari satu argumen atau parameter, tapi hanya bisa memiliki satu ekspresi atau isi,karena fungsi lambda tidak punya nama, jadi kita butuh variabel untuk menyimpannya.
Ini adalah format untuk membuat fungsi lambda: lambda args : expression
## Latihan Menggunakan Fungsi Lambda
![plgbnr](https://user-images.githubusercontent.com/115929351/205598354-fadbc27d-1335-49b6-8fda-d8ae4c7e777d.png)
Penjelasan :
1. Ini merupakan hasil pangkat menggunakan fungsi lambda, dengan memiliki lebih dari 1 parameter yaitu variabel x, dengan formula x**2 dilanjut dengan memasukkan integer angka.
2. Ini adalah hasil penjumlahan serta pangkat menggunakan fungsi lambda, dengan memasukkan 2 variabel yaitu x,y dilanjut dengan formula x**2 + y**2 dan memasukkan integer angka.
3. Ini adalah hasil pembagian argumen menggunakan fungsi lambda, yaitu dengan membuat formula "sum" atau penjumlahan dari angka di dalam argumen tersebut kemudian dibagi dengan "len" atau banyaknya suku argumen.
4. Ini merupakan penggabungan dari beberapa string menggunakan fungsi lambda, yaitu dengan memberikan statement join dan menambahkan "@" kemudian membuat dictionary dari beberapa string.
## Output Latihan Menggunakan Fungsi Lambda
![latbnrbt](https://user-images.githubusercontent.com/115929351/205597399-b2958b96-909b-46f7-802b-bc7d4c0d8475.png)
Berikut adalah hasil output dari penggunaan fungsi lambda, lambda otomatis menghtiung parameter tanpa membutuhkan variabel lebih atau return. Intinya, lambda digunakan untuk membuat fungsi dalam satu baris dan ia bersifat anonymous, lambda bisa kita simpan di dalam variabel dan dijadikan sebagai parameter.
## Membuat Program Menampilkan Data Mahasiswa (Penggunaan Fungsi Def)
![codingpra5](https://user-images.githubusercontent.com/115929351/205598211-258f6e64-1cfc-4572-92f9-a7c8c2b02d61.png)
Tugas Praktikum

Buat program sederhana dengan mengaplikasikan penggunaan fungsi
yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:

• Fungsi tambah() untuk menambah data

• Fungsi tapilkan() untuk menampilkan data

• Fungsi hapus(nama) untuk menghapus data berdasarkan nama

• Fungsi ubah(nama) untuk mengubah data berdasarkan nama

• Buat flowchart dan penjelasan programnya pada README.md.

• Commit dan push repository ke github.

## Step by Step
![carbon(4)](https://user-images.githubusercontent.com/115929351/205602494-7ed54f89-f064-4f9b-acec-fbbfc83e3712.png)

1. Saya membuat dictrionary kosong, dan akan memakaikan fungsi def pada setiap menu. Saya membuat opsi atau perintah dari setiap menu yaitu [1]Show Data, [2]Insert Data, [3]Edit Data, [4]Delete Data. dan [5]Exit.

2.  Menu Show untuk menampilkan tabel data mahasiswa, disini saya menggunakan statement if len untuk kondisi jika data kurang dari 0, maka akan menampilkan "BELUM ADA DATA". dan else untuk kondisi jika data tersebut terdapat dalam data maka saya menggunakan statement for untuk mengulang kembali dan menampilkan tabel data mahasiswa.

3. Menu Insert untuk menambahkan data mahasiswa baru, saya membuat inputan "Nama, NIM, Nilai" kemudian membuat satu dictionary yang berisi item tersebut kemudian menggabungkannya dengan append. Dan kembali mengguanakan statement for untuk mengulang kembali tabel data mahsiswa.

4. Menu Edit untuk melakukan perubahan pada data mahasiswa, saya membuat variabel integer serta string untuk membuuat pilihan apakah melakukan perubahan pada (Nama, NIM< atau Nilai) dan variabel nilai untuk membuat inputan peruabhan apa yang akan diinput.Dan membuat indeks seperti data[][] untuk menentukan posisi mana yang akan diubah/diedit.

5. Menu Delete untuk menghapus data mahasiswa, saya membuat variabel inputan untuk menanyakan nomor berapa yang ingin dihapus serta menggunakan methods pop untuk menghapus sebaris atau  pada data jika menggunakan clear maka menghapus smua item yang ada di dalam data.

6. Menu Exit untuk halaman keluar program, karena disini saya menempatkan while true dibagian bawah pada bagian def show_menu maka saya menempatkan break dibawah while true sebagai bagian dari proses looping. Maka saya memunculkan "Apakah anda ingin menampilkan menu (y/t)" sebagai opsi untuk exit, jika user menginput "t" maka akan otomatis keluar dari program tersebut.

7. Terakhir saya membuat tampilan menu, seperti :

[1] Show Data

[2] Insert Data

[3] Edit Data

[4] Delete Data

[5] Exit

Dan menggunakan integer sebagai inputan serta statemnent if, untuk kondisi jiika user memilih user memilih no 1 pada halaman inputan, maka saya menambahkan show () dibawah if untuk memanggil fungsi def sebelumnya yang saya sudah buat diawal, begitu pula seterusnya elif menu == 2, maka saya menambahkan insert () dibawah elif untuk memanggil fungsi def dari insert. Dan begitupun pada no 3,4,5. Dan memeberikan statement while true, serta break untuk terus mengulang opsi menu tersebut sampai user memilih untuk tidak menampilkan menu kembali maka program akan break.
## Output Membuat Program Menampilkan Data Mahasiswa (Penggunaan Fungsi Def)
![showmenu](https://user-images.githubusercontent.com/115929351/205616520-9d65f8f4-7a25-432c-a0b9-9224d2534fe0.png)
1. Berikut adalah output dari tampilan menu Show Data, disini saya belum menginput data mahasiswa alias banyak data < 0 maka program akan menampilkan "BELUM ADA DATA", jika user sudah menambah data mahasiswa dan kembali pada menu Show Data maka program akan menampilkan data mahasiswa tersebut.
![insert](https://user-images.githubusercontent.com/115929351/205621252-1e509ec6-6d40-45d0-bf90-e0271aaab7e9.png)
2. Ini adalah hasil output dari menu Insert Data, saya menambahkan data mahasiswa contohnya (Nama : Isna, NIM 021, Nilai 89) dan program menampilkan tabel data mahasiswa.
![edit](https://user-images.githubusercontent.com/115929351/205622099-afde882e-5527-4f42-a250-b9da2e497be4.png)
3. Berikut merupakan tampilan output dari menu edit, disini terdapat beberapa 3 data mahasiswa yaitu Isna, Jeni dan Sera masing-masing beserta NIM dan Nilainya, kemudian saya melakukan perubahan dengan menginput nomor yang akan diubah, kemudian menginput item yang ingin diubah apakah (Nama, NIM, Nilai) saya memilih "Nama" : Jono, pada nomor 1, data mahasiswa yang sebelumnya bernama Jeni, saya edit nama nya menjadi Jono.
![delete](https://user-images.githubusercontent.com/115929351/205623203-c6ac10c1-af44-4677-80c8-82cda9ef38de.png)
4. Selanjutnya ini adalah output dari menu delete, disini saya mempunyai 3 data mahasiswa yaitu, Isna, Jono, dan Sera serta saya ingun menghapus data mahasiswa bernama Sera beserta NIM dan Nilainya dengan menginput nomor mahasiswa tersebut, dan status nya "Data telah dihapus" kemudian saya memilih opsi menu no 1 yaitu Show Data untuk mengecek apakah data yang saya delete telah terhapus, dan ternyata work it data yang ditampilkan tersisa 2 data mahasiswa yaitu Isna dan Jono.
![exit](https://user-images.githubusercontent.com/115929351/205626047-a9666d8f-ca9e-4f07-a13a-ee9199fbbb50.png)
5. Dan terakhir adalah opsi menu exit, ketika user memutuskan untuk tidak lagi menampilkan menu atau "t", maka akan otomatis keluar dari program tersebut.

 


