def asciiConverter(userChar):
    converted = ord(userChar)
    return(converted)

if __name__ == "__main__":
    try:
        fulllist = []
        userChar = input(f'Give me a character to  onvert to ASCII : ')
        convertedChar = asciiConverter(userChar)
        print(f'{convertedChar}')


    except Exception as error:
        raise error

    finally:
        print(f':D')