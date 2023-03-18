def addNumbers(numbers):
    total = 0
    for i in range(0, len(numbers)):
        final = total+numbers[i]
        total = final

    return(final)
        

def multNumbers(numbers):
    total= 1
    for i in range(0, len(numbers)):
        final = total*numbers[i]
        total = final

    return(final)

def main():
    numbers = []

    amountOfNumbers = int(input(f"How many numbers do you want ? : "))

    for i in range(0,amountOfNumbers):
        newNumber = int(input(f"What's the next number ? : "))
        numbers.append(newNumber)
        #i+=1

    
    addOrMult = input(f"do you want to add or multiply those numbers ? : ")

    while addOrMult != 'add' and addOrMult !='multiply':
        print(f"you can only add or multiply the numbers...")
        addOrMult = input(f"do you want to add or multiply those numbers ? : ")
        
    if addOrMult.lower() == 'add':
        print(f"those numbers added is {addNumbers(numbers)}")
    elif addOrMult.lower() == 'multiply':
        print(f"those numbers multiplied is {multNumbers(numbers)}")



if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        raise error
    
    finally:
        print(f":D")

        # print(numbers[i])
        # print(numbers[i+1])
        # final = numbers[i] + numbers[i+1]
        # print(final)