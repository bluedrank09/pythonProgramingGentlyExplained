def convertFromHours(convertTo, userNumber):
    if convertTo.lower() == 'minutes':
        finalNumber = f"That is {userNumber*60} minutes"
    elif convertTo.lower == 'seconds':
        finalNumber = f"That is {userNumber*3600} seconds"
    
    return(finalNumber)

def convertFromMinutes(convertTo, userNumber):
    if convertTo.lower() == 'hours':
        finalNumber = f"That is {userNumber/60} hours"
    elif convertTo.lower == 'seconds':
        finalNumber = f"That is {userNumber*60} hours"
    
    return(finalNumber)

def convertFromSeconds(convertTo, userNumber):
    if convertTo.lower() == 'hours':
        finalNumber = f"That is {userNumber/3600} hours"
    elif convertTo.lower == 'minutes':
        finalNumber = f"That is {userNumber/60} minutes"
    
    return(finalNumber)
    
if __name__ == "__main__":
    try:
        userInitalUnit = input(f"What unit are you going to give te number in : ")
        userNumber = int(input(f"Give me the number of {userInitalUnit} : "))

        if userInitalUnit.lower() == 'hours':
            convertTo = input(f"What do you want to convert {userInitalUnit} to : ")
            print(convertFromHours(convertTo, userNumber))

        if userInitalUnit.lower() == 'minutes':
            convertTo = input(f"What do you want to convert {userInitalUnit} to : ")
            print(convertFromMinutes(convertTo, userNumber))

        if userInitalUnit.lower() == 'seconds':
            convertTo = input(f"What do you want to convert {userInitalUnit} to : ")
            print(convertFromSeconds(convertTo, userNumber))

    except Exception as error:
        raise error 

    finally:
        print(f":D")