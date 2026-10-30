# Program Pengolah dan Analisis Nilai Siswa

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan bahwa rancangan program dapat menerima data siswa, memvalidasi nilai, menghitung statistik, dan menentukan status ketuntasan dengan benar.

## 2. Ketentuan Pengujian

- Rentang nilai yang diterima adalah 0–100.
- Batas ketuntasan awal adalah 75.
- Nilai yang sama dengan atau lebih besar dari 75 dinyatakan tuntas.
- Nilai di bawah 75 dinyatakan belum tuntas.

## 3. Skenario Pengujian

| No. | Data atau Kondisi | Hasil yang Diharapkan |
| --- | --- | --- |
| 1 | Nilai siswa 85 | Data diterima, status tuntas |
| 2 | Nilai siswa 75 | Data diterima, status tuntas |
| 3 | Nilai siswa 60 | Data diterima, status belum tuntas |
| 4 | Nilai siswa 105 | Data ditolak karena melebihi batas |
| 5 | Nilai siswa -5 | Data ditolak karena kurang dari batas |
| 6 | Nilai siswa 0 | Data diterima, status belum tuntas |
| 7 | Nilai siswa 100 | Data diterima, status tuntas |
| 8 | Data beberapa siswa: 80, 70, dan 90 | Rata-rata 80, nilai tertinggi 90, nilai terendah 70 |
| 9 | Tidak ada data siswa | Program menampilkan pemberitahuan bahwa data belum tersedia |

## 4. Kesimpulan Pengujian

Skenario pengujian tersebut digunakan sebagai dasar untuk memeriksa fungsi program pada tahap implementasi. Pengujian mencakup nilai normal, nilai batas, nilai tidak valid, serta pengolahan beberapa data siswa.

Program diharapkan dapat menghasilkan keluaran yang sesuai dengan setiap skenario pengujian.