import numpy as np
import pandas as pd
from data_structures import Project, Honeypot, Attacker, Defender
import time
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def runtest(tools, alpha_val, budget, plen, hlen, seed):
    np.random.seed(seed)
    # data Preparation
    russia = Attacker(tools=tools, alpha=alpha_val)
    ukraine = Defender(budget=budget)

    l1 = plen  # len of projects
    l2 = hlen  # len of honeypots

    armored_tank = []  # projects
    air_defense = []  # Honeypots

    for i in range(l1):
        name = 'AT' + str(np.random.randint(10000, 99999))
        armored_tank.append(Project(name, int(np.random.randint(50, 200, 1))))

    for i in range(l2):
        name = 'AD' + str(np.random.randint(10000, 99999))
        air_defense.append(Honeypot(name, int(np.random.randint(50, 200, 1))))

    prob_attack = ukraine.prob_to_get_attack(projects=armored_tank, honeypots=air_defense)
    cost_build = ukraine.cost_to_build(honeypots=air_defense)

    # Algorithm start here

    seq = russia.sequence(projects=armored_tank, honeypots=air_defense)  # sequence initializer

    CP_list = []  # cumulative probability list, used as column name
    for i in range(russia.tools + 1):
        CP_list.append('P' + str(i))
    df_column = ['h'] + CP_list + ['exp_loss', 'invested_amt']

    df = pd.DataFrame(np.zeros((1, russia.tools + 4)), columns=df_column)  # container
    df.iloc[0, 1] = 1  # Initially the probability of losing less than or equal to 0 tool is 1

    h = 0
    for attack in seq:
        h += 1
        # print('now working on h = {}'.format(h))
        temp_df = df[df.loc[:, 'h'] == h - 1]

        # temp_df = temp_df.reset_index()

        for row in range(len(temp_df)):

            temp = temp_df.iloc[row, :]
            temp[0] = h

            if attack not in armored_tank:

                # if its not touched by attacker
                if temp[-1] <= ukraine.budget:
                    df = df.append(temp, ignore_index=True)

                # if its touched by attacker
                psum = 0
                temp2 = temp.copy()
                for t in range(russia.tools):
                    calc = temp[t + 2] * (1 - prob_attack[attack]) + temp[t + 1] * prob_attack[attack]
                    psum += calc
                    temp2[t + 2] = calc

                temp2[1] = 1 - psum
                b = temp[-1]
                temp2[-1] = b + cost_build[attack]
                if temp2[-1] <= ukraine.budget:
                    df = df.append(temp2, ignore_index=True)

            else:

                psum = temp[1:-3].sum()

                temp[-2] = prob_attack[attack] * attack.val * psum + temp[-2]
                if temp[-1] <= ukraine.budget:
                    df = df.append(temp, ignore_index=True)

        # elimination of row start here
        elim_df = df[df.loc[:, 'h'] == h].sort_values(by=['invested_amt']).reset_index().drop(["index"], axis=1)
        df = df[df.loc[:, 'h'] != h]
        # if h == 5:
        #    break
        # print(elim_df)
        drop_list = set()
        alpha = .01
        beta = .5
        for i in range(len(elim_df) - 1):
            if elim_df.iloc[i, -3] > 0:
                for j in range(i + 1, len(elim_df)):
                    # print('comparing {} with {}'.format(i,j))
                    if round(elim_df.iloc[j, -3], 2) - alpha <= round(elim_df.iloc[i, -3], 2) <= round(
                            elim_df.iloc[j, -3], 2) + alpha:

                        # print('found')
                        if elim_df.iloc[i, -1] <= elim_df.iloc[j, -1]:
                            # elim_df = elim_df.drop([j]).reset_index().drop(["index"], axis=1)
                            # print(j)
                            drop_list.add(j)
                        else:
                            # elim_df = elim_df.drop([i]).reset_index().drop(["index"], axis=1)
                            # print(i)
                            drop_list.add(i)

                    if round(elim_df.iloc[j, -1]) - beta <= round(elim_df.iloc[i, -1]) <= round(
                            elim_df.iloc[j, -1]) + beta:

                        if elim_df.iloc[i, -3] <= elim_df.iloc[j, -3]:
                            # elim_df = elim_df.drop([j]).reset_index().drop(["index"], axis=1)
                            # print(j)
                            drop_list.add(i)
                        else:
                            # elim_df = elim_df.drop([i]).reset_index().drop(["index"], axis=1)
                            # print(i)
                            drop_list.add(j)

                        # print('found another')
                # print('here1')
        elim_df = elim_df.drop(list(drop_list)).reset_index().drop(["index"], axis=1)
        df = df.append(elim_df, ignore_index=True)
        # print(elim_df)

        if h == len(seq):
            result = elim_df['exp_loss'].min()
    r = 0
    for i in armored_tank:
        r += i.val
    rloss = result / r
    # one way is to check whether defender can maximize the probability of P_r with less budget/same budget
    print(
        'For {} project, {} honeypots, {} tool, where alpha = {}, the exp loss = {} and relative loss = {}'.format(plen,
                                                                                                                   hlen,
                                                                                                                   tools,
                                                                                                                   alpha_val,
                                                                                                                   result,
                                                                                                                   rloss))
    # for i in range(len(armored_tank)):
    #    print(armored_tank[i].name)
    return rloss


N = 50
# timedict = {}
# elossdict_compare = {}
tool, hpots, alpha, rloss = [], [], [], []

for n in range(N):
    print('running iteration number {}'.format(n))

    for pk in [2,4,6,8]:  # number of tools

        for p2 in [25]:  # number of honeypot

            for b in [-.5, 0, .5]:  # attacker type

                try:

                    # start_time = time.time()
                    result = runtest(pk, b, 10000, 100, p2, n)
                    # end_time = time.time()
                    # timedict[p1,p2,p3] =( (end_time - start_time) + timedict[p1,p2,p3] )/ 2
                    # elossdict[p1,p2,p3] = result
                    # elossdict_compare[pk, p2, p3, n] = result
                    # print('runtime: {}'.format(end_time-start_time))

                except:

                    # timedict[p1,p2,p3] = 0
                    # start_time = time.time()
                    result = runtest(pk, b, 10000, 100, p2, n)
                    # end_time = time.time()
                    # timedict[p1,p2,p3] =( (end_time - start_time) + timedict[p1,p2,p3] )/ 2
                    # elossdict[p1,p2,p3] = result
                    # elossdict_compare[pk, p2, p3, n] = result
                tool.append(pk)
                hpots.append(p2)
                alpha.append(b)
                rloss.append(result)

    record_50_10000 = np.column_stack([hpots, tool, alpha, rloss])
    np.savetxt("record_100_10000_{}.csv".format(p2), record_50_10000)
# print(elossdict_compare)
# with open("runtime.txt", 'w') as f:
#   for key, value in timedict.items():
#      f.write('%s:%s\n' % (key, value))

# with open("eloss_compare.txt", 'w') as f:
#    for key, value in elossdict_compare.items():
#        f.write('%s:%s\n' % (key, value))
