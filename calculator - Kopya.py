print("""
[1] addition
[2] exraction
[3] Divide
[4] exit

""")

giriş = input("Seçiminzi: ")

if giriş == "1":
	x = input("ilk sayı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)
	
	print("işlem sonucu: ",x + y)
if giris == "2":
	x = input("ilk saı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)
	
	print("işlem sonucu: ",x - y)
if giris == "3":
	x = input("ilk saı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)
	
	print("işlem sonucu: ",x / y)

if giris == "4":
	print("çıkılıyor...")
	quit()

