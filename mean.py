print("\tAplikasi Mengitung Nilai Rata Rata siswa")
print("\t\tSMK Putra Bangsa")
print("==========================================================")
Nama=(input("Nama Siswa\t\t\t:"))
Nilai1=float(input("Input Nilai Perandingan 1\t:"))
Nilai2=float(input("Input Nilai Perandingan 2\t:"))
Nilai3=float(input("Input Nilai Perandingan 3\t:"))
Nr=(Nilai1+Nilai2+Nilai3)/3
if Nr > 80:
    jr= ("Juara I!")
elif Nr > 75:
    jr= ("Juara 2!")
elif Nr > 70:
    jr= ("Juara 3!")
else: jr= ("Tidak Juara")

print("==========================================================")
print("Nama Siswa\t\t\t:" ,Nama)
print("Nilai rata rata\t\t\t:",Nr)
print("menjadi juara ke-\t\t:",jr)
print("dari perlombaan yang diikutinya")
