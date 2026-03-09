waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w cm: "))

bmi = waga / (wzrost / 100) ** 2

print(f"Twoje BMI wynosi: {bmi:.2f}")

if bmi < 18.5:
    print("Niedowaga")
elif 18.5 <= bmi < 25:
    print("Waga prawidłowa")
elif 25 <= bmi < 30:
    print("Nadwaga")
else:
    print("Otyłość")