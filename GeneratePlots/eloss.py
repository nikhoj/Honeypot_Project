import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# plot for 5 projects
df = pd.read_csv('5_Tools.csv')

x = df['Iternations_Num']
y = df['Expected Loss-S']
y1 = df['Expected Loss-A']
y2 = df['Expected Loss-N']

plt.subplot(1, 3, 1)
plt.title('k = 5, m = 15')
# plt.xlabel('Iteration')
plt.ylabel('Expected Loss')
#plt.axis([0, 11, 1500, 4000])
plt.scatter(x, y, label="Risk-Seeking", color="red", marker=".", s=20)
plt.scatter(x, y1, label="Risk-Averse", color="green", marker="^", s=10)
plt.scatter(x, y2, label="Risk-Neutral", color="blue", marker="s", s=10)
# plt.legend(loc="lower right", prop={'size': 5})
plt.xticks(x)
df = pd.read_csv('8_Tools.csv')

x = df['Iternations_Num']
y = df['Expected Loss-S']
y1 = df['Expected Loss-A']
y2 = df['Expected Loss-N']

plt.subplot(1, 3, 2)
plt.title('k = 8, m = 15')
plt.xlabel('Instance')
# plt.ylabel('Expected Loss')
#plt.axis([0, 11, 1500, 4000])
plt.scatter(x, y, label="Risk-Seeking", color="red", marker=".", s=20)
plt.scatter(x, y1, label="Risk-Averse", color="green", marker="^", s=10)
plt.scatter(x, y2, label="Risk-Neutral", color="blue", marker="s", s=10)
plt.xticks(x)
# plt.legend(loc="lower right", prop={'size': 5})

df = pd.read_csv('12_Tools.csv')

x = df['Iternations_Num']
y = df['Expected Loss-S']
y1 = df['Expected Loss-A']
y2 = df['Expected Loss-N']

plt.subplot(1, 3, 3)
plt.title('k = 12, m = 15')
#plt.xlabel('Iterations')
#plt.ylabel('Expected Loss')
#plt.axis([0, 11, 1500, 4000])
plt.scatter(x, y, label="Risk-Seeking", color="red", marker=".", s=20)
plt.scatter(x, y1, label="Risk-Averse", color="green", marker="^", s=10)
plt.scatter(x, y2, label="Risk-Neutral", color="blue", marker="s", s=10)
plt.xticks(x)
plt.legend(loc="lower right", prop={'size': 10})
'''
df = pd.read_csv('15_Tools.csv')

x = df['Iternations_Num']
y = df['Expected Loss-S']
y1 = df['Expected Loss-A']
y2 = df['Expected Loss-N']

plt.subplot(1, 4, 4)
plt.title('k = 15')
#plt.xlabel('Iterations')
# plt.ylabel('Expected Loss')
#plt.axis([0, 11, 1500, 4000])
plt.scatter(x, y, label="Risk-Seeking", color="red", marker=".")
plt.scatter(x, y1, label="Risk-Averse", color="green", marker="^", s=5)
plt.scatter(x, y2, label="Risk-Neutral", color="blue", marker="s", s=10)
plt.legend(loc="lower right", prop={'size': 10})
'''
plt.xticks(x)
plt.tight_layout()
plt.show()
