import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

g_dist = stats.gamma(a=2)
print('quantiles of 2, 4, 5:')
print(g_dist.cdf([2, 4, 5]))
print('Values of 25%, 50%, and 90%:')
print(g_dist.pdf([0.25, 0.5, 0.9]))

stats.norm.moment(6, loc=0, scale=1)

norm_dist = stats.norm(loc=0, scale=1.8)
dat = norm_dist.rvs(size=100)
info = stats.describe(dat)
print(info)

mu, sigma =stats.norm.fit(dat)
print('MLE of data:' + str(mu) + ' ' + str(sigma))

dat1 = norm_dist.rvs(size=100)
exp_dist = stats.expon()
dat2 = exp_dist.rvs(size=100)
cor, pval =stats.pearsonr(dat1, dat2)
print('Pearson correlation coefficient: ' + str(cor))
cor, pval = stats.spearmanr(dat1, dat2)
print('Spearman correlation coefficient: ' + str(cor))

x = stats.chi2.rvs(3, size=50)
y = 2.5 + 1.3 * x + stats.norm.rvs(size=50, loc=0, scale=1.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(slope, intercept, r_value, p_value, std_err)

