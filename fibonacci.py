print("""---Fibonacci Programı---
Lütfen Seçim Yapınız;
1 - Fibonacci serisi
2 - Fibonacci deger bulma
3 - Fibonacci toplama""")

secim=input("Deger giriniz: ")


def Fibotoplam(t_Deger):
    if t_Deger == 0:
        return 0
    if t_Deger == 1:
        return 1
    else:
        return Fibotoplam(t_Deger-1) + Fibotoplam(t_Deger-2)


if secim==1:
    print("1 seçildi")
elif secim==2:
    print("2 seçildi")
elif secim==3:
    print("3 seçildi")
    t_deger=input("Toplanmasını istenen sırayı girin: ")
    Fibotoplam(t_deger)
else:
    print("Hatalı değer girildi.")
