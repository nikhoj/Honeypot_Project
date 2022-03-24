import random
import numpy as np
import pandas as pd 


class Project:

    def __init__(self, name, val):
        self.name = name
        self.val = val


class Honeypot:

    def __init__(self, name, val):
        self.name = name
        self.val = val
        


class Attacker:

    def __init__(self, tools, alpha = 'Null' , perception_detection_prob = 'Not Given'): 
        
        self.tools = tools
        self.alpha = alpha
        self.perception_detection_prob = perception_detection_prob
        
     
     
    def util_for_attack (self, item):
        
        if self.alpha != 0:
            return (1-np.exp(-1 * self.alpha * item))/self.alpha
        else:
            return item

    def sequence(self, projects, honeypots):
        combine_projects = projects + honeypots
        #print(combine_projects[0])
        
        if self.alpha == "Null":
            random.shuffle(combine_projects)
            return combine_projects
        
        else:
            
            
            dict = {}
            if self.perception_detection_prob == 'Not Given':
                
                for p in combine_projects:                    
                
                    prob = np.random.rand()
                    
                    dict[p] = self.util_for_attack(p.val) * (1 - prob)
                
            else:
                
                for p in combine_projects:
                
                    prob = self.perception_detection_prob[p]
                    dict[p] = self.util_for_attack(p.val) * (1 - prob)
            
            df =  pd.DataFrame(dict.items(), columns=('Project', 'exp_utility')).sort_values(by = ['exp_utility']).reset_index().drop(["index"], axis=1)
            return df['Project'].tolist()
                
            
        
            
        


class Defender:

    def __init__(self, budget):
        self.budget = budget

    def cost_to_build(self, honeypots=0, costs=0):
        dict = {}
        l = len(honeypots)
        
        if costs != 0:
            for i in range(l):
                dict[honeypots[i]]: costs[i]
        else:
            for i in range(l):
                dict[honeypots[i]] = int(np.random.randint(50, 100, 1, dtype=int))

        return dict
    
    def prob_to_get_attack(self, projects, honeypots, probs_projects=0, probs_honeypots=0):
        dict = {}
        combine_projects = projects + honeypots
        
        l = len(combine_projects)
        
        if probs_projects != 0:
            for i in range(l):
                combine_probs = probs_projects + probs_honeypots
                dict[combine_projects[i]] = combine_probs[i]
        else:
            for i in range(l):                
                dict[combine_projects[i]] = np.random.rand()

        return dict
