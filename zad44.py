import pandas as pd
import matplotlib
url = "miasta.csv"

df = pd.read_csv(url)

print(df)

data = {2010,460,555,405}
# dataframe from dictionary
df2 = pd.DataFrame(data)

#df.to_csv('miasta.csv', mode='a', index=False, header=False)
fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(array[:, 0], array[:, 1])
axs[0].set(ylabel='$f(x)=x^2$')
axs[1].plot(array[:, 0], array[:, 2])
axs[1].set(xlabel='$x$', ylabel='$f(x)=x^3$')
