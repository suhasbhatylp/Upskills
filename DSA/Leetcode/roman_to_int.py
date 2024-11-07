def roman_to_decimal(value):
    my_dict  = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(value) - 1):
        if my_dict[value[i]] >= my_dict[value[i+1]] :
            result += my_dict[value[i]]
        else :
            result -= my_dict[value[i]]
    return result + my_dict[value[-1]]


print(roman_to_decimal('XIIX'))
