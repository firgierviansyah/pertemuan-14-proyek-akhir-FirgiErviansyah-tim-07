# PROPOSAL PROYEK : Program Pengolah dan Analisis Nilai Siswa

## 1. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan dalam proses pembelajaran. Guru perlu mengolah nilai untuk mengetahui hasil belajar siswa, menghitung rata-rata kelas, serta mengetahui nilai tertinggi dan terendah.

Apabila pengolahan dilakukan secara manual, proses tersebut dapat membutuhkan waktu dan berpotensi menimbulkan kesalahan perhitungan. Oleh karena itu, diperlukan program sederhana yang dapat membantu proses pengolahan dan analisis nilai siswa secara lebih cepat dan terstruktur.

Proyek ini dirancang menggunakan bahasa pemrograman Python dengan sistem berbasis terminal.

## 2. Pengguna dan Tujuan Program

Pengguna utama: Guru atau pengajar.

Tujuan program:

1. Mempermudah proses memasukkan dan mengolah nilai siswa.
2. Membantu menghitung statistik nilai kelas.
3. Mengetahui status ketuntasan setiap siswa.
4. Menampilkan hasil pengolahan nilai secara terstruktur.

## 3. Ruang Lingkup Proyek

Program Pengolah dan Analisis Nilai Siswa merupakan program berbasis Python yang dijalankan melalui terminal.

Fitur wajib program meliputi:

1. Membaca data nama dan nilai siswa dari file teks.
2. Memvalidasi nilai agar berada dalam rentang 0–100.
3. Menghitung rata-rata nilai siswa.
4. Menentukan nilai tertinggi dan terendah.
5. Menghitung jumlah siswa yang tuntas dan belum tuntas berdasarkan batas ketuntasan 75.
6. Menampilkan hasil analisis melalui terminal.
7. Menyimpan hasil analisis ke dalam file laporan berbentuk teks.

Data siswa disimpan dalam file data/nilai_contoh.txt, sedangkan hasil analisis disimpan dalam output/laporan_nilai.txt.

## 4. Kebutuhan Fungsional

Fitur utama yang akan dikembangkan:

1. Memasukkan data nama dan nilai siswa.
2. Memvalidasi nilai agar berada pada rentang 0–100.
3. Menghitung rata-rata nilai seluruh siswa.
4. Menampilkan nilai tertinggi dan terendah.
5. Menentukan status ketuntasan siswa berdasarkan batas nilai yang ditetapkan.
6. Menampilkan rekapitulasi hasil pengolahan nilai.

## 5. Input, Process, dan Output (IPO)

### 1. Input
- File data/nilai_contoh.txt yang berisi nama dan nilai siswa.
- Batas ketuntasan sebesar 75.

### 2. Proses
1. Membaca data siswa dari file teks.
2. Memisahkan nama dan nilai berdasarkan tanda koma.
3. Memvalidasi format data dan memastikan nilai berada pada rentang 0–100.
4. Menyimpan data yang valid ke dalam list of dictionary.
5. Menghitung rata-rata nilai.
6. Mencari nilai tertinggi dan terendah.
7. Menghitung jumlah siswa tuntas dan belum tuntas.
8. Menampilkan hasil analisis di terminal.
9. Menyimpan hasil analisis ke file laporan.

### 3. Output
- Daftar nama dan nilai siswa beserta status ketuntasan.
- Rata-rata nilai siswa.
- Nilai tertinggi dan terendah.
- Jumlah siswa tuntas dan belum tuntas.
- File laporan output/laporan_nilai.txt.

## 6. Algoritma dan Pseudocode

MULAI

    Tetapkan batas ketuntasan = 75

    Baca data dari file nilai_contoh.txt

    Jika data tidak ditemukan:
        Tampilkan pesan
    Jika tidak:
        Validasi setiap data siswa
        Simpan data yang valid

    Jika tidak ada data valid:
        Tampilkan pesan bahwa data kosong
    Jika ada data valid:
        Hitung rata-rata nilai
        Cari nilai tertinggi
        Cari nilai terendah
        Hitung jumlah siswa tuntas
        Hitung jumlah siswa belum tuntas

        Tampilkan hasil analisis
        Simpan hasil analisis ke laporan_nilai.txt

