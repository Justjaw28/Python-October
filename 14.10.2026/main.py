print ("Vítejte u nás v  Divadla!")
print ("Kolik vás je?")
osoby = int(input())
if osoby >= 4:
    print ("Budete platit skupinovou cenu s slevou 30%.")
    print ("Cena ja" , osoby * 500  * 0.75 , "Kč")
else:
    print ("Kolik vám je let?")
    let = int(input())
    if osoby > 1:
        print (osoby , "osoby ve věku" , let , "let.")
        if let < 26:
            print ("Jste student? [a/n]")
            student = input()
            if student == "a":
                print ("Cena je" , osoby * 500 * 0.7, "Kč")
            else:
                print ("Zaplatíte celou cenu. Cena je" , osoby * 500 , "Kč")
        elif let >= 26 and let < 65:
            print ("Cena je" , osoby * 500 , "Kč")
        else:
            print ("Cena je" , osoby * 500 * 0.8, "Kč")
    else:
        print (osoby , "osoba ve věku" , let , "let.")
        if let < 26:
            print ("Jste student? [a/n]")
            student = input()
            if student == "a":
                print ("Cena je" , osoby * 500 * 0.7, "Kč")
            else:
                print ("Zaplatíte celou cenu. Cena je" , osoby * 500 , "Kč")
        elif let >= 26 and let < 65:
            print ("Cena je" , osoby * 500 , "Kč")
        else:
            print ("Cena je" , osoby * 500 * 0.8, "Kč")