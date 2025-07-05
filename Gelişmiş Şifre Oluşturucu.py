
"""
Geliştirilmiş ve Türkçeleştirilmiş Şifre Oluşturucu
"""

import random
import string
import math
import datetime
import os

print("16 sayısının karekökü:", math.sqrt(16))
print("1 ile 10 arasında rastgele sayı:", random.randint(1, 10))
print("Rastgele meyve seçimi:", random.choices(["Elma", "Muz", "Kiraz"]))
print("Rastgele sayı (farklı yöntemle):", random.randint(1, 10))


sade_sifre = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
print("Basit Rastgele Şifre:", sade_sifre)


def sifre_uret(uzunluk=12):
    if uzunluk < 4:
        raise ValueError("Şifre uzunluğu en az 4 karakter olmalıdır.")

    # Şifre karakter setleri
    buyuk_harfler = string.ascii_uppercase
    kucuk_harfler = string.ascii_lowercase
    rakamlar = string.digits
    ozel_karakterler = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    
    sifre = [
        random.choice(buyuk_harfler),
        random.choice(kucuk_harfler),
        random.choice(rakamlar),
        random.choice(ozel_karakterler)
    ]

  
    tum_karakterler = buyuk_harfler + kucuk_harfler + rakamlar + ozel_karakterler
    sifre += random.choices(tum_karakterler, k=uzunluk - 4)

  
    random.shuffle(sifre)

    return ''.join(sifre)


try:
    uzunluk = int(input("İstediğiniz şifre uzunluğunu girin (en az 4): "))
    uretilen_sifre = sifre_uret(uzunluk)
    print("Oluşturulan Güçlü Şifre:", uretilen_sifre)
except ValueError as hata:
    print("Hata:", hata)
