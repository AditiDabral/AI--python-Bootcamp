#LIst : are mutable : can be change 
randoms= [1,2,4,"d"]

randoms.append("apple")

randoms.insert(2,"cherry")

print(randoms.append("Tiya"))
print(randoms)

randoms.remove("cherry")
print(randoms)

del randoms[0]
print(randoms)

randoms.pop() # by default remove last element // randoms.pop(1) delete the second element 
print(randoms)

# ***** Slicing ***
sliced= randoms[2:3]
print(sliced)
print(randoms[:4])

###########################################################

# tuples : they are immutable (which cant be changed)
single_item = ("glass",)
colurs = ("blue,black,white")

# acessing element in tuples
print(colurs[-1])

############################################################
# DICTIONARY : keys andvalues pair 
student = {"name":"Alex","age": 23,"State":"UP"}

#iterate a dict : creating a list frrom dict 
for key, value in student.items():
    print(key,"=",value)

student["college"]="ITT Madras" #updating 

print(student)
print(student["name"])

# del key and value 

del student["college"]
print(student)

student.pop("age")
print(student)

###########################
# sets: unorder collection of unquie items , u cant have repetative items
set1 = {1,2,3}
set2 = {3,4,5,6}
print(set1)

set1.add(50) # adding 
print("set1 =",set1)

print("set2 =",set2)
set2.remove(4) # deleting 
print("set2 after removing 4 =",set2)

empty_set = set()

# set operation
print(set1 | set2) #union 

print(set1 & set2)  #intesection : common
print(set1 - set2 ) # difference : print diff in set 1 as compare to set 2 