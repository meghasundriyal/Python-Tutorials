# To convert celsius value to kelvin and farenheit

def convert(celsius):
    kelvin = celsius + 273.15
    faren = (celsius*1.8) + 32
    return kelvin , faren

# Defining main
def main():
    temp = 35
    kelvin, faren = convert(temp)
    print("Celsius : ", temp, 
            "\nKelvin : ", kelvin, 
            "\nFarenheit : ", faren)

if __name__ == "__main__":
    main()            