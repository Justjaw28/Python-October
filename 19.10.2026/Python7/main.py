print ("Vyberte 3 náhodná čísla:")
cislo1 = int(input())
cislo2 = int(input())
cislo3 = int(input())

if cislo1 > cislo2:
    p = cislo1
    cislo1 = cislo2
    cislo2 = p
if cislo2 > cislo3:
    p = cislo2
    cislo2 = cislo3
    cislo3 = p
if cislo1 > cislo2:
    p = cislo1
    cislo1 = cislo2
    cislo2 = p

print ( cislo1, cislo2, cislo3)