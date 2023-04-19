#!/usr/bin/env python
# coding: utf-8

# In[1]:


str = input("Enter your state of origin:")

print("Your state of origin is:",str)
print("The first character is:",str[0])
print("The characters starting from 3rd to 5th are:", str[2:5])
print("The string starting from 3rd character is:", str[2:])
print("state of origin two times", str * 2)


# In[3]:


# Input from user
m = float(input("Enter mass in kilogram: "))

# constant value for the speed of light in m/s
c = 299792458

# calculating energy using Einstein's equation
energy = m * c ** 2

# Display the result
print(f"The energy equivalent to {m} kg of mass is {energy} joules.")


# In[4]:


list = [ 'Anaconda', 786, 2.23, 'Jupyter', 70.2]
shortlist = [321,'python']

print(list)          # prints complete list 
print(list[0])       # prints first element of the list
print(list[1:3])     # prints elemensts starting from 2nd till 3rd
print(list[2:])      # Prints elements starting from 3rd element'''
print(shortlist * 2)  # prints list two times
print(list + shortlist) # prints concatenated lists


# In[5]:


tuple = ("Ekiti, 750, 'Oshogbo', 250, Akure",500)
s_tuple = ("Abeokuta", 300, "Ogbomoso")

# prints the complete tuple
print (tuple)

# print last elements of the tuple
print (tuple[-1])

# prints elements of the tuple strating from 2nd till 3rd
print (tuple[2:4])

# prints elements of the tuple starting from 3rd element
print (s_tuple * 3)

# prints concatenated tuples
print (tuple + s_tuple)


# In[7]:


# Returns false as game_1 is not equal to game_2
game_1 = 2
game_2 = 4
print(bool(game_1 == game_2))
# Or
print(game_1 == game_2)


#Returns False as val is None
val = None
print(bool(val))

# Returns false as num is an empty sequence
num = ()
print(bool(num))

# Returns true as age is boolean
age = True
print(bool(age))


# In[10]:


# Convert to int 

grade = int(70)   # grade will be 70
gpa = int(4.9)     # gpa will be 4.9
cgpa = int(4)      # cgpa will be 4

print(f"Grade = {grade}")
print(f"GPA = {gpa}")
print(f"CGPA = {cgpa}")


# In[11]:


# Convert to float

grade = float(97)
gpa = float(5)
cgpa = float(4.7)

print(f"Grade = {grade}")
print(f"GPA = {gpa}")
print(f"CGPA = {cgpa}")


# In[ ]:




