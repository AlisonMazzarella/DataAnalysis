#Question 2: Do fetuses with lower baseline heart rates have higher percentage of time with abnormal long term variability?
#Answer 2: Yes, based on our line graph, we can identify that fetuses with lower baseline heart rates experience higher percentage of time with abnormal long term variability. 

import pandas as pd
from matplotlib import pyplot as plt


#take data 
data = pd.read_csv("fetal_health.csv")

#form dataframe
data = data.head()

df = pd.DataFrame(data, columns=["percentage_of_time_with_abnormal_long_term_variability", "baseline_value"])

#plot the dataframe
df.plot(x="percentage_of_time_with_abnormal_long_term_variability", y=["baseline_value"], kind="line", figsize=(9, 8))

#print bar graph 
plt.show()