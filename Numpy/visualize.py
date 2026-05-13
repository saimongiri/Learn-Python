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