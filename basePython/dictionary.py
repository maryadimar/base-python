"""
Dictionary

Dictionary adalah tipe data yang tiap anggotanya terdiri dari pasangan kunci-nilai (key-value). Mirip dengan kamus dimana ada kata ada arti. Dictionary umumnya dipakai untuk data yang besar dan untuk mengakses anggota data secara acak. Anggota dictionary tidak memiliki indeks.

Dictionary dideklarasikan dengan menggunakan tanda kurung kurawal { }, dimana anggotanya memiliki bentuk kunci:nilai atau key:value dan tiap anggota dipisah tanda koma. Kunci dan nilainya bisa memiliki tipe sembarang.

Untuk mengakses nilai dari anggota dictionary, kita menggunakan key-nya.
"""
d = {1: "nama", 2:"dua", "tiga":3}
print(d)

print("cetak key tiga : ", d['tiga'])
print("cetak key 1 : ", d[1])

"""
Beberapa Catatan …

    Tipe data sering disebut objek. Pada dasarnya semua hal di python adalah objek.
    Ada tipe data lain yang umumnya dimiliki oleh bahasa Python, yaitu tipe None. Tipe None adalah sebuah tipe data spesial yang menunjukkan bahwa nilai/data suatu variabel itu belum/tidak ada (bukan nol, tapi tidak ada). Pada bahasa pemrograman lain seperti C, atau PHP, tipe data ini disebut null.
    Tipe data string, tuple, dan list masuk ke dalam tipe data yang disebut tipe data berurut / ordered atau sekuensial / sequence. Tipe data dictionary disebut data tidak berurut / unordered.

"""