

def readcurrency(filename):
        
    new_list = []
    with open (filename, "r") as file_object:
        for lines in file_object:
            x = lines.partition(" ")
            new_dict = {}
            symbol = x[0]
            rate = x[2]
            new_dict['symbol'] = symbol
            new_dict['rate'] = rate
            print(new_dict)
            new_list.append(new_dict)
            
    print(new_list)
            # new_list = []
            # new_dict = 
            # new_list.append(new_dict)
    #return new_list

#print(readcurrency('currency.txt'))

readcurrency("currency.txt")