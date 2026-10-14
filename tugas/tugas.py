# ==========================================
# 1. CLASS KARYAWAN (SUPERCLASS)
# ==========================================
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok

    def get_gaji_pokok(self):
        return self.__gaji_pokok

    def set_gaji_pokok(self, gaji_baru):
        if gaji_baru <= 0:
            print(f"[PERINGATAN] Gaji pokok tidak boleh <= 0! Nilai {gaji_baru} ditolak.")
        else:
            self.__gaji_pokok = gaji_baru
            print(f"[INFO] Gaji pokok {self.nama} berhasil diubah menjadi Rp {gaji_baru:,.0f}.")

    def hitung_gaji_total(self):
        return self.__gaji_pokok

    def tampilkan_info(self):
        print(f"Nama        : {self.nama}")
        print(f"ID Karyawan : {self.id_karyawan}")
        print(f"Gaji Pokok  : Rp {self.get_gaji_pokok():,.0f}")


# ==========================================
# 2. CLASS KARYAWAN TETAP (CHILD CLASS)
# ==========================================
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.tunjangan

    def tampilkan_info(self):
        print("====== DETAIL KARYAWAN TETAP ======")
        print(f"Nama        : {self.nama}")
        print(f"ID Karyawan : {self.id_karyawan}")
        print(f"Gaji Pokok  : Rp {self.get_gaji_pokok():,.0f}")
        print(f"Tunjangan   : Rp {self.tunjangan:,.0f}")
        print(f"Total Gaji  : Rp {self.hitung_gaji_total():,.0f}")
        print("===================================")


# ==========================================
# 3. CLASS KARYAWAN KONTRAK (CHILD CLASS)
# ==========================================
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, jam_lembur, tarif_lembur):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + (self.jam_lembur * self.tarif_lembur)

    def tampilkan_info(self):
        print("====== DETAIL KARYAWAN KONTRAK ======")
        print(f"Nama         : {self.nama}")
        print(f"ID Karyawan  : {self.id_karyawan}")
        print(f"Gaji Pokok   : Rp {self.get_gaji_pokok():,.0f}")
        print(f"Jam Lembur   : {self.jam_lembur} jam")
        print(f"Tarif Lembur : Rp {self.tarif_lembur:,.0f} / jam")
        print(f"Total Gaji   : Rp {self.hitung_gaji_total():,.0f}")
        print("=====================================")


# ==========================================
# 4. MAIN PROGRAM
# ==========================================
print("========== DEMONSTRASI POLYMORPHISM ==========")

karyawan1 = KaryawanTetap("Budi Santoso", "KT-001", 5000000, 1500000)
karyawan2 = KaryawanKontrak("Siti Aminah", "KK-002", 3000000, 20, 50000)

daftar_karyawan = [karyawan1, karyawan2]

for karyawan in daftar_karyawan:
    karyawan.tampilkan_info()
    print()

print("========== DEMONSTRASI ENCAPSULATION ==========")
print(">> Set gaji pokok TIDAK VALID (-1000):")
karyawan1.set_gaji_pokok(-1000)

print("\n>> Set gaji pokok VALID (6000000):")
karyawan1.set_gaji_pokok(6000000)

print("\n>> Tampilkan ulang info Budi:")
karyawan1.tampilkan_info()