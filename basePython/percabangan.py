"""
Percabangan adalah cara yang digunakan untuk mengambil keputusan apabila di dalam program dihadapkan pada kondisi tertentu. Jumlah kondisinya bisa satu, dua atau lebih.

Percabangan mengevaluasi kondisi atau ekspresi yang hasilnya benar atau salah .  Kondisi atau ekspresi tersebut disebut ekspresi boolean. Hasil dari pengecekan kondisi adalah True atau False. Bila benar (True), maka pernyataan yang ada di dalam blok kondisi tersebut akan dieksekusi. Bila salah (False), maka blok pernyataan lain yang dieksekusi.
"""

"""
Pernyataan if

Pernyataan if menguji satu buah kondisi. Bila hasilnya benar maka pernyataan di dalam blok if tersebut dieksekusi. Bila salah, maka pernyataan tidak dieksekusi. Sintaksnya adalah seperti berikut
"""

"""
if tes kondisi:
   blok pernyataan if
"""
print("========================")
print("kondisi if")
print("-----------------")
angka = 5
if angka > 0:
	print (angka, "adalah bilangan positif")

angka = -1
if angka > 0:
	print(angka, "adalah bilangan positif")

"""
Pada contoh di atas, awalnya angka berisi 5. Pada saat if yang pertama dieksekusi maka kondisinya adalah apakah 5 > 0? Karena hasilnya benar/True, maka statement di grup if ini dieksekusi dan menampilkan pesan 5 adalah bilangan positif.

Selanjutnya angka sudah diubah jadi -1. Untuk if yang kedua, hasil pengujian kondisinya menjadi apakah -1 > 0? Hasilnya salah/False. Oleh karena itu, pernyataan di dalam grupnya tidak dijalankan.
"""

#selanjutnya kondisi if else
"""
Pernyataan if…else

Pernyataan if…else menguji 2 kondisi. Kondisi pertama kalau benar, dan kondisi kedua kalau salah. Sintaksnya adalah seperti berikut:
"""
"""
if tes kondisi:
    blok pernyataan if
else:
    blok pernyataan else
"""
print("========================")
print("kondisi if - else")
print("------------------")
bilangan = 2

# coba juga mengubah bilangan menjadi bilangan = -1
# dan perhatikan hasilnya 
if bilangan >= 0:
	print(bilangan, "bilangan positif")
else:
	print(bilangan, "bilangan negatif")

"""
Pernyataan if…elif…else…

Pernyataan if…elif…else digunakan untuk menguji lebih dari 2 kondisi. Bila kondisi pada if benar, maka pernyataan di dalamnya yang dieksekusi. Bila salah, maka masuk ke pengujian kondisi elif. Terakhir bila tidak ada if atau elif yang benar, maka yang dijalankan adalah yang di blok else. Sintaksnya adalah seperti berikut:
"""
"""
if tes kondisi:
    blok pernyataan if
elif tes kondisi:
    blok pernyataan elif
else:
    blok pernyataan else
"""
print("========================")
print("kondisi if…elif…else")
bilangan_ = -3

if bilangan_ > 0:
	print(bilangan_, "bilangan positif")
elif bilangan_ == 0:
	print(bilangan_, "nol")
else:
	print(bilangan_, "bilangan negatif")
	print("-------------------------")
