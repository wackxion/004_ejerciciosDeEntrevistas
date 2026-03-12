# A

def analicis(n):
    if n % 3 == 0 :
        print("Fizz " + str( n))
    elif n % 5 == 0 :
        print("Buzz " + str( n))
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz " + str( n))
    else:
        print(n)


for i in range(100):
    analicis(i)


# B

def leeAlDerechoYAlReves(unaFrace):
    if unaFrace.replace(" ", "") == unaFrace[::-1].replace(" ", ""):
        print("Es un palindromo")
    else:
        print("No es un palindromo")

leeAlDerechoYAlReves("anita lava la tina")

# C

def dameUnNumero():
    unNumero = int(input("Dame un numerodel 1 al 10: "))
    # devolverlos en numeros romanos
    numerosRomanos = {
        1: "I", 
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"}
    if unNumero in numerosRomanos:
        print(numerosRomanos[unNumero])

dameUnNumero()


