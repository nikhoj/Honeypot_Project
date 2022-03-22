import numpy as np
import pandas as pd
from data_structures import Project, Honeypot, Attacker, Defender

# data Preparation
russia = Attacker(tools=1)
ukraine = Defender(budget=1000)

l1 = 2  # len of projects
l2 = 1  # len of honeypots

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

CP_list = []  # cumulative probability list, used as column name
for i in range(russia.tools + 1):
    CP_list.append('P' + str(i))
df_column = ['artillery'] + CP_list + ['exp_loss', 'invested_amt']

df = pd.DataFrame(np.zeros((1, russia.tools + 4)), columns=df_column)   # container
df.iloc[0, 1] = 1   # Initially the probability of losing less than or equal to 0 tool is 1



for attack in seq:
    df2 = df.copy()
    for row in range(len(df2)):
        temp = df2.iloc[row,:].to_frame()
        
    
        #print(temp)
        
        if attack not in armored_tank:
            #print( 'it is not a armored tank')
            
            # if the honey was not touched
            #df = df.append(temp, ignore_index=True)
            df = pd.concat([df,temp.T], ignore_index = True)
            df.iloc[-1,0] = attack.name
            print(df)
            break
            
            
            #if the honeypot is touched by the attacker
            for i in range(russia.tools+1):
                if i != 0:
                    temp.iloc[i+1,0] = temp.iloc[i+1,0] *(1 - prob_attack[attack]) + temp.iloc[i,0] * prob_attack[attack]
                else:
                    temp.iloc[i+1,0] = temp.iloc[i+1,0] *(1 - prob_attack[attack])
            
            temp.iloc[-1,0] = temp.iloc[-1,0] + cost_build[attack]
            df = df.append(temp, ignore_index=True)
            df.iloc[-1,0] = attack.name
            
            
            
        else:
            #print(' is a armored tank')
            
            p_temp = temp.iloc[1:-3,0].sum()
                
            temp.iloc[-2,0] = prob_attack[attack] * attack.val * p_temp + temp.iloc[-2,0]
            df = df.append(temp, ignore_index=True)
            df.iloc[-1,0] = attack.name
        
           
    '''
    #eliminate all the dominated states
    lr = len(df) - 1        #last row
    print(lr)
    for i in range(lr,0,-1):
        
        if df.iloc[i,0] == attack.name:
            
            for j in range(i-1,0,-1):
                if df.iloc[j,0:-1].equals(df.iloc[i,0:-1]):
                    
                    
                    
                    if df.iloc[j,-1] < df.iloc[i,-1]:
                        df = df.drop(labels = i)    # j dominates i
                        #df = df.reset_index()
                    else:
                        df = df.drop(labels = j)    # i dominates j
                        #df = df.reset_index()
                    
                elif df.iloc[j,0] != attack.name:
                    break
        else:
            break
        '''
                    
                    
            
