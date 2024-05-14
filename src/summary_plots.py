import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import integrate

import os
import glob

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

os.chdir('../data')
print("File location using os.getcwd():", os.getcwd())

#sns.color_palette()
colour=[(1,1, 1),
 (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
 (1.0, 0.4980392156862745, 0.054901960784313725),
 (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
 (0.5803921568627451, 0.403921568627451, 0.7411764705882353),
 (0.09019607843137255, 0.7450980392156863, 0.8117647058823529),
 (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
 (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
 (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
 (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
 (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
 (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)]
sns.set_palette(colour)
sns.palplot(colour) 
#plt.show()

def plot_freq_wks(data, colour):
    sns.set_palette(colour[3:]) #change starting colour
    fig, ax = plt.subplots(figsize=(4, 4))
    fig.suptitle('Freq per min', fontsize=24)
    # ax=df.boxplot(grid=False, showfliers=False)
    # ax=sns.stripplot(data=df, jitter=True, marker='o', alpha=0.7, size=8 ,color='grey')
    ax=sns.boxplot(data=cell, showfliers=False)
    ax.set_ylim([0, 3])
    ax.set_yticks([1,2,3])

#fig.savefig('C:/Users/Tony Kelly/Desktop/Worms_freq.svg', bbox_inches = 'tight', format="svg",transparent=True)   

#fig.savefig(desktop +'/GECI_freq.svg', bbox_inches = 'tight', format='svg')


def plot_freq_wks(data, colour):
freq_ExTime = pd.read_excel ('Freq_GECI.xlsx', sheet_name='Sheet2')

sns.set_palette(colour[4:])

fig, ax = plt.subplots(figsize=(4, 4))
fig.suptitle('Freq per min', fontsize=24)
# ax=df.boxplot(grid=False, showfliers=False)
# ax=sns.stripplot(data=df, jitter=True, marker='o', alpha=0.7, size=8 ,color='grey')
ax=sns.boxplot(data=freq_ExTime.drop(['animal_id'], axis=1), showfliers=False)

freq_ExTime.mean()

df=freq_ExTime

from scipy.stats import ranksums, wilcoxon, kruskal, mannwhitneyu, dunnett, f_oneway, normaltest, ttest_ind, ttest_rel
F_value, p = f_oneway(df['2wks'].dropna(), df['4wks'].dropna(), df['>8wks'].dropna()) #parametic 
F_value, p = f_oneway(df['4wks'].dropna(), df['>8wks'].dropna()) #parametic 
t_value, p = ttest_rel(df['4wks'].dropna(), df['>8wks'].dropna()) #parametic 

h_value, p = kruskal(df['2wks'].dropna(), df['4wks'].dropna(), df['>8wks'].dropna())
     
u_value, p = dunnett(np.array(df['4wks'].dropna()), np.array(df['>8wks'].dropna()), control=np.array(df['2wks'].dropna()))


wk2=np.array(df['2wks'].dropna())
wk4=np.array(df['4wks'].dropna())
wk8=np.array(df['>8wks'].dropna())
tbl=dunnett(wk4,wk8, control=wk2)

u_value, p = mannwhitneyu(df['2wks'].dropna(), df['>8wks'].dropna())
u_value, p = mannwhitneyu(df['4wks'].dropna(), df['>8wks'].dropna())
u_value, p = mannwhitneyu(df['2wks'].dropna(), df['4wks'].dropna())
u_value, p = mannwhitneyu(df['2wks'].dropna(), df['>8wks'].dropna())
u_value, p = mannwhitneyu(df['4wks'].dropna(), df['>8wks'].dropna())

sys.path.append('//10.10.20.24/messdaten/Tony/codes/python/stats/')
from df_anova import restruct,stats_anova, stats_anova1

df = restruct(freq_ExTime.drop(['animal_id'], axis=1))
stats_anova1(df, 'variable', 'condition')