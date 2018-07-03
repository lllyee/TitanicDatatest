import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.width', 1000)#不换行输出
TData=pd.read_excel('/Users/yiliu/lllyeeData/titanic.xls')
#TData.info()
#print(TData.head())#前5行数据
print(TData.describe())
SurvivalRate=round((100*TData['survived'].sum())/TData['survived'].count(),2)
print('Titanic数据集共有{}条成员记录，有{}个成员生还，总体生还率为{}%'.format(TData['survived'].count(),TData['survived'].sum(),SurvivalRate))
#TData.groupby('survived')['survived'].count().plot(kind='bar')#groupby 聚合运算  bar:条形图 barh:横向条形图
#data.plot(kind='bar')
TData.groupby('pclass')['name'].count().plot(kind='bar')
#print(TData.groupby('pclass')['name'].count())
plt.show()
