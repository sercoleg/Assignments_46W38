# Prepare variables

numbers = []    # empty list of values

# ------------
# Users inputs
# ------------

while True:     # will run always except when breaking it. It will ask for user inputs until end is given
    userinput = input('input your number or type: end to finish')
    if userinput == 'end': # In case of end, the input loop will end
        break

# ------------
# Looking for minimal and maximal value in user inputs without using specific functions for this.
# ------------

if numbers: # in case that numbers were added it will look for min and max, otherwise the code will end with a message 'no numbers added'
    minvalue = numbers[0]
    maxvalue = numbers[0]
    for x in numbers[1:]:
        if x < minvalue:
            minvalue = x
        if x > maxvalue:
            maxvalue = x
    print('Inputs numbers:', numbers)
    print('Minimal number:', minvalue)
    print('Maximal number:', maxvalue)
else:
    print('no numbers added')
