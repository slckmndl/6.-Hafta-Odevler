import random

print("""
      =============================================="
      |                                            |
      |                                            |
      |             SAYI TAHMIN OYUNU              |
      |                  V 2.3                     |
      |               HOSGELDINIZ                  |
      |                                            |
      ==============================================\n\n""")

sayi_listesi = list(range(101))

tahmin = input(""" 
Aklinizdan 1-100 arasinda bir sayi tutunuz !" Tahmin etmeye calisacagiz..

Hazirsaniz ENTER a basiniz ! (Cikmak icin Q ya basiniz ! ) : """)

print("\n\n")


while True:

    if tahmin=="q":
        break

    if tahmin=="":

        print("Tuttugunuz Sayi : ")

        pc_tahmin = random.choice(sayi_listesi)

        print(pc_tahmin)


        feedback = input("""
Tuttugunuz sayi ile tahmin edilen sayi dogru ise "dogru" yaziniz !        

Eger tuttugunuz sayi tahmin edilen sayidan kucukse "-" ve buyukse "+" 

isareti koyunuz ve ENTER a basiniz! = """)


        if feedback=="dogru":
            print("Nasilda Bildik ! ")
            break


        if feedback=="-":
            print("Yeni Tahmin : ")
            a = random.randrange(0,pc_tahmin)
            print(a)


        if feedback=="+":
            print("Yeni Tahmin : ")
            b = random.randrange(pc_tahmin,101)
            print(b)





