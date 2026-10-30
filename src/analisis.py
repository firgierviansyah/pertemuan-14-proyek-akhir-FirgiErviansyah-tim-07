def hitung_rata_rata(data_siswa):
    """
    Menghitung rata-rata nilai seluruh siswa.
    """
    if not data_siswa:
        return 0

    total = sum(siswa["nilai"] for siswa in data_siswa)

    return total / len(data_siswa)


def cari_nilai_tertinggi(data_siswa):
    """
    Mencari nilai tertinggi siswa.
    """
    if not data_siswa:
        return 0

    return max(siswa["nilai"] for siswa in data_siswa)


def cari_nilai_terendah(data_siswa):
    """
    Mencari nilai terendah siswa.
    """
    if not data_siswa:
        return 0

    return min(siswa["nilai"] for siswa in data_siswa)


def hitung_ketuntasan(data_siswa, batas=75):
    """
    Menghitung jumlah siswa yang tuntas dan belum tuntas.
    """
    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= batas:
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    return jumlah_tuntas, jumlah_belum_tuntas


def simpan_laporan(data_siswa, path, batas=75):
    if not data_siswa:
        print("Tidak ada data untuk disimpan.")
        return

    rata_rata = hitung_rata_rata(data_siswa)
    tertinggi = cari_nilai_tertinggi(data_siswa)
    terendah = cari_nilai_terendah(data_siswa)

    jumlah_tuntas, jumlah_belum_tuntas = (
        hitung_ketuntasan(data_siswa, batas)
    )

    with open(path, "w", encoding="utf-8") as file:
        file.write("========== LAPORAN ANALISIS NILAI ==========\n")
        file.write(f"Batas ketuntasan: {batas}\n\n")

        file.write("DAFTAR NILAI SISWA\n")
        file.write("-" * 45 + "\n")

        for siswa in data_siswa:
            status = (
                "Tuntas"
                if siswa["nilai"] >= batas
                else "Belum Tuntas"
            )

            file.write(
                f"{siswa['nama']:<20} "
                f"{siswa['nilai']:<10.2f} "
                f"{status}\n"
            )

        file.write("\nSTATISTIK KELAS\n")
        file.write(f"Rata-rata nilai : {rata_rata:.2f}\n")
        file.write(f"Nilai tertinggi : {tertinggi:.2f}\n")
        file.write(f"Nilai terendah  : {terendah:.2f}\n")
        file.write(f"Siswa tuntas    : {jumlah_tuntas}\n")
        file.write(f"Belum tuntas    : {jumlah_belum_tuntas}\n")

    print(f"\nLaporan berhasil disimpan ke: {path}")