# Portofolio Website - Tugas Mata Kuliah Pemrograman Berbasis Platform

**Nama**        : Muhammad Zaki Radipradana  
**NPM**         : 2506599541  
**Kelas**       : PBP D  
**Link Deploy** : https://muhammad-zaki54-myportofolio.pws.cs.ui.ac.id/  

---

## Deskripsi Proyek
Proyek ini adalah sebuah website portofolio pribadi yang dibangun secara bertahap dan nantinya akan menjadi luaran akhir mahasiswa dari mata kuliah Pemrograman Berbasis Platform (PBP) di Fakultas Ilmu Komputer, Universitas Indonesia. Website ini baru dapat berfungsi untuk menampilkan profil, riwayat pendidikan, dan pengalaman saya. Namun kedepannya, akan ditambahkan fitur-fitur lain yang dapat menunjang portofolio ini, sehingga dapat lebih lengkap lagi. 

---

## Progress Mingguan
- 2 Sept 2026 - Tutorial 0 & 1: Melakukan setup dan inisialisasi project 
- 7 Sept 2026 - Tugas 1: Menambahkan section educations dan experiences, serta menambahkan animasi highlight pada nav bar 
- 9 Sept 2026 - Tutorial 2: Mengimplementasikan MVT untuk section Experience
- 14 Sept 2026 - Tugas 2: Menambahkan section Education dengan mengimplementasikan MVT
- 16 Sept 2026 - Tutorial 3: Menambahkan fitur create, search, dan delete pada section experience serta mengimplementasikan autentikasi saat create/delete
- 21 Sept 2026 - Tugas 3: Menambahkan fitur create, delete, dan update pada section education dengan mengimplementasikan autentikasi serta memunculkan nofitikasi status  

---

### Tugas 1

1. Ya, saya menggunakan elemen semantik section dan article pada struktur HTML yang saya buat. Kedua elemen tersebut mempermudah saya dalam menjaga kerapihan tata letak komponen-komponen pada design web saya. Elemen article membungkus komponen-komponen kecil yang nantinya dikelompokkan kembali berdasarkan bagian yang bersesuaian menggunakan elemen section untuk kemudian disajikan kepada user.

2. Tantangan cukup besar saya hadapi adalah saat membuat section Experiences dan Header yang responsif pada tampilan desktop dan mobile. Pada tampilan mobile, kedua section tersebut menjadi sangat sempit dan membuat tulisan yang ada di section-section tersebut saling bertabrakan. Oleh karena itu, saya mengutamakan keterbacaan tulisan, sehingga user dari kedua device tetap dapat memahami hal yang disampaikan pada web.

3. Sebuah website portofolio biasanya akan memiliki section Contact Form yang berfungsi agar user (recruiter) dapat mengontak pemilik website secara langsung tanpa perantara platform lain. Namun, karena website yang telah dibuat sejauh ini merupakan static web murni, ketika user mencoba memasukkan sebuah input (contoh: email dan pesan), struktur website tidak memiliki komponen untuk memproses dan menyimpan data masukan tersebut. Untuk itu, kedepannya saya ingin mengimplementasikan fungsionalitas dinamis berupa database agar website saya dapat menyimpan input dan memiliki section Contact Form yang dapat berjalan dengan baik. 

**AI Disclosure**:
Secara umum, pada tugas pertama ini, saya dibantu oleh Gemini. Strategi saya dalam menggunakannya adalah saya menjadikan Gemini sebagai alat bantu dalam memahami potongan kode yang telah dan akan dibuat. Kemudian saya juga memintanya untuk memberikan saya contoh atau step-by-step pengimplementasian bagian yang ingin saya bangun dengan tetap memberikan penjelasan dari kode tersebut agar saya tetap mengerti apa yang akan dilakukan oleh program yang saya rancang. 

**Link**: https://share.gemini.google/HSTklJEH4NyP

---

### Tugas 2

1. Setelah user membuka/mengakses URL halaman portofolio baru, Django akan memetakan URL tersebut ke View melalui urls.py. Setelah itu, View akan mengambil dan memproses data dari Model apabila dibutuhkan. Lalu, View akan mengirim context-nya ke Template dan Django akan mengembalikan HTML yang telah dirender sebagai response ke browser.

    Peran Komponen-Komponen dalam Alur Tersebut:
    - urls.py proyek : menghubungkan URL proyek ke aplikasi main
    - urls.py aplikasi : menentukan view yang menangani URL proyek
    - view : mengambil data dari Model dan mengirimkannya melalui context ke Template
    - model : mengatur dan mengelola data aplikasi
    - template : menentukan tampilan akhir HTML

