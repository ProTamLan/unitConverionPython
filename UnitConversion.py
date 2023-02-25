def Menu(): #define function named menu with no parameters
    print('1. Miles to Kilometers')
    print('2. Pounds to tons')
    print('3. Farenheit to Celsius')
    print('4. Decimal to Binary')


def miles_km():
    miles = float(input("Enter Miles: "))
    km = miles * 1.60934
    print("The Distance in Kilometers is: ", km)

def km_miles():
    km = float(input("Enter Total Kilometers(km): "))
    miles = km/1.60934
    print("The Distance in Miles: ", miles)

def Pounds_Tons():
    Pounds = float(input("Enter Total Pounds (lbs): "))
    Tons = Pounds * 0.0005
    print("Total Weight of {1} lbs in Tons is: {0}".format(Tons, Pounds))

def Farenheit_Celsius():
    Farenheit = float(input("Enter Total Farenheit (F): "))
    Celsius = (Farenheit - 32) * 5/9
    print("The Temperature in Celsius is: ", Celsius)

def Decimal_Binary():
    Decimal = int(input("Enter Decimal Number: "))
    Binary = bin(Decimal)
    print("The Binary Number is: ", Binary)    

Menu()
#choice = int(input("Enter your choice of conversion: "))
#if choice == 1: miles_km() etc...
miles_km()
km_miles()
Pounds_Tons()
Farenheit_Celsius()
Decimal_Binary()


#lime https://youtu.be/pCOkIMm2t70
