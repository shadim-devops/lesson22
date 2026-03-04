waga = float(input("Podaj wagę (kg): "))
wzrost = float(input("Podaj wzrost (cm): "))

bmi = waga / (wzrost / 100) ** 2

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("niedowaga")
elif bmi < 25:
    print("waga prawidłowa")
elif bmi < 30:
    print("nadwaga")
else:
    print("otyłość")