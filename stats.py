import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Notebooks/covid_19_data.csv')
df = pd.DataFrame(data)
df.rename(columns={ "ObservationDate":"timestamp","Province/State": "State", "Country/Region": "Country"}, inplace=True )
df.dropna(inplace=True)
city_index = df[df["Country"]== "India"].index.values
countries = df.groupby('Country')
confirmed = df.loc[city_index, "Confirmed"].values
deaths = df.loc[city_index, "Deaths"].values
recovered = df.loc[city_index, "Recovered"].values
x = np.arange(1)
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
fig.set_facecolor("#e6dfed")
axes.set_title('Covid19 Visualization')
axes.set_xlabel("India")
axes.set_facecolor("#e6dfed")
axes.bar(x + 0.2,deaths.max(), width=0.3,label="deaths")
axes.bar(x + 0.5,recovered.max(),width=0.3, label="recoveries")
axes.bar(x + 0.8, confirmed.max(),width=0.3,label="Confirmed")
axes.set_xticks(np.arange(3))
axes.text(x + 0.08,deaths.max(),deaths.max(), fontsize = 15) 
axes.text(x + 0.4,recovered.max(),recovered.max()) 
axes.text(x + 0.7, confirmed.max(), confirmed.max()) 
axes.legend()
