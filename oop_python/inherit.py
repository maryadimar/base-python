#inherit
class Bapak:

	def __init__(self, nama, tinggi, berat):
		self.nama   = nama
		self.tinggi = tinggi
		self.berat  = berat
	#membuat fungsi untuk kelas bapak
	def berjalan(self):
		print("Berjalan kedepan")

	def berlari(selft):
		print("berlari ke tepian")


#membuat kelas anak
class Anak(Bapak):
	def kelakuananak(self):
		print("Nangis minta jajan")

b = Bapak("andi (Bpk)", 170, 60)
print("Nama   :", b.nama)		
print("Tinggi :", b.tinggi, "cm")		
print("Berat  :", b.berat, "kg")
b.berjalan()
b.berlari()
print()
#membuat objek anak ,namun bisa mengakses keseluruhan yang dimiliki bapak
#mulai dari nama sampai fungsi berlari merupakan attribut/fungsi yang dimiliki Bpk
a = Anak("damar (Anak)", 160, 50)
print("Nama   :", a.nama)		
print("Tinggi :", a.tinggi, "cm")		
print("Berat  :", a.berat, "kg")
a.berjalan()		
a.berlari()
a.kelakuananak()
