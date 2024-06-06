#Projek Formulir

#Ini Bagian Input
nama_lengkap = str(input("Masukkan Nama Lengkap : "))
tahun_lahir = int(input("Masukkan Tahun Lahir : "))
tempat_lahir = str(input("Masukkan Tempat Lahir : "))

#Ini Bagian Output
jumlah_lahir = 2024 - tahun_lahir
print("Identitas diri")
print("nama : ", nama_lengkap)
print("umur : ", jumlah_lahir)
print("Lahir di : ", tempat_lahir)