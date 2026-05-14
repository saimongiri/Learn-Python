import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# Displots stands for distribution plot 
sns.displot([0,1,2,3,4,5])
plt.show() # with histogram

# Plotting Displot without histogram

sns.displot([1,2,3,4,5],kind="kde")
plt.show()

# Normal Distribution

x = random.normal(loc=1 ,scale=2 ,size=(2,3)) #loc - mean 
# scale - standard deviation
# size - the shape of the returned array

print(x)

# visualization of normal distribution

sns.displot(random.normal(size=1000),kind="kde")
plt.show()

# Binomial Distribution - Discrete Distribution
# It has 3 parameter :
# n - number of trials
# p - probability of occurance of each trial
#  size - the shape of returned array

x = random.binomial(n=10 , p=0.5 , size=10)
print(x)

# Visualization of Binomial Distribution

sns.displot(x)
plt.show()

# Poisson Distribution 

# lam - rate or known number of occurances 
# size - the size of returned array

x = random.poisson(lam=4 , size=10)
print(x)

sns.displot(random.poisson(lam=5 , size=1000))
plt.show()

# Uniform Distribution
# used to describe probability where every event has equal chances of occuring

# low - lower bound default 0.0
# high - higher bound default 1.0
# size - the shape of returned array

x = random.uniform(size=(2,3))
print(x)

sns.displot(random.uniform(size=1000),kind="kde")
plt.show()

# Logistic Distribution
# used to describe growth
# has parameter : loc,scale and size (already explained)

x = random.logistic(loc=1 , scale=2 ,size=10)
print(x)

sns.displot(random.logistic(loc=5 , scale=10, size=1000))
plt.show()

# Multinomial Distribution
# is generalization of binomial distribution
# has 3 parameter
# n - number of times to run the experiment
# pvals - list of probabilites of outcomes
# size - the shape of the returned array

x = random.multinomial(n= 6 ,pvals=[1/6,1/6,1/6,1/6,1/6,1/6] )
print(x)

# Exponential Distribution
# is used for describing time till next event eg : success / failure etc
# has 2 parameter : scale- inverse rate defaults to 1.0
# size

x = random.exponential(scale=2,size=(2,3))
print(x)

sns.displot(random.exponential(size=1000),kind="kde")
plt.show()

# Chi square Distribution
# used as a basis to verify the hypothesis

# has 2 parameter: df- degree of freedom
# size

x = random.chisquare(df=2 ,size=(2,3))
print(x)

sns.displot(random.chisquare(df=1,size=1000),kind="kde")
plt.show()

# Rayleigh Distribution
# is used for signal processing
# parameter : scale and size

x = random.rayleigh(scale=2 , size=(2,3))
print(x)

# visualized

sns.displot(random.rayleigh(size=1000),kind="kde")
plt.show