import sys

def collatz(number):
    
        if number == 1:
            print('This is the end.')
            return number
            sys.exit()
    
        #even
        if number % 2 == 0:
            number = number // 2
            print (number)
        
        #odd    
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
    
        return collatz(number)
    
        

if __name__ == "__main__":
    try:
        user_input = int (input ('Give us an integer. \n') )
        collatz( user_input )
     
    except Exception:
        print('i really meant it about the integer \n ')