while True:
    print('    HESAP MAKÝNESÝ  Toplama(1) Çýkarma(2) Çarpma(3) Bölme(4)')
    print('-------------------')
    islem = input("Ýþlem Seçiniz: ")


    if (islem == 1):
        sayi1 = input("Sayý Giriniz: ")
        sayi2 = input("Ýkinci Sayýyý Giriniz: ")
        sonuc=sayi1+sayi2
        print(sonuc)
    elif (islem == 2):
        sayi1 = input("Sayý Giriniz: ")
        sayi2 = input("Ýkinci Sayýyý Giriniz: ")
        sonuc=sayi1-sayi2
        print(sonuc)
    elif (islem == 3):
        sayi1 = input("Sayý Giriniz: ")
        sayi2 = input("Ýkinci Sayýyý Giriniz: ")
        sonuc=sayi1*sayi2
        print(sonuc)
    elif (islem == 4):
        sayi1 = input("Sayý Giriniz: ")
        sayi2 = input("Ýkinci Sayýyý Giriniz: ")
        sonuc=sayi1/sayi2
        print(sonuc)
