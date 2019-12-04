import numpy as np
import matplotlib.pylab as plt


#CODES FOR QUESTION1
"""
p_list = np.arange(0.1, 1.1, 0.1)
miu_list = [-10, -5, -1, 0, 1, 5, 10]

print(p_list)
miu1 = 0
sigma1 = 1
miu2 = 5
sigma2 = 1
l = []
p = 0.5
"""
"""
# with fixed miu and s sigma , we change the value of p 
for p in p_list:
    num_list = []
    for i in range(10000):
        X = np.random.normal(miu1, sigma1, 1)
        Y = np.random.normal(miu2, sigma2, 1)
        n = np.random.binomial(1, p)
        Z = X + n * Y
        num_list.append(Z[0])
    l.append(num_list)
plt.figure(figsize=(20, 10))
fig, ax = plt.subplots(2, 5)
ax = ax.flatten()
fig.set_figwidth(20)

for i, axis in enumerate(ax):
    axis.hist(l[i], bins=100, normed=True, color='b')
    axis.set_title("p = %.1f"%(p_list[i]))
    
    
plt.tight_layout()
plt.savefig('./fig_gaitong2.jpg')
"""

# figure out the influence of para: miu
"""
l_miu = []
fig, ax = plt.subplots(1, 7)
for miu_ in miu_list:
    tmp_list = []
    for i in range(10000):
        X = np.random.normal(miu1, sigma1, 1)
        Y = np.random.normal(miu_, sigma2, 1)
        n = np.random.binomial(1, p)
        Z = X + n * Y
        tmp_list.append(Z[0])
    l_miu.append(tmp_list)
ax = ax.flatten()
fig.set_figwidth(30)
for i, axis in enumerate(ax):
    axis.hist(l_miu[i], bins=100, normed=True, color='c')
    axis.set_title('miu2={}'.format(miu_list[i]))
plt.savefig('./fig_miu.jpg')
"""

#figure out the influence of sigma
"""
sigma_list = [0.1, 0.2, 0.5, 1, 2.5,  5]
l_sigma = []
for sig in sigma_list:
    tmp_list = []
    for i in range(10000):
        X = np.random.normal(0, sig, 1)
        Y = np.random.normal(10, 1, 1)
        n = np.random.binomial(1, p)
        Z = X + n * Y
        tmp_list.append(Z[0])
    l_sigma.append(tmp_list)

fig, ax = plt.subplots(1, 6)
ax = ax.flatten()
fig.set_figwidth(30)
for i, axis in enumerate(ax):
    axis.hist(l_sigma[i], bins=100, normed=True, color='r')
    axis.set_title('sigma={}'.format(sigma_list[i]))
plt.savefig('./fig_sigma(fixed2).jpg')
"""

#CODES FOR QUESTION2:
U_list = []
num = 1000
miu1, miu2 = 0, 5
sig1, sig2 = 1, 1
p = 0.5
l_all = []
l_All = []
number = 1000
for k in range(number):
    tmp_list = []
    for i in range(num):
        X = np.random.normal(miu1, sig1, 1)
        Y = np.random.normal(miu2, sig2, 1)
        n = np.random.binomial(1, p)
        Z = X + Y * n
        tmp_list.append(Z[0])
        l_All.append(Z[0])
    l_all.append(tmp_list)
np_Z = np.array(l_All)
mean = np_Z.mean()
var = np_Z.var()
for i in range(number):
#l_all[i]: 1 * n
    np_tmp = np.array(l_all[i])
    SUM = np_tmp.sum()
    U_new = (SUM - num * mean) / np.sqrt(num * var)
    U_list.append(U_new)

plt.hist(U_list, normed=True, bins=100)
plt.savefig('./Q2(%d).jpg' %(number))
print("finished calculations" + "--" * 5)