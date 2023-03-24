#N: Переставити сусідні
def swap_elements(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst
print(swap_elements([1,2,3,4,5]))
#O: Переставити min і max
st = [3, 4, 5, 2, 1]
min_index = st.index(min(st))
max_index = st.index(max(st))
st[min_index], st[max_index] = st[max_index], st[min_index]
print(st)
#R: Кількість співпадаючих пар
def count_pairs(numbers):
    pairs_count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                pairs_count += 1
    return pairs_count
print(count_pairs([1,2,3,2,3]))
#T: Кількість різних елементів - 2
def count_unique_elements(lst):
    unique_elements = set(lst)
    return len(unique_elements)
print(count_unique_elements([3,2,1,2,3]))
#V: Унікальні елементи
lst = [1, 2, '+', 2, 3, 3, 3,'-']
count = -1
for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        count += 1
print(count)
    