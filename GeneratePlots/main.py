import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set_theme()

fname = 'myfile.txt'
data = pd.read_csv(fname, header=None)
data = data.rename(columns={0: "Projects", 1: "Honeypots", 2: "AttackerType", 3: "Runtime"})

X = [5, 10, 15]

# Grouped data for 5 projects
fiveP = data[data['Projects'] == 5]
fig, axs = plt.subplots(1, 3)

axs[0].plot(X, fiveP[fiveP['AttackerType'] == 0].Runtime, label="Risk-Neutral")
axs[0].plot(X, fiveP[fiveP['AttackerType'] < 0].Runtime, label="Risk-Seeking")
axs[0].plot(X, fiveP[fiveP['AttackerType'] > 0].Runtime, label="Risk-Averse")
axs[0].title.set_text('n = 5')

axs[0].set_ylabel('Runtime (sec)')
# Grouped data for 5 projects
tenP = data[data['Projects'] == 10]

axs[1].plot(X, tenP[tenP['AttackerType'] == 0].Runtime, label="Risk-Neutral")
axs[1].plot(X, tenP[tenP['AttackerType'] < 0].Runtime, label="Risk-Seeking")
axs[1].plot(X, tenP[tenP['AttackerType'] > 0].Runtime, label="Risk-Averse")
axs[1].set_xlabel('Number of Honeypots')
axs[1].title.set_text('n = 10')
# Grouped data for 5 projects
fifteenP = data[data['Projects'] == 15]

axs[2].plot(X, fifteenP[fifteenP['AttackerType'] == 0].Runtime, label="Risk-Neutral")
axs[2].plot(X, fifteenP[fifteenP['AttackerType'] < 0].Runtime, label="Risk-Seeking")
axs[2].plot(X, fifteenP[fifteenP['AttackerType'] > 0].Runtime, label="Risk-Averse")
axs[2].title.set_text('n = 15')
axs[2].legend()


plt.show()
