# Psikolojik Olcek Puani Hesaplayicisi - Hata Avi Surumu

# Kullanicidan isim bilgisi alinir.
isim = input("Katilimcinin adini girin: ")

# Olcekteki soru sayisi belirlenir.
soru_sayisi = 5

# Puanlari saklamak icin liste olusturulur.
puanlar = []

# Bes sorunun puanlari kullanicidan alinir.
for i in range(soru_sayisi):
    puan = float(input(f"{i+1}. soru puani (1-5): "))
    puanlar.append(puan)

# Toplam ve ortalama hesaplanir.
toplam = sum(puanlar)
ortalama = toplam / soru_sayisi

# Puanlarin gecerli olup olmadigi kontrol edilir.
gecerli = all(1 <= puan <= 5 for puan in puanlar)

# Sonuclar ekrana yazdirilir.
print(f"\nKatilimci: {isim}")
print(f"Toplam puan: {toplam:.2f}")
print(f"Ortalama puan: {ortalama:.2f}")
print(f"Puanlar gecerli mi?: {gecerli}")

if not gecerli:
    print("Uyari: Puanlar 1 ile 5 arasinda olmalidir.")
