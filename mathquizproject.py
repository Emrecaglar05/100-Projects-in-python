# -*- coding: utf-8 -*-
"""MathQuizProject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eHav5xVo6IOsYWWxqMgFDRJ1UxrJIwD1
"""

import random
import time

def soru_olustur():
    sayi1 = random.randint(1, 10)
    sayi2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        cevap = sayi1 + sayi2
    elif operator == "-":
        cevap = sayi1 - sayi2
    elif operator == "*":
        cevap = sayi1 * sayi2
    else:
        while sayi2 == 0:
            sayi2 = random.randint(1, 10)
        cevap = round(sayi1 / sayi2, 2)

    return f"{sayi1} {operator} {sayi2}", cevap

def math_quiz():
    score = 0
    rounds = int(input("Kaç soru çözmek istersin? "))

    for i in range(rounds):
        soru, dogru_cevap = soru_olustur()
        print(f"\nSoru {i+1}: {soru}")
        print("⏳ 5 saniyen var, hazır ol!")

        for saniye in range(5, 0, -1):
            print(saniye)
            time.sleep(1)

        kullanıcı_cevap = input("Cevabını gir: ")

        try:
            if "/" in soru:
                kullanıcı_cevap = float(kullanıcı_cevap)
            else:
                kullanıcı_cevap = int(kullanıcı_cevap)

            if kullanıcı_cevap == dogru_cevap:
                print("✅ Doğru cevap!")
                score += 1
            else:
                print(f"❌ Yanlış cevap! Doğru cevap: {dogru_cevap}")
        except:
            print("⚠️ Geçersiz giriş! Sayı girmelisin.")

    print(f"\n🎯 Toplam puan: {score}/{rounds}")
    if score == rounds:
        print("🏆 Tebrikler! Tüm soruları doğru bildiniz.")
    else:
        print("📚 Üzgünüz, daha fazla çalışmalısınız.")

math_quiz()
18



# Fonksyonlar hakkında temeller

def hosgeldin(isim):
  print(f"Hoşgeldin,  {isim}!")

hosgeldin("Emre")