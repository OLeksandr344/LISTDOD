#A парні індекси
x = [1, 2, 3, 4, 5]
pair_ind = x[::2]
print(pair_ind)
print('---------------')
#B: Парні елементи
def pair_numb(ls):
    pair_ls = []
    for i in ls:
        if i % 2 == 0:
            pair_ls.append(i)
    return pair_ls  
print(pair_numb([1,2,3,4]))
print('---------------')
#C: Більше попереднього
def numb_lst(lsn):
    new_lst = []
    for i in range(len(lsn)):
        if lsn[i] > lsn[i-1]:
            new_lst.append(lsn[i])                     
    return new_lst
print(numb_lst([1, 5, 2, 4, 3]))
print('---------------')
#D: Перший додатний 
x = [-1, 0, 1]
for i in x:
    dx = x.index(i>0)
print(dx)
print('---------------')
#E: Перший додатній - 2
dx = (i for i in range(len(x)) if x[i] > 0)
result = next(dx, -1)
print(result)    

  

    

    
    

    



        
        
        
        
    

        
        
    