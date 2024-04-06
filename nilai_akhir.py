print("\t\tAplikasi Mengitung Nilai Akhir")
print("\t\t\tSMK Putra Bangsa")
print("==========================================================")
Nama=(input("Nama Siswa\t\t\t:"))
Nilai1=float(input("Input Nilai Keaktifan\t\t:"))
Nilai2=float(input("Input Nilai Tugas\t\t:"))
Nilai3=float(input("Input Nilai Ujian\t\t:"))
nk=Nilai1*0.2
nt=Nilai2*0.3
nu=Nilai3*0.5
nj=nk+nt+nu
if nj > 80:
    jr= ("A")
elif nj > 70:
    jr= ("B")
elif nj > 56:
    jr= ("C")
elif nj > 46:
    jr= ("D")
else: jr= ("E")
print("==========================================================")
print("Memperoleh nilai prestasi sebagai berikut:\n")
print("Nama Siswa\t\t\t:" ,Nama)
print("Nilai Keaktifan x 20%\t\t:",nk)
print("Nilai Tugas x 30%\t\t:",nt)
print("Nilai Ujian x 50%\t\t:",nu)
print("Total Nilai\t\t\t:",nj)
print("Dengan Grade\t\t\t:",jr)
print("==========================================================")
