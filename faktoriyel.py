#Faktöriyel
i=1
sonuc=1
faktoriyel=int(input("Faktoriyeli hesaplanacak sayıyı giriniz: "))
while (i<=faktoriyel):
    sonuc=i*sonuc
    i=i+1
    
print("Sonuc=",sonuc)
