def get_a_list_of_numbers():
    # Prepare variables
    list_of_numbers = []    # empty list of values
    # Users inputs

    while True:     # will run always except when breaking it. It will ask for user inputs until end is given
        userinput = input('input your number or type: end to finish')
        if userinput == 'end': # In case of end, the input loop will end
            break
        n = float(userinput)
        list_of_numbers.append(n)
    return list_of_numbers

def find_min(list_of_numbers):
    # Looking for minimal value in user inputs without using specific functions for this.

    if not list_of_numbers: # in case that numbers were not added it will return None
        return None
    minvalue = list_of_numbers[0]
    for x in list_of_numbers[1:]:
        if x < minvalue:
            minvalue = x
    return minvalue

def find_max(list_of_numbers):
    # Looking for maximal value in user inputs without using specific functions for this.

    if not list_of_numbers: # in case that numbers were not added it will return None
        return None
    maxvalue = list_of_numbers[0]
    for x in list_of_numbers[1:]:
        if x > maxvalue:
            maxvalue = x
    return maxvalue
