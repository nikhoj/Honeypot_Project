import numpy as np
import pandas as pd
from data_structures import Project, Honeypot, Attacker, Defender

# data Preparation
russia = Attacker(tools=3)
ukraine = Defender(budget=1000)

l1 = 5  # len of projects
l2 = 5  # len of honeypots

armored_tank = []   # projects
air_defense = []    # Honeypots

for i in range(l1):
    name = 'AT' + str(np.random.randint(10000, 99999))
    armored_tank.append(Project(name, int(np.random.randint(50, 200, 1))))

for i in range(l2):
    name = 'AD' + str(np.random.randint(10000, 99999))
    air_defense.append(Honeypot(name, int(np.random.randint(50, 200, 1))))


prob_attack = russia.prob_to_attack(projects = armored_tank, honeypots = air_defense)
cost_build = ukraine.cost_to_build(honeypots=air_defense)



# Algorithm start here

seq = russia.sequence(projects=armored_tank, honeypots=air_defense)  # sequence initializer


# dataFrame initialization
#F = {0 : [0] * (russia.tools + 4)}
#for h in range(1,l1 + l2 + 1):
 #   if seq[h] in armored_tank:
  #      F[h] = [F[h-1], F[h-1]]
        
        
CP_list = []  # cumulative probability list, used as column name
for i in range(russia.tools + 1):
    CP_list.append('P' + str(i))
df_column = ['h'] + CP_list + ['exp_loss', 'invested_amt']

df = pd.DataFrame(np.zeros((1, russia.tools + 4)), columns=df_column)   # container
df.iloc[0, 1] = 1   # Initially the probability of losing less than or equal to 0 tool is 1


h = 0
for attack in seq:
    h += 1
    temp_df = df[df.loc[:,'h'] == h-1]
    
    #temp_df = temp_df.reset_index()
    
    for row in range(len(temp_df)):
        
        temp = temp_df.iloc[row,:]        
        temp[0] = h        
        
        if attack not in armored_tank:
            
            #if its not touched by attacker
            df = df.append(temp , ignore_index = True)
            
            #if its touched by attacker
            psum = 0
            temp2 = temp.copy()
            for t in range(russia.tools):
                
                calc = temp[t+2] *(1 - prob_attack[attack]) + temp[t+1] * prob_attack[attack]
                psum += calc
                temp2[t+2] = calc
                
            temp2[1] = 1 - psum
            b = temp[-1]
            temp2[-1] = b + cost_build[attack]
            df = df.append(temp2, ignore_index = True)
            
        else:
            psum = temp[1:-3].sum()
                
            temp[-2] = prob_attack[attack] * attack.val * psum + temp[-2]
            df = df.append(temp, ignore_index=True)
