def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celcius_to_kelvin(celcius):
    kelvin = (celcius + 273.15)
    return kelvin

def kelvin_to_celcius(kelvin):
    celcius = (kelvin - 273.15)
    return celcius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5 - 459.67)
    return fahrenheit
def main():
    print("Program Konversi Suhu")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celcius ke Kelvin")
    print("4. Kelvin ke Celsius")
    print("5. Fahrenheit ke Kelvin")
    print("6. Kelvin ke Fahrenheit")

    try:
        pilihan = int(input("Masukkan pilihan (1-6): "))

        if pilihan == 1:
            celsius = float(input("Masukkan suhu dalam Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} derajat Celsius sama dengan {fahrenheit:.2f} derajat Fahrenheit.")
        elif pilihan == 2:
            fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius:.2f} derajat Celsius.")
        elif pilihan == 3:
            celcius = float(input("Masukkan suhu dalam celcius: "))
            kelvin = celcius_to_kelvin(celcius)
            print(f"{celcius} derajat Celcius sama dengan {kelvin:.2f} derajat Kelvin.")
        elif pilihan == 4:
            kelvin = float(input("Masukkan suhu dalam Kelvin: "))
            celcius = kelvin_to_celcius(kelvin)
            print(f"{kelvin} derajat kelvin sama dengan {celcius:.2f} derajat Celsius.")
        elif pilihan == 5:
            fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit} derajat Fahrenheit sama dengan {kelvin:.2f} derajat Kelvin.")
        elif pilihan == 6:
            kelvin = float(input("Masukkan suhu dalam Kelvin: "))
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin} derajat Fahrenheit sama dengan {fahrenheit:.2f} derajat Fahrenheit.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan pilihan yang valid (angka).")


if __name__ == "__main__":
    main()
