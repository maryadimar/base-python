class Hero:	
	"""
	Untuk penanganan enkapsulasi dengan cara python maka bisa menggunakan decorator. Adapun decorator yang digunakan property, getter, setter dan deleter. Berikut ini contoh kode penggunaan decorator property, getter, setter
	"""
	def __init__(self, nama, jenis, kuat):
		self.__nama  = nama
		self.__jenis = jenis
		self.__kuat  = kuat

	@property
	def info(self):
		return (self.__nama+ "-" + self.__jenis+ "-" + str(self.__kuat))

	@property
	def nama(self):
		pass

	@nama.getter
	def nama(self):
		return self.__nama

	@nama.setter
	def nama(self, input):
		self.__nama = input

	@property
	def jenis(self):
		pass

	@jenis.getter
	def jenis(self):
		return self.__jenis

	@jenis.setter
	def jenis(self, input):
		self.__jenis = input

	@property
	def kuat(self):
		pass

	@kuat.getter
	def kuat(self):
		return self.__kuat

	@kuat.setter
	def kuat(self, input):
		self.__kuat = input

semar = Hero("semar", "Penyihir", 100)
print(semar)
semar.nama = "Semar mesem"
semar.jenis = "Jawara"
semar.kuat = 140
print(semar.info)
		