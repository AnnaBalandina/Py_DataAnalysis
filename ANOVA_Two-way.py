import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt

data = d=pd.read_excel('D:/AnnaB/AUI-97/All_2_AUI-97_24h.xlsx',index_col=None)
d_melt = pd.melt(d, id_vars=['time'], value_vars=['k', 'c_3', 'c_4', 'c_5', 'c_10', 'c_25', 'c_50', 'c_100', 'c_200', 'c_300', 'c_400', 'c_500'])
d_melt.columns = ['time', 'Conc', 'value']
d_melt.head()

# ANOVA
formula = 'value~C(Conc)+C(time)+C(Conc):C(time)'
model = ols(formula, d_melt).fit()
aov_table = anova_lm(model, typ=2)

print(aov_table)
aov_table.to_excel(r'D:/AnnaB/AUI-97/Results_of_Analisis/Anova_TwoFactor_AUI-97!!!.xlsx', index = False)

res = model.resid 
fig = sm.qqplot(res, line='s')
plt.show()

#Create a boxplot
d=pd.read_excel('D:/AnnaB/AUI-97/All_2_AUI-97_24h.xlsx',index_col=None)
d_melt = pd.melt(d, id_vars=['time'], value_vars=['k',  'c_3', 'c_4', 'c_5', 'c_10', 'c_25', 'c_50', 'c_100', 'c_200', 'c_300', 'c_400', 'c_500'])
d_melt.columns = ["Time_of_Exposition_AUI-97", "Concentration_of_AUI-97", "Values_of_Survival"]
d_melt.head()

print(d_melt)
sns.boxplot(x="Concentration_of_AUI-97", y="Values_of_Survival", hue="Time_of_Exposition_AUI-97", data=d_melt, palette="Set2",fliersize=3,whis=1) 

