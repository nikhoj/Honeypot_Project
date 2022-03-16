import numpy as np
import pandas as pd
from data_structures import Project, Honeypot, Attacker, Defender

# data Preparation
russia = Attacker(tools=4)
ukraine = Defender(budget=1000)

l1 = 10  # len of projects
l2 = 8  # len of honeypots

armored_tank = []   # projects
air_defense = []    # Honeypots

for i in range(l1):
    name = 'AT' + str(np.random.randint(10000, 99999))
    armored_tank.append(Project(name, int(np.random.randint(50, 200, 1))))

for i in range(l2):
    name = 'AD' + str(np.random.randint(10000, 99999))
    air_defense.append(Honeypot(name, int(np.random.randint(50, 200, 1))))

# Algorithm start here

seq = russia.sequence(projects=armored_tank, honeypots=air_defense)  # sequence initializer


# dataFrame initialization

CP_list = []  # cumulative probability list, used as column name
for i in range(russia.tools + 1):
    CP_list.append('P' + str(i))
df_column = ['artillery'] + CP_list + ['exp_loss', 'invested_amt']

df = pd.DataFrame(np.zeros((1, russia.tools + 4)), columns=df_column)   # container
df.iloc[0, 1] = 1   # Initially the probability of losing less than or equal to 0 tool is 1
print(df)


for attack in seq:
    if attack in armored_tank:
        pass
    else:
        pass


