
import pandas as pd
import matplotlib.pyplot as plt
    
data = pd.read_csv('Notebooks/covid_19_data.csv')
df = pd.DataFrame(data)
df.rename(columns={ "ObservationDate":"timestamp","Province/State": "State", "Country/Region": "Country"}, inplace=True )
city_index = df[df["Country"]=="India"].index.values
deaths = df.loc[city_index, "Deaths"].values
recovered = df.loc[city_index, "Recovered"].values
plt.title("Covid19 visualization")
plt.xlabel("Deaths")
plt.plot(deaths, label="death")
plt.plot(recovered, label="recoveries")
plt.legend()
plt.show()

'''
timestamp = df.loc[city_index, "timestamp"].values
plt.title("covid19 visualization")
'''
