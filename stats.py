import matplotlib.pyplot as plt

bar = [633471.0, 23874171.0]
plt.title("Pie")
plt.pie(bar, labels=[ "Deaths", "Recoveries"], explode=[0,0.1], shadow=True, autopct="%1.1f%%")
plt.tight_layout()
plt.show()