add = lambda a , b : a + b
print(add(2 , 3))

square = lambda num :num *num 
print(square(5))

nums = [1 ,2 ,3 ,4]
squares =list(map(lambda x :x * x , nums))
print(squares)

l = [1 ,2 ,3 ,4]
double = list(map(lambda k: k * 2, l))
print(double)

numbers = [1 , 2 , 3 , 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)