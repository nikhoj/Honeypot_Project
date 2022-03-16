import random
import numpy as np


class Project:

    def __init__(self, id, val):
        self.id = id
        self.val = val


class Honeypot:

    def __init__(self, id, val):
        self.id = id
        self.val = val


class Attacker:

    def __init__(self, tools, cls="random"):
        self.cls = cls
        self.tools = tools

    def prob_to_attack(self, projects, honeypots, probs_projects=0, probs_honeypots=0):
        dict = {}
        combine_projects = list(projects.keys()) + list(honeypots.keys())
        combine_probs = probs_projects + probs_honeypots
        l = len(combine_projects)
        if probs_projects != 0:
            for i in range(l):
                dict[combine_projects[i]] = combine_probs[i]
        else:
            for i in range(l):
                dict[combine_projects[i]] = np.random.rand()

        return dict

    def sequence(self, projects, honeypots):
        combine_projects = list(projects.keys()) + list(honeypots.keys())

        if self.cls == "random":
            random.shuffle(combine_projects)
            return combine_projects


class Defender:

    def __init__(self, budget):
        self.budget = budget

    def cost_to_build(self, honeypots=0, costs=0):
        dict = {}
        l = len(honeypots)

        if honeypots != 0:
            for i in range(l):
                dict[honeypots[i]]: costs[i]
        else:
            for i in range(l):
                dict[honeypots[i]]: int(np.random.randint(50, 100, 1, dtype=int))

        return dict
