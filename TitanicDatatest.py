import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 1000)#不换行输出
TData=pd.read_excel('/Users/yiliu/lllyeeData/titanic.xls')
#TData.info()
#print(TData.head())#前5行数据
print(TData.describe())
SurvivalRate=round((100*TData['survived'].sum())/TData['survived'].count(),2)
print('Titanic数据集共有{}条成员记录，有{}个成员生还，总体生还率为{}%'.format(TData['survived'].count(),TData['survived'].sum(),SurvivalRate))
#TData.groupby('survived')['survived'].count().plot(kind='bar')#groupby 聚合运算  bar:条形图 barh:横向条形图
#data.plot(kind='bar')
#TData.groupby('pclass')['name'].count().plot(kind='bar')
#print(TData.groupby('pclass')['name'].count())
#sns.factorplot('sex',data=TData,kind='count')
#plt.show()
#print(TData[TData['age'].isnull()])
#TData['age'].hist(bins=80,color='g')#bins指有多少个条状图 参考"https://blog.csdn.net/u013230234/article/details/75451833"
print("均值",TData['age'].mean())
print("中位数",TData['age'].median())
print("最大值",TData['age'].max())
print("最小值",TData['age'].min())
print("标准差",TData['age'].std())
#船票价格分布
#TData['fare'].hist(bins=40)

TData.groupby(TData['embarked'])['name'].count()
plt.show()