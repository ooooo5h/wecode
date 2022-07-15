def get_even_number(num):
    
    even_numbers = []
    
    for i in range(1, num+1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            continue
        
    return even_numbers
