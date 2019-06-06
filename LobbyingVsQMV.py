# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:09:09 2019

@author: Ali Abdoli
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from datetime import date, timedelta

pd.set_option('display.max_columns', 500)
lobbies = pd.read_csv('./Communications_OCL_CAL/Communication_PrimaryExport.csv')
lobbies = lobbies[['EN_CLIENT_ORG_CORP_NM_AN']][lobbies['POSTED_DATE_PUBLICATION'] >= str((date.today() - timedelta(days=365)))]
lobbies = lobbies['EN_CLIENT_ORG_CORP_NM_AN'].value_counts()
lobbies = lobbies.rename_axis('Name').reset_index(name='count')

marketCap = pd.read_excel('./mig_report.xlsx')
marketCap = marketCap[['Name','QMV($)']]
data = pd.merge(lobbies, marketCap, on='Name')
plt.scatter(data['count'], data['QMV($)'])
slope, intercept, r_value, p_value, std_err = stats.linregress(data['count'], data['QMV($)'])
yfit = [intercept + slope * xi for xi in data['count']]
plt.plot(data['count'], yfit)
plt.suptitle('Plot of Lobbying Efforts vs Qutoed Market Value')
plt.xlabel('Lobbying Efforts')
plt.ylabel('Quoted Market Value (CAD)')
plt.savefig('scatter.png', dpi=1200)
print(r_value**2)
print(intercept)
print(slope)
