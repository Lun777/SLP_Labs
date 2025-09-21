import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline

a = pd.read_csv("test.csv")
print(a)
Nan = a.isnull().sum()
print(a.groupby(a["Rooms"]).agg(len))
print(Nan)
print(a[a['LifeSquare'].isnull()])
plt.plot(a["Id"], a["Square"])
plt.yscale(value="log")
plt.show()
plt.boxplot(x = a['HouseYear'])
plt.show()
a = a[a["HouseYear"] >= 1933]
plt.boxplot(x = a['HouseYear'])
plt.show()
plt.boxplot(x = a['HouseFloor'])
plt.show()
a = a[a["HouseFloor"] <= 29]
plt.boxplot(x = a['HouseFloor'])
plt.show()
a["LifeSquare"] = a['LifeSquare'].fillna(3.14 * a["Square"])
a["Healthcare_1"] = a['Healthcare_1'].fillna(a['Helthcare_2'])
Nan = a.isnull().sum()
print(Nan)
b = a.pivot_table(a, index = a["DistrictId"], columns = a["Rooms"], aggfunc = len, fill_value = 0)
print(b)
print(a)