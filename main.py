def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    if (num1 < num2):
        if (num1 < num3): 
            minval = num1
        else:
            minval = num3
            
    else:
        if (num2 < num3):
            minval = num2
        else:
            minval = num3
    
    if (num1 > num2):
        if (num1> num3):
            maxval = num1
        else:
            maxval = num3
    else:
        if (num2 > num3):
            maxval = num2
        else:
            maxval = num3
            
    if (
        
          
    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
