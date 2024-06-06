tinggi_badan = float(input("Masukkan tinggi badan : "))
berat_badan = float(input("Masukkan berat badan : "))

bmi = berat_badan / (tinggi_badan **2)

if bmi < 18.5:
 print("kurang")

elif bmi > 24.9:
 print("obesitas")

else:
  print("ideal")