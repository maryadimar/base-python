def faktor(x):
	 print("fakotr dari ", x , "adalah")
	 for i in range(1, x+1):
	 	if x % i == 0:
		 	print(i)

num = int(input("masukan bilangan :"))

faktor(num)

		