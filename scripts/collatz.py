import sys

def collatz(number):
    
    if number == 1:
        print('This is the end.')
        return number
        sys.exit()
    
    # floor divide even number
    if number % 2 == 0:
        number = number // 2
        print (number)
        
    # transform odd number    
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
    
    return collatz(number)
        

if __name__ == "__main__":
    one_at_the_end = collatz(int (input() ) )