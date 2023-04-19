#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pyhton to calculate simple intererst
P=float(input("Enter the Principle Amount:"))
R=float(input("Enter the rate of interest:"))
T=float(input("Enter the Time period in years:"))

# calculating simple interest
A=P*(1+(R/100)*T)

#printing the result
print("simple interest is:",A)


# In[ ]:


#python to calculate compound interest
P=float(input("Enter the Principle Amount:"))
R=float(input("Enter the Rate of interest:"))
T=float(input("Enter the Time period in years:"))
N=int(input("Enter the number of compounded interest in a year:"))

# calculating compoud interest
A=P*(1+R/N)*N*T

#printing result
print("Compound Interest is:",A)


# In[ ]:


#pyhton to calculate Annuity Plan
R=float(input("Enter the Rate Amount:"))
N=int(input("Enter the number of compounded interest in a year:"))
PMT=float(input("Enter the payment per period:"))
T=float(input("Enter the time period in years:"))

#calculating Annuity plan
numerator=PMT*((1+R/N)*(N*T)-1)
denomenator=R/N
A=numerator/denominator

#printing the result
print("Annuity plan is:",A)


# In[ ]:




