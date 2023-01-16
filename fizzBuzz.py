def fizzBuzzChecker(userNumber):
    completeList = []
    for i in range (1,userNumber+1):
        if i%3 == 0 and i%5 != 0:
            completeList.append('Fizz')
        if i%5 == 0 and i%3 != 0:
            completeList.append('Buzz')
        if i%3 == 0 and i%5 == 0:
            # completeList.pop[(len(completeList))-1]
            # completeList.pop[(len(completeList))-2]
            #completeList.remove((len(completeList))-1)
            #completeList.remove()
            completeList.append('FizzBuzz')
        if i%3 != 0 and i%5 != 0:
            completeList.append(i)

    return(completeList)

if __name__ == "__main__":
    try:
        userNumber = int(input(f"Give me a number : "))
        print(f"{fizzBuzzChecker(userNumber)}")

    except Exception as error:
        raise error

    finally:
        print(f":D")
