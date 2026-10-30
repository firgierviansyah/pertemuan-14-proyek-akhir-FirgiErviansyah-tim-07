
def validasi_nilai(nilai):
    """
    Memeriksa apakah nilai berada pada rentang 0 sampai 100.
    """
    try:
        nilai = float(nilai)

        if 0 <= nilai <= 100:
            return True
        else:
            return False

    except (ValueError, TypeError):
        return False


def tentukan_status(nilai, batas=75):
    """
    Menentukan status ketuntasan siswa.
    """
    if nilai >= batas:
        return "Tuntas"
    else:
        return "Belum Tuntas"
