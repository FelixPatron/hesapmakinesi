while True:
    print('    HESAP MAK�NES�  Toplama(1) ��karma(2) �arpma(3) B�lme(4)')
    print('-------------------')
    islem = input("��lem Se�iniz: ")


    if (islem == 1):
        sayi1 = input("Say� Giriniz: ")
        sayi2 = input("�kinci Say�y� Giriniz: ")
        sonuc=sayi1+sayi2
        print(sonuc)
    elif (islem == 2):
        sayi1 = input("Say� Giriniz: ")
        sayi2 = input("�kinci Say�y� Giriniz: ")
        sonuc=sayi1-sayi2
        print(sonuc)
    elif (islem == 3):
        sayi1 = input("Say� Giriniz: ")
        sayi2 = input("�kinci Say�y� Giriniz: ")
        sonuc=sayi1*sayi2
        print(sonuc)
    elif (islem == 4):
        sayi1 = input("Say� Giriniz: ")
        sayi2 = input("�kinci Say�y� Giriniz: ")
        sonuc=sayi1/sayi2
        print(sonuc)
