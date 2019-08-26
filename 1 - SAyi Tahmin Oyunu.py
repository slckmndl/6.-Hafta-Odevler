print("""
      =============================================="
      |                                            |
      |                SELCUK DAL                  |
      |             SAYI TAHMIN OYUNU              |
      |                  V 2.3                     |
      |               HOSGELDINIZ                  |
      |                                            |
      ==============================================""")

print("""
OYUN YONERGESI

Sayi tahmin oyunumuza hos geldiniz. 
Lutfen aklinizdan 1 - 100 arasi bir sayi tutunuz.
Programimiz aklinizda tuttugunuz sayiyi bulmaya calisacaktir.
Programimizin yaptigi tahmin aklinizdaki sayidan buyukse    -
Programimizin yaptigi tahmin aklinizdaki sayidan kucukse    + 
Programimizin yaptigi tahmin aklinizdaki sayi ise           D 
tusuna basiniz.
""")

baslama=input("Hazirsaniz H tusuna basin ve heyecan baslasin. Oyundan cikmak istiyorsaniz Q tusuna basin, severek ayrilalim : ")

if baslama == "Q":
    print("Oyunda Cikiliyor...Gule Gule")
    quit()

if baslama == "H":
    altsinir=0
    ustsinir=101
    import random
    tahmin=random.randint(altsinir, ustsinir)
    print("1. tahmin : ", tahmin)
    deneme=1
    while True:
        deneme+=1
        degerlendirme=input("Yukaridaki yonergeye gore degerlendirmenizi yapiniz !  ")
        if degerlendirme == "-":
            ustsinir=tahmin
            tahmin=int((ustsinir+altsinir)/2)
            print(deneme,".", "tahmin :", tahmin)
        elif degerlendirme == "+":
            altsinir=tahmin
            tahmin=int((ustsinir+altsinir)/2)
            print(deneme,".", "tahmin :", tahmin)
        elif degerlendirme == "D":
            print("Tebrikler.{}. denemede bildiniz.".format(deneme))
            break
