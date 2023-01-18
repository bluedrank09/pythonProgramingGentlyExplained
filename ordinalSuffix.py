def ordinalNumber(userNumber):
    if userNumber%10 == 1:
        finalResult = f"{userNumber}st"
    elif userNumber%10 == 2:
        finalResult = f"{userNumber}nd"
    elif userNumber%10 == 3:
        finalResult = f"{userNumber}rd"
    else:
        finalResult = f"{userNumber}th"

    return(finalResult)


if __name__ == "__main__":
    try:
        userNumber = int(input(f"Give me a number : "))
        print(ordinalNumber(userNumber))

    except Exception as error:
        raise error 

    finally:
        print(f":D")