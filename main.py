soat=int(input("Soat(0-23):"))
if 5<=soat<=11:
    print("Xayrli kun")
if 12<=soat<=17:
    print("Xayrli kun")
if 18<=soat<=22:
    print("Xayrli kun")
else:
    print("Xayrli kun")

a = float(input("Birinchi son: "))
amal = input("Amal (+, -, *, /): ")
b = float(input("Ikkinchi son: "))

if amal == "+":
    print("Natija:", a + b)
elif amal == "-":
    print("Natija:", a - b)
elif amal == "*":
    print("Natija:", a * b)
elif amal == "/":
    if b != 0:
        print("Natija:", a / b)
    else:
        print("Nolga bo'lish mumkin emas")
else:
    print("Noto'g'ri amal")
summa = int(input("Xarid summasi: "))
if summa > 500000:
    print("Chegirma: 10%")
    print("To'lov:", summa * 0.9, "so'm")
elif summa > 200000:
    print("Chegirma: 5%")
    print("To'lov:", summa * 0.95, "so'm")
else:
    print("Chegirma yo'q")
    print("To'lov:", summa, "so'm")
yosh = int(input("Yoshingiz: "))
if yosh < 0:
    print("Xato yosh")
elif yosh <= 12:
    print("Bola")
elif yosh <= 17:
    print("O'smir")
elif yosh <= 59:
    print("Kattalar")
else:
    print("Keksa")
rang = input("Svetofor rangi: ").lower()
if rang == "qizil":
    print("To'xtang")
elif rang == "sariq":
    print("Tayyor turing")
elif rang == "yashil":
    print("Yuring")
else:
    print("Noma'lum rang")
    print("xato rang")