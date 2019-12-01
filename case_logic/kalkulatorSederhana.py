#membuat fungsi untuk setiap operator nya
def penjumlahan(x,y):
	return x+y

def pengurangan(x,y):
	return x-y

def perkalian(x,y):
	return x*y

def pembagian(x,y):
	return x/y

print("===================================")
print("====== APLIKASI KALKULATOR ========")
print("===================================")
print("== Silahkan Pilih Operator nya : ==")
print("Penjumlahan [1]")
print("Pengurangan [2]")
print("Perkalian   [3]")
print("Pembagian   [4]")

pilihan = input("Pilih Operator [1/2/3/4]")

input1  = int(input("masukan angka pertama :"))
input2  = int(input("masukan angka kedua   :"))

if pilihan == '1':
	print(input1, "+", input2 ,"=", penjumlahan(input1,input2))

elif pilihan == '2':
	print(input1, "-", input2, "=", pengurangan(input1,input2))

elif pilihan == '3':
	print(input1, "x", input2, "=", perkalian(input1,input2))

elif pilihan == '4':
	print(input1, ":", input2, "=", pembagian(input1,input2))

else:
	print("operator tidak di eksekusi")


