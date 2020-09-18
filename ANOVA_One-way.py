import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Import 
data=pd.read_excel('D:/AnnaB/AUI-97/MTT BT-20_48h AUI-97_26.03.xls',index_col=0)
X = data.loc[8:23,"k":"c_500"]
#Y = data.loc[0:23,"time"]
X.head(35)

#Rename columns & create boxplot 
X.columns=['Control','3_μg/ml','4_μg/ml','5_μg/ml','10_μg/ml','25_μg/ml','50_μg/ml','100_μg/ml','200_μg/ml','300_μg/ml','400_μg/ml','500_μg/ml']
X.boxplot(column=['Control','3_μg/ml','4_μg/ml','5_μg/ml','10_μg/ml','25_μg/ml','50_μg/ml','100_μg/ml','200_μg/ml','300_μg/ml','400_μg/ml','500_μg/ml'], grid=False, rot=45)

# F & P factor
f, p = stats.f_oneway(X['Control'], X['3_μg/ml'], X['4_μg/ml'], X['5_μg/ml'],X['10_μg/ml'],X['25_μg/ml'],X['50_μg/ml'],X['100_μg/ml'],X['200_μg/ml'],X['300_μg/ml'],X['400_μg/ml'],X['500_μg/ml'])
print(f,p)

d_melt = pd.melt(X.reset_index(), id_vars=['index'], value_vars=['Control','3_μg/ml','4_μg/ml','5_μg/ml','10_μg/ml','25_μg/ml','50_μg/ml','100_μg/ml','200_μg/ml','300_μg/ml','400_μg/ml','500_μg/ml'])
# replace column names
d_melt.columns = ['index', 'Concentration', 'value']
# Ordinary Least Squares (OLS) model
model = ols('value ~ C(Concentration)', data=d_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table

#Export of table
anova_table.to_excel(r'D:/AnnaB/AUI-97/Results_of_Analisis/Anova_AUI-97_24h_Conc(3-500μg_ml)!!!!.xlsx', index = False)
