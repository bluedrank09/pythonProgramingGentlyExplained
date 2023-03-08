def getSmallest(listOfNumbers):
    #minNumber = listOfNumbers.min()
    minNumber = min(listOfNumbers)
    return minNumber

def getBiggest(listOfNumbers):
    #maxNumber = listOfNumbers.max()
    maxNumber = max(listOfNumbers)
    return maxNumber

if __name__ == "__main__":
    try:
        listOfNumbers = []

        userListLength = int(input("How many numbers do you want in your list ? : "))

        for i in range(0, userListLength):
            newNumber = int(input("Input a number : "))
            listOfNumbers.append(newNumber)
            i = i+1

        minOrMax = input("Do you want to find the min or max of those numbers ? : ")

        if minOrMax.lower() == 'min':
            print(f"The smallest number is {getSmallest(listOfNumbers)}")
        elif minOrMax.lower() == 'max':
            print(f"The smallest number is {getBiggest(listOfNumbers)}")
            

    except Exception as error:
        raise error

    finally:
        print(f":D")