SELESAI

## 7. Struktur Program dan Modularisasi

Program dibagi menjadi beberapa file Python agar setiap bagian memiliki tugas yang jelas.

### 1. main.py
Berfungsi sebagai program utama yang mengatur jalannya program, mulai dari membaca data, menampilkan hasil analisis, hingga menyimpan laporan.

Fungsi:
- tampilkan_hasil()
- main()

### 2. data_io.py
Berfungsi membaca data siswa dari file teks dan memeriksa validitas data.

Fungsi:
- baca_data()

### 3. analisis.py
Berfungsi melakukan perhitungan dan menyimpan hasil analisis.

Fungsi:
- hitung_rata_rata()
- cari_nilai_tertinggi()
- cari_nilai_terendah()
- hitung_ketuntasan()
- simpan_laporan()

### 4. utilitas.py
Berfungsi menyediakan fungsi pendukung untuk validasi nilai dan menentukan status ketuntasan.

Fungsi:
- validasi_nilai()
- tentukan_status()

## 8. Struktur Data

Struktur data yang digunakan adalah:

1. List: untuk menyimpan kumpulan data siswa.
2. Dictionary: untuk menyimpan informasi setiap siswa, seperti nama dan nilai.

Struktur tersebut dipilih karena mudah digunakan untuk mengelola dan mengolah sekumpulan data siswa.

## 9. Rancangan Test Case

| No. | Skenario Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Memasukkan nilai 85 | Data diterima dan status tuntas |
| 2 | Memasukkan nilai 75 | Data diterima dan status tuntas |
| 3 | Memasukkan nilai 60 | Data diterima dan status belum tuntas |
| 4 | Memasukkan nilai 105 | Data ditolak karena melebihi batas |
| 5 | Memasukkan nilai -5 | Data ditolak karena kurang dari 0 |
| 6 | Memasukkan beberapa data siswa | Program menampilkan hasil analisis kelas dengan benar |

## 10. Pembagian Tugas

Pembagian tugas disesuaikan dengan jumlah anggota kelompok.

| Peran | Tanggung Jawab |
|---|---|
| Koordinator | Mengatur proses pengerjaan proyek |
| Programmer | Mengembangkan fungsi dan logika program |
| Penguji | Melakukan pengujian dan memeriksa kesalahan |
| Dokumentasi | Menyusun proposal dan dokumentasi proyek |

Apabila jumlah anggota terbatas, beberapa tanggung jawab dapat dirangkap dengan tetap menetapkan penanggung jawab setiap tugas.

## 11. Jadwal Pengerjaan

| Tahap | Kegiatan |
|---|---|
| Pertemuan 14 | Perancangan proyek, IPO, pseudocode, test case, dan dokumentasi awal |
| Antara P14–P15 | Persiapan implementasi fitur utama |
| Pertemuan 15 | Implementasi, pengujian, debugging, dan dokumentasi |
| Pertemuan 16 | Presentasi dan demonstrasi proyek sesuai arahan perkuliahan |

## 12. Repository GitHub

Repository proyek:

URL: https://github.com/firgierviansyah/pertemuan-14-proyek-akhir-FirgiErviansyah-tim-07.git

Repository digunakan untuk menyimpan dokumen rancangan dan perkembangan proyek.

---

## Kesimpulan

Program Pengolah dan Analisis Nilai Siswa dirancang sebagai program sederhana yang membantu proses pengolahan nilai menggunakan konsep dasar matematika dan pemrograman Python. Melalui proyek ini, diharapkan proses pengolahan data dapat dilakukan secara lebih terstruktur, mudah dipahami, dan bermanfaat dalam kegiatan pembelajaran.