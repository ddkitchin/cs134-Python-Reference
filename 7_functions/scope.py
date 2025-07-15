# @copyright Deborah Kitchin

# value = 10000 #uncomment to make a global variable value

def main() -> None:
    # noinspection GrazieInspection,AiaStyle
    """
        Uncomment to bring in global variable value. It can now be changed by main().
        global value #
        print("value in before input statement",value)
        """

    value = int(input("Enter a side length:"))
    #print("value after input statement before call to cubeVolume",value)
    print(cube_volume(value))
    #print(sideLength) #can't access in main... local to cubeVolume). Same situation for result


# noinspection AiaStyle
def cube_volume(side_length: int) -> int:
    """ 1) if no value on line 1 then this will blow up because cubeVolume does
    no have access to value in main even thought it is called by main.
        2) if value is on line 1 then it will print the value of the global variable.

    print("value inside cubeVolume",value)
    """
    result = side_length ** 3
    return result
    #return sideLength ** 3 # this is the same as 2 lines above. If you don't need to keep variable this is enough.


''' 1) if no value on line 1 then this will blow up because main variable value is gone.
    2) if value is on line 1 then it will print the value of the global variable at the end of the program.
    
print("final Value",value)
'''


if __name__ == "__main__":
    main()
