import numpy as np
import csv
from data_structures import Project, Honeypot, Attacker, Defender

# data Preparation


def data_generator(tools, budget, project_num, honeypot_num):
    
    #russia = Attacker(tools=tools)
    #ukraine = Defender(budget=budget)
    
    armored_tank = []   # projects
    air_defense = []    # Honeypots
    
    for i in range(project_num):
        name = 'AT' + str(np.random.randint(10000, 99999))
        armored_tank.append(Project(name, int(np.random.randint(50, 200, 1))))
    
    for i in range(honeypot_num):
        name = 'AD' + str(np.random.randint(10000, 99999))
        air_defense.append(Honeypot(name, int(np.random.randint(50, 200, 1))))
    
    
    #prob_attack = russia.prob_to_attack(projects = armored_tank, honeypots = air_defense)
    #cost_build = ukraine.cost_to_build(honeypots=air_defense)
    
    i = 100    
    # name of csv file 
    filename = "projects_{}.csv".format(i)
    
    #column name
    column = ['project' , 'value']
    
    # writing to csv file 
    with open(filename, 'w', newline = '') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(column) 
        
        tmp = []
        # writing the data rows
        for item in armored_tank:
            tmp.append([item.name, item.val])
            
        csvwriter.writerows(tmp)
        
    

data_generator(0,0,5,5)
