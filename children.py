import pandas as pd
import matplotlib.pyplot as plt
import subprocess as sp
sp.call('wget -nc https://data.cdc.gov/api/views/chcz-j2du/rows.csv', shell=True)
d=pd.read_csv('rows.csv')
years=d.Year.unique()
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
for i in years:
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='1-4 years'),'Total Deaths']
 a1.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='5-9 years'),'Total Deaths']
 a2.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='10-14 years'),'Total Deaths']
 a3.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='15-19 years'),'Total Deaths']
 a4.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='20-24 years'),'Total Deaths']
 a5.append(a)
 plt.ylim([0,32000])
plt.plot(years,a1,':k')
plt.plot(years,a2,'-k')
plt.plot(years,a3,'--k')
plt.plot(years,a4,'-.k')
plt.plot(years,a5,'-k',linewidth=3)
plt.legend(('1-4 years','5-9 years','10-14 years','15-19 years','20-24 years'),loc=2)
plt.title('Impact of COVID-19 on mortality of children & adolescents')
plt.savefig('child.jpg',dpi=300)
plt.show()

