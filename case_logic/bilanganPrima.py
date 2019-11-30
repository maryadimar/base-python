def is_prime(x):
    prime = "Bilangan Prima"
    # Mengecek jika x < 2 maka bukan bilangan prima
    if x < 2:
        prime = "Bukan bilangan prima"
    # Mengecek jika x = 2 maka bilangan prima
    if x == 2:
        prime = "Bilangan Prima"
    # Memoduluskan x dengan semua bilangan yang lebih kecil dari x
    for i in range(2, x):
        # Jika menghasilkan 0 maka bukan bilangan prima
        if x % i == 0:
            prime = "Bukan bilangan prima"
            break
    return prime


bilangan = int(input("Masukkan Bilangan : "))
print(is_prime(bilangan))