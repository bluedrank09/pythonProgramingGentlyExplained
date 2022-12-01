def convertToCelcius(userTemperatureValue, userTemperatureUnit):
    match userTemperatureUnit.lower():
        case 'kelvin':
            degreesCelcius = userTemperatureValue - 273.15
        case 'farenheit':
            degreesCelcius = (userTemperatureValue-32)*(5/9)

    return(degreesCelcius)

def convertToFarenheit(userTemperatureValue, userTemperatureUnit):
    match userTemperatureUnit.lower():
        case 'celcius':
            degreesFarenheit = userTemperatureValue*(9/5) + 32
        case 'kelvin':
            degreesFarenheit = 1.8*(userTemperatureValue-273) + 32
    
    return(degreesFarenheit)
            


    degreesFarenheit = userTemperatureValue*(9/5) + 32
    return(degreesFarenheit)

def convertToKelvin(userTemperatureValue, userTemperatureUnit):
    match userTemperatureUnit.lower():
        case 'farenheit':
            degreesKelvin = (5/9)*userTemperatureValue + 459.67
        case 'celcius':
            degreesKelvin =userTemperatureValue + 273.15
    return(degreesKelvin)


if __name__ == "__main__":
    try:
        userTemperatureUnit = input(f"What unit do you want to give the temperature in ? : ")
        
        if userTemperatureUnit == "farenheit" :
            userTemperatureValue = int(input(f"What is the temperature Farenheit you want to convert ? : "))
            userConvertTo = input(f"What unit do you want to convert it to ? : ")
            
            if userConvertTo == 'kelvin':
                degreesKelvin = convertToKelvin(userTemperatureValue, userTemperatureUnit)
                print(f"{userTemperatureValue} degrees farenheit is {degreesKelvin} drgrees kelvin")

            elif userConvertTo == 'celcius':
                degreesCelcius = convertToCelcius(userTemperatureValue, userTemperatureUnit)
                print(f"{userTemperatureValue} degrees farenheit is {degreesCelcius} drgrees Celcius")

        elif userTemperatureUnit == "celcius":
            userTemperatureValue = int(input(f"What is the temperature Celcius you want to convert ? : "))
            userConvertTo = input(f"What unit do you want to convert it to ? : ")

            if userConvertTo == 'farenheit':
                degreesFarenheit = convertToFarenheit(userTemperatureValue, userTemperatureUnit)
                print(f"{userTemperatureValue} degrees celcius is {degreesFarenheit} drgrees farenheit")
            elif userConvertTo == 'kelvin':
                degreesKelvin = convertToKelvin(userTemperatureValue, userTemperatureUnit)
                print(f"{userTemperatureValue} degrees celcius is {degreesKelvin} drgrees kelvin")

        elif userTemperatureUnit == 'kelvin':
            userTemperatureValue = int(input(f"What is the temperature Kelvin you want to convert ? : "))
            userConvertTo = input(f"What unit do you want to convert it to ? : ")

            if userConvertTo == 'farenheit':
                degreesFarenheit = convertToFarenheit(userTemperatureValue, userTemperatureUnit)
                print(f"{userTemperatureValue} degrees celcius is {degreesFarenheit} drgrees farenheit")
            elif userConvertTo == 'celcius':
                degreesCelcius = convertToCelcius(userTemperatureValue, userTemperatureUnit)
                print(f"{userTemperatureValue} degrees kelvin is {degreesCelcius} drgrees celcius")


            

            #print(f"{userTemperatureValue} degrees celcius is {degreesFarenheit} degrees Farenheit")

    except Exception as error:
        raise error

    finally:
        print(f":)")