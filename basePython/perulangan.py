"""
Perulangan

Secara umum, Python mengeksekusi program baris perbaris. Mulai dari baris satu, dua, dan seterusnya. Ada kalanya, kita perlu mengeksekusi satu baris atau satu blok kode program beberapa kali. Hal ini disebut dengan perulangan atau biasa disebut looping atau iterasi. Untuk lebih jelasnya perhatikan gambar berikut:
"""

"""
Perulangan dengan menggunakan for memiliki sintaks seperti berikut:
for var in sequence:
    body of for
"""

"""
var adalah variabel yang digunakan untuk penampung sementara nilai dari sequence pada saat terjadi perulangan. Sequence adalah tipe data berurut seperti string, list, dan tuple.

Perulangan terjadi sampai looping mencapai elemen atau anggota terakhir dari sequence. Bila loop sudah sampai ke elemen terakhir dari sequence, maka program akan keluar dari looping.
"""
print("sum pada loop")
print("==============")
nomer = [2,3,4,6,7,8]

sum = 0

for each in nomer:
	sum = sum + each

print("Total : ", sum)

print("================")
print("looping isi list")
print("================")
# looping isi list
lists = [2,5,4,4]

for cetak in lists:
	print(cetak)
print("=====================")
print("looping dengan range")
print("=====================")

x = [1,2,3,4,5,6,7,8,9,10,11]

for x in range(1,10):
	print(x)
print("======================")

"""
Fungsi range()

Fungsi range() dapat digunakan untuk menghasilkan deret bilangan. range(10) akan menghasilkan bilangan dari 0 sampai dengan 9 (10 bilangan).

Kita juga bisa menentukan batas bawah, batas atas, dan interval dengan format range(batas bawah, batas atas, interval).Bila interval dikosongkan, maka nilai default 1 yang akan digunakan.

Fungsi range tidak menyimpan semua nilai dalam memori secara langsung. Ia hanya akan mengingat batas bawah, batas atas, dan interval dan membangkitkan hasilnya satu persatu hanya bila dipanggil. Untuk membuat fungsi ini langsung menampilkan semua item, kita bisa menggunakan fungsi list(). Untuk jelasnya perhatikan contoh berikut:
"""
print("fungsi range")
print("======================")
#output range(0,10)
print(range(10),"\n")
#range dengan list
#output [0,1,2,3,4,5,6,7,8,9]
print(list(range(10)), "\n")
#cetak value tertentu dengan batasan
#output [2,3,4,5,6,7]
print(list(range(2,8)), "\n")
print(list(range(2,20,3)))
print("======================")
"""
Kita bisa menggunakan fungsi range() dalam perulangan menggunakan for untuk iterasi bilangan berurut. Hal ini dengan cara mengkombinasikan fungsi range() dengan fungsi len() . Fungsi len() berfungsi untuk mendapatkan panjang atau jumlah elemen suatu data sekuensial atau berurut.
"""
sebutkan_5_nama_ikan = ["lele", "indosiar", "tongkol", "capung", "kintel"]

#looping dengan index

for index in range(len(sebutkan_5_nama_ikan)):
	print("nama ikan nya :", sebutkan_5_nama_ikan[index])
print("======================")
"""
Perulangan Menggunakan while

Perulangan menggunakan while akan menjalankan blok pernyataan terus menerus selama kondisi bernilai benar.

Adapun sintaks dari perulangan menggunakan while adalah:
while expression:
    statement (s)
Di sini, statement (s) bisa terdiri dari satu baris atau satu blok pernyataan. Expression merupakan ekspresi atau kondisi apa saja, dan untuk nilai selain nol dianggap True. Iterasi akan terus berlanjut selama kondisi benar. Bila kondisi salah, maka program akan keluar dari while dan lanjut ke baris pernyataan di luar while.
"""
print("Looping dengan while")
print("======================")
hitung = 0
while(hitung < 5):
	print('mari berhitung :', hitung)
	hitung = hitung + 1
print("selamat jalan")
print("======================")

"""
Infinite Loop

Sebuah kondisi dimana loop selalu benar dan tidak pernah salah disebut loop tidak terbatas (infinite loop). Terkadang hal ini menjadi masalah. Tapi sering juga infinite loop berguna, misalnya untuk program client/server dimana server perlu menjaga komunikasi tetap hidup dan tidak terputus.

Pada contoh program while di atas, bila kita lupa menuliskan kode count = count + 1, maka akan jadi infinite 
"""
"""
Kendali Looping

Looping umumnya akan berhenti bila kondisi sudah bernilai salah. Akan tetapi, seringkali kita perlu keluar dari looping di tengah jalan tergantung keperluan. Hal ini bisa kita lakukan dengan menggunakan kata kunci break dan continue.

Statement break memaksa program keluar dari blok looping di tengah jalan. Sedangkan statement continue menyebabkan program langsung melanjut ke step / interval berikutnya dan mengabaikan (skip) baris kode di bawahnya (yang satu blok). Jelasnya perhatikan contoh berikut:
"""
#tanpa break
print("Memanfaatkan break")
print("======================")
for var in "sakulaku":
	# if var == "u":
	# 	break
	print("huruf sekarang :", var)
print("======================")
#denga break
for x in "saku":
	if x == "u":
		break #coba ganti dg continue
	print("huruf sekarang :", x)
print("selamat jalan..")
print("======================")
"""
while else

Python mendukung penggunaan else sebagai pasangan dari while. Blok pernyataan else hanya akan dieksekusi bila kondisi while bernilai salah.
"""
print("while else")
print("======================")
angka = 0
while (angka < 5):
	print(angka, "kurang dari 5")
	angka = angka + 1
else:
	print(angka, "tidak kurang dari 5")
print("======================")

	