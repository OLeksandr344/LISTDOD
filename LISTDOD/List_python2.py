#F: Найбільший елемент
x = [1, 2, 3, 2, 1]
px = max(x)
dx = x.index(px)
print(px, dx)
print('---------------')
#G: Більше своїх сусідів
def neighbrd(lst1):
    count = 0
    for i in range(1, len(lst1)):
        if lst1[i] > lst1[i-1] and lst1[i] > lst1[i+1]:
            count += 1        
    return count
print(neighbrd([1,0,1,0,1,0,1,0]))
print('---------------')       
#H: Найменший додатний
x = [5,-4,3,-2,1]
xm = min(i for i in x if i > 0)                  
print((xm))
print('---------------')
#I: Найближче число
def nearest(lst, n):
    return min(lst, key=lambda x: abs(x - n))
print(nearest([6,5,4,2,1],3))
print('---------------')
#j шеренга
heights = [165, 163, 160, 160, 157, 157, 155, 154]  
#x = int(input("ріст")) 
x = 160
index = len(heights) 
print(index) 
while index > 0 and heights[index - 1] < x: 
    index -= 1
print(index + 1)
print('---------------') 
 #Кількість різних елементів
def count_not_equal(lst):
    unique_elems = set(lst)
    count = len(unique_elems)
    return count
print(count_not_equal([1,2,2,3,3,3]))
print('---------------') 
#L: Найменший непарний
def minpar(lst):
    min_val = float('inf')
    for i in lst:
        if i % 2 != 0 and i < min_val and i >0:
            min_val = i
    if min_val == float('inf'):
        return 0
    return min_val
print(minpar([3,1,2,4,6,8]))
print('---------------') 
#M зворот        
def reverse_list(lst):
    n = len(lst)
    for i in range(n//2):
        lst[i], lst[n-i-1] = lst[n-i-1], lst[i]
    return lst
print(reverse_list([1,2,3,4,5]))         
           
        
            


        
            
        
    
        
    

     
            
                                 
        
            
            
        
        
        

    