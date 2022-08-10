import random

while True:
    kullanici_secimi = input("Seçiminizi girin (taş, kağıt, makas): ")
    olasi_secimler = ["taş", "kağıt", "makas"]
    pc_secimi = random.choice(olasi_secimler)
    print(f"\n Senin seçimin {kullanici_secimi}, yapay zekanın seçimi {pc_secimi} oldu.\n")

    if kullanici_secimi == pc_secimi:
        print(f"İkiniz de {kullanici_secimi} seçtiniz. Berabere!")
    elif kullanici_secimi == "taş":
        if pc_secimi == "makas":
            print("Taş makası kırdı! Sen kazandın!")
        else:
            print("Kağıt taşı kapladı! Kaybettin.")
    elif kullanici_secimi == "kağıt":
        if pc_secimi == "taş":
            print("Kağıt taşı kapladı! Kazandın!")
        else:
            print("Makas kağıdı kesti! Kaybettin.")
    elif kullanici_secimi == "makas":
        if pc_secimi == "kağıt":
            print("Makas kağıdı kesti! Kazandın!")
        else:
            print("Taş makası kırdı! Kaybettin.")

    yeniden_oyna = input("Tekrar oynamak ister misiniz? (e/h): ")
    if yeniden_oyna.lower() != "e":
        break
