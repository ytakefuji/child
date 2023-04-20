import pandas as pd
import matplotlib.pyplot as plt
import subprocess as sp
sp.call('wget -nc https://data.cdc.gov/api/views/chcz-j2du/rows.csv', shell=True)
d=pd.read_csv('rows.csv')
years=d.Year.unique()
a1=[]
a2=[]
for i in years:
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='0 years'),'Total Deaths']
 a1.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='1-4 years'),'Total Deaths']
 a2.append(a)
 plt.ylim([0,25000])
plt.plot(years,a1,':k')
plt.plot(years,a2,'-k')
plt.legend(('0 years','1-4years'))
plt.title('Impact of COVID-19 on mortality of children')
plt.savefig('child.jpg',dpi=300)
plt.show()

