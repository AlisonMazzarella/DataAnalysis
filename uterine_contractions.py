#Question 1: Do fetuses whose mothers endure longer uterine contractions have higher abnormal short term variability? 
#Answer 1: No, actually fetuses have higher abnormal short term variability if their mothers experience shorter uterine contractions. 

import pandas as pd
from matplotlib import pyplot as plt


#take data 
data = pd.read_csv("fetal_health.csv")

#form dataframe
data = data.head()

df = pd.DataFrame(data, columns=["uterine_contractions", "abnormal_short_term_variability"])

#plot the dataframe
df.plot(x="uterine_contractions", y=["abnormal_short_term_variability"], kind="bar", figsize=(9, 8))

#print bar graph 
plt.show()
