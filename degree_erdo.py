dict_test = {"A": ["B", "C"], "B": ["A", "C"], "C":["A", "B", "D"], "D": ["C"]}
def degree_sequence(dict_var):
  list_var = list()
  for x in dict_var:
    #print(len(dict_test[x]))
    list_var.append(len(dict_test[x]))
  list_var.sort(reverse = True)
  return list_var
def Erdos_Gallai(list_var):
    #First step: add all numbers together and check if it is even
    sum = 0
    for x in list_var:
        sum += x
    #if not even return false
    if(sum % 2 != 0):
        return False
    #Second step: follow erdo's summation formula
    n = len(list_var)
    k = 1
    #loop responsible for each k value
    while(k != n+1):
        left_sum = 0
        right_sum = 0
        #loop responsible for left_sum value
        for iter in range(k):
            left_sum += list_var[iter]
        #create constant needed: k(k-1) and adjust k
        right_sum_const = (k - 1) * k
        right_sum += right_sum_const
        j = k + 1
        #loop responsible for right_sum value
        for iter_2 in range(len(list_var)):
            if(iter_2 >= j-1):
                right_sum += min(list_var[iter_2], iter_2 + 1)
        #conditional that rules out false sequences
        if(left_sum > right_sum):
            return False 
        k += 1
    #If while loop is broken then the degree sequence is true
    return True

    

list_test = list()
list_test = degree_sequence(dict_test)
bool_val = Erdos_Gallai(list_test)
print("BOOL VAL: ")
print(bool_val)

#THIS LOOP PRINT [3,2,2,1]
#for i in list_test:
#    print(i)

