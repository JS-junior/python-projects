import  matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Notebooks/covid_19_data.csv')
df = pd.DataFrame(data)
df.rename(columns={ "ObservationDate":"timestamp","Province/State": "State", "Country/Region": "Country"}, inplace=True )
city_index = df[df["Country"]=="India"].index.values
#df.iloc[city_index]
#df.loc[city_index, "Deaths"].values
deaths = df.loc[city_index, "Deaths"].values
recovered = df.loc[city_index, "Recovered"].values
#total = df.loc[city_index, "Deaths"].values
plt.title("Covid19 visualization")
plt.xlabel("Deaths")
plt.plot(deaths, label="death")
plt.plot(recovered, label="recoveries")
#plt.plot(total, label="cases")
plt.legend()

'''
timestamp = df.loc[city_index, "timestamp"].values
plt.title("covid19 visualization")
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
#axes.legend()
axes.plot(recovered, timestamp, markerfacecolor="yellow", markersize=10, linestyle="-")
axes.plot(deaths, timestamp, markerfacecolor="yellow", linestyle="-",markersize=10)
'''
