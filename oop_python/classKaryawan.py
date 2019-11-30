class Karyawan(object):
	
	jumlah_karyawan = 0
	#funsi ini bakal tereksekusi diawal program dijalankan
	def __init__(self, nama, gaji):
		self.nama = nama
		self.gaji = gaji
		Karyawan.jumlah_karyawan += 1

	def tampilkanprofile(self):
		print("Nama :", self.nama)
		print("Gaji :", self.gaji)
		print()

#membuat objek dari kelas karyawan
#karyawan 1
Karyawan1 = Karyawan("Agung", 3000000)
#karyawan 2
Karyawan2 = Karyawan("Maryadi", 4000000)

#akses objek karyawan yang sudah dibuat diatas denagn memanfaatkan fungsi tampilkanprofile
Karyawan1.tampilkanprofile()
Karyawan2.tampilkanprofile()
#tampilkan total karyawan 
print("Jumlah Karyawan :", Karyawan.jumlah_karyawan)


		

		