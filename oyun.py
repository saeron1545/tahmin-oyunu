import random

def tahmin_et():
    sayi = random.randint(1, 100)
    tahmin_hakki = 5
    
    print("1 ile 100 arasında bir sayıyı tahmin et!")
    print("Toplam 5 tahmin hakkın var.")

    while tahmin_hakki > 0:
        tahmin = int(input("Tahmininizi girin: "))
        
        if tahmin < sayi:
            print("Daha yüksek bir sayı girin.")
        elif tahmin > sayi:
            print("Daha düşük bir sayı girin.")
        else:
            print("Tebrikler! Doğru tahmin ettiniz.")
            break
        
        tahmin_hakki -= 1
        print("Kalan tahmin hakkı:", tahmin_hakki)

    if tahmin_hakki == 0:
        print("Tahmin hakkın bitti. Doğru cevap:", sayi)

tahmin_et()
