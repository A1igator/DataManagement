# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:09:09 2019

@author: Ali Abdoli
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

pd.set_option('display.max_columns', 500)
lobbies = pd.read_csv('./Communications_OCL_CAL/Communication_PrimaryExport.csv')
lobbies = lobbies[['EN_CLIENT_ORG_CORP_NM_AN']][lobbies['POSTED_DATE_PUBLICATION'] >= str((date.today() - timedelta(days=365)))]
lobbies = lobbies['EN_CLIENT_ORG_CORP_NM_AN'].value_counts()
lobbies = lobbies.rename_axis('Name').reset_index(name='count')

marketCap = pd.read_excel('./mig_report.xlsx')
marketCap = marketCap[['Name','QMV($)']]
data = pd.merge(lobbies, marketCap, on='Name')

plt.hist(data['QMV($)'], bins=7)
plt.suptitle('Quoted Market Value Histogram')
plt.xlabel('Quoted Market Value (CAD)')
plt.ylabel('Frequency')
plt.savefig('QMVHist.png', dpi=1200)
