#First python assignment
#name : Ransford Addai
#Training ID : 32524




# 1. Variables
x = 10
print(x)
greetings = "Hello"
print(greetings)
new_variable = 8
print(new_variable)
print(type(new_variable))



# 2. Data types
integer_variable = 5
float_variable= 4.2
string_variable = "11"
boolean_variable = False
print(integer_variable, type(integer_variable))
print(float_variable, type(float_variable))
print(string_variable, type(string_variable))
print(boolean_variable, type(boolean_variable))
integer_variable = str(5)
float_variable = bool(4.2)
string_variable = int("11")
boolean_variable = float(False)
print(integer_variable, type(integer_variable))
print(float_variable, type(float_variable))
print(string_variable, type(string_variable))
print(boolean_variable, type(boolean_variable))




# 3. Sets
set_of_numbers = {1,2,3,4,5,6,7,8,9,10}
set_of_numbers.add(11)
set_of_numbers.remove(5)
print(3 in set_of_numbers)
print(len(set_of_numbers))




# 4. Lists
ordered_list = [1,2,3,4,5,6,7,8,9,10]
ordered_list.append(11)
ordered_list.remove(5)
print(3 in ordered_list)
ordered_list.pop(0)
print(len(ordered_list))
ordered_list.reverse()
print(ordered_list)




# 5. Tuples
my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple)
print(3 in my_tuple)
#A tuple is immutable, however, I can indirectly add a number by concatenating
number_to_add = 11
new_tuple = my_tuple + (number_to_add,)
print(new_tuple)




# 6. Dictionaries
myDict = {"name": "Ama", "age": 8, "country": "Ghana"}
print(myDict.get("age"))
myDict["country"]= "Togo"
print(myDict)
myDict.update({"Hometown": "Kumasi"})
print(myDict)
del myDict["age"]
print(myDict)





# 7. Mathematical operations
a = 3
b = 5
print(a+b)
print(a*b)
c = 3+ 5
print(c)
d = 3-5
print(d)
e = 3*5
print(e)
f = 3/5
print(f)
print(5%2)
print(5**3)
#to find the square root of a number we import math
import math
print(math.sqrt(4))





# 8. Casting
num_string = "5"
num_string = int("5")
print(num_string)
num_string = float("5")
print(num_string)








