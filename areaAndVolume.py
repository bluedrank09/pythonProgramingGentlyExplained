def area(length, width):
    totalArea = length*width
    return(totalArea)

def perimeter(length, width):
    totalPerim = (length*2) + (width*2)
    return(totalPerim)

def volume(length, width, height):
    totalVolume = length*width*height
    return(totalVolume)

def surfaceArea(length, width, height):
    totalSurfaceArea = ((length*width*2) + (length*height*2) + (width*height*2))
    return(totalSurfaceArea)

if __name__ == "__main__":
    try:
        length = int(input(f"Give me a value for the length : "))
        width = int(input(f"Give me a value for the width : "))
        calcToPerform = input(f"What do you want to calculate ? : ")

        if calcToPerform.lower() == 'area':
            print(f"The area is {area(length, width)}")
        elif calcToPerform.lower() == 'perimeter':
            print(f"THe perimeter is {perimeter(length, width)}")
        elif calcToPerform.lower() == 'volume':
            height = int(input(f"Give me a value for the height : "))
            print(f"The volume is {volume(length, width, height)}")
        elif calcToPerform.lower() == 'surface area':
            height = int(input(f"Give me a value for the height : "))
            print(f"The surface area is {surfaceArea(length, width, height)}")
            

    except Exception as error:
        raise error

    finally:
        print(f":)")