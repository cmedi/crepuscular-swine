#zigzag print from automate the boring stuff with python 2e

import time, sys
indent = 0 #space indentation
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second

        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 2
            if indent == 40:
                # change direction
                indentIncreasing = False
        else:
            #decrease the number of spaces
            indent = indent - 2
            if indent == 0:
                #change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
