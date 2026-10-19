print ("Napište 3 libovolná čísla:")
cislo1 = int(input())
cislo2 = int(input())
cislo3 = int(input())
print ("Vybrali jste čísla:", cislo1, cislo2, cislo3)

min = cislo1
max = cislo1
if cislo2 < min:
    min = cislo2
elif cislo2 > min:
    max = cislo2

if cislo3 < min:
    min = cislo3
elif cislo3 > max:
    max = cislo3

print ("Číslo" , min , "je minimum \na číslo" , max , "je maximum")
if max and min != cislo1:
    print ("Od maxima po minimum:" , max, cislo1, min)
elif max and min != cislo2:
    print ("Od maxima po minimum:" , max, cislo2, min)
else:
    print ("Od maxima po minimum:" , max, cislo3, min)