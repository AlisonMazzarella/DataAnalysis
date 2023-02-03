#Question 3 (stretch challenge): Do fetuses with histograms with more peaks have a higher chance of fetal mortality? 
#Answer 3: Based on our scatter plot results we can see that fetuses with more peaks in their histograms are more commonly diagnosed as having a normal fetal health prediction. 

import pandas as pd
from matplotlib import pyplot as plt


#take data 
data = pd.read_csv("fetal_health.csv")

#form dataframe
data = data.head()

df = pd.DataFrame(data, columns=["histogram_number_of_peaks", "fetal_health"])

#plot the dataframe
df.plot(x="histogram_number_of_peaks", y=["fetal_health"], kind="scatter", figsize=(9, 8))

#print bar graph 
plt.show()