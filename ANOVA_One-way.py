import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Import 
data=pd.read_excel('D:/AnnaB/AUI-97/MTT BT-20_48h AUI-97_26.03.xls',index_col=0)
data.head(10)

#Create boxplot to visualize my data 
data.boxplot(column=['k','C_3','C_4', 'C_5','C_10','C_25','C_50','C_100','C_200','C_300', 'C_400','C_500'], grid=False, rot=45)

#ANOVA (ANalysis Of VAriance) test 
f, p = stats.f_oneway(data['k'], data['C_3'], data['C_4'], data['C_5'],data['C_10'],data['C_25'],data['C_50'],data['C_100'],data['C_200'],data['C_300'],data['C_400'],data['C_500'])
print(f,p)
d_melt = pd.melt(data.reset_index(), id_vars=['index'], value_vars=['k', 'C_3', 'C_4', 'C_5', 'C_10', 'C_25', 'C_50', 'C_100', 'C_200', 'C_300', 'C_400', 'C_500'])
# replace column names
d_melt.columns = ['index', 'treatments', 'value']
# Ordinary Least Squares (OLS) model
model = ols('value ~ C(treatments)', data=d_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table

#Export data to Excel 
anova_table.to_excel(r'D:/AnnaB/AUI-97/Anova_AUI-97_48h_Conc(3-500).xlsx', index = False)