2. Sebab, jika data ditulis langsung di dalam template, setiap perubahan informasi pada portofolio mengharuskan kita untuk mengubah kode template secara manual. Lain halnya jika data disimpan pada model. Dengan menggunakan model, data dapat dengan mudah ditambah, diubah, atau dihapus tanpa perlu mengubah struktur templatenya. Hal ini dapat dilakukan karena model terhubung secara langsung dengan database. Dengan demikian, penggunaan model dapat membuat aplikasi lebih terstuktur dan pemeliharaannya menjadi lebih mudah, terutama ketika jumlah data semakin banyak. Selain itu, dengan menggunakan model, pengembangan aplikasi menjadi lebih mudah karena data yang sama dapat digunakan oleh berbagai halaman/fitur.

3. Perbedaannya adalah fungsi makemigrations menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Sedangkan, fungsi migrate mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya. Contoh perubahan model yang mengharuskan kedua fungsi tersebut dijalankan adalah ketika kita ingin menambahkan suatu atribut atau mengubah tipe data yang dapat disimpan dalam suatu atribut karena terjadi perubahan pada model, sehingga fungsi makemigrations dan migrate perlu dijalankan.

**AI Disclosure**:
Pada tugas 2 ini saya menggunakan AI Gemini dengan strategi, yaitu memetakan terlebih dahulu hal-hal apa saya yang perlu dikerjakan. Kemudian, berdasarkan Tutorial 2, saya mencoba mengimplementasikannya sendiri dan meminta AI untuk memeriksanya apakah sudah benar atau belum. Saya juga meminta AI untuk membuat file HTML dan CSS untuk section Education yang nantinya saya animasikan sendiri tampilannya. Terakhir, saya meminta bantuan AI untuk merancang unit test dari modul baru yang telah dibuat. 

**Link**: https://share.gemini.google/CUMTEmMSbvXu

---

### Tugas 3

1. Karena ModelForm dapat digunakan untuk membuat boilerplate dari sebuah form yang sifatnya reusable dan dapat dikustomisasi menggunakan metadata. Dengan demikian, kita tidak perlu mendefinisikan sendiri struktur dari form tersebut dan kode yang dibuat menjadi lebih ringkas dibandingkan jika kita membuat form HTML secara manual. Pada form yang kita buat juga wajib ditambahkan csrf_token karena token tersebut merupakan sebuah token rahasia yang bersifat unik dan dibuat oleh server untuk melindungi aplikasi dari request yang tidak terotorisasi.

2. JSON lebih disukai dibandingkan XML pada aplikasi web modern karena ukurannya yang lebih ringkas, parser yang sangat cepat, dan di sisi frontend, integrasinya sangat natural dengan JavaScript.

3. Alurnya adalah saat user mengakses suatu URL tertentu, Django akan mencocokkan URL tersebut dengan fungsi view. Fungsi view kemudian mengambil data portofolio dari Model. Kemudian, data tersebut akan dilakukan serialization menjadi sebuah JSON dan dikembalikan kepada user melalui HttpResponse. Proses serialization perlu dilakukan karena proses tersebut mengubah objek atau data dari Model Django menjadi format data yang dapat direpresentasikan sebagai JSON, sehingga data tersebut dapat dikirim sebagai response kepada user.

**AI Disclosure**:
Pada tugas 3 ini saya menggunakan Gemini AI dengan strategi, yaitu pertama-tama saya meminta AI untuk memetakan terlebih dahulu apa saja yang saya perlu kerjakan di tugas 3 ini dan apa yang perlu diimplementasikan kembali dari tutorial 3 yang telah dilakukan sebelumnya. Kemudian, berdasarkan tutorial 3, saya mencoba untuk mengimplementasikannya sendiri pada bagian yang ingin saya bangun di tugas ini, yaitu education section lalu saya meminta AI untuk memeriksanya. Saya juga meminta AI untuk menyesuaikan file style.css dengan file-file template baru yang dibuat, yaitu education_form.html dan education_delete_modal.html. Setelahnya, saya meminta AI untuk menambahkan tombol add, delete (icon trash can), dan status notification pada template education.html. Terakhir, saya meminta AI untuk menjelaskan bagaimana cara membuat bagian update form pada education section dan menambahkan tombol update (icon pensil) di sebelah tombol delete. Saat memasangkan kedua tombol tersebut, saya mengalami sebuah kendala/bug, yaitu letak kedua tombol tidak dapat sejajar. Saya meminta Gemini untuk melakukan debugging namun belum mendapatkan solusinya, hingga akhirnya saya berhasil mendapatkan solusinya dari bantuan ChatGPT.

**Link**:
- https://share.gemini.google/yOzl5Y8JX8Ip 
- https://chatgpt.com/share/6ab151cb-4efc-83ec-bb1b-0ddac3524d13
