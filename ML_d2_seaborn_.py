
import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
# print(tips.head())
# print(tips.describe())
# sns.distplot(tips['total_bill'])
# sns.distplot(tips['total_bill'],kde=False,bins=30)

# sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')

# sns.pairplot(tips)
# sns.pairplot(tips,hue='sex',palette='coolwarm')

# sns.kdeplot(tips['total_bill'])
# sns.rugplot(tips['total_bill'])

# sns.barplot(x='sex',y='total_bill',data=tips,estimator=sum)
# sns.barplot(x='sex',y='tip',data=tips,estimator=max)

# sns.countplot(x='smoker',data=tips)
# sns.countplot(x='day',data=tips)
# sns.countplot(x='time',data=tips)

# sns.boxplot(x='day',y='total_bill',data=tips)
# sns.boxplot(data=tips,orient='h')
# sns.boxplot(x='day',y='total_bill',hue='smoker',data=tips)

# sns.violinplot(x='day',y='total_bill',data=tips)
# sns.violinplot(x='day',y='total_bill',data=tips,hue='sex')
# sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True,palette='Set1')

# sns.stripplot(x='day',y='total_bill',data=tips)
# sns.stripplot(x='day',y='total_bill',data=tips,jitter=False)
# sns.stripplot(x='day',y='total_bill',data=tips,jitter=False,hue='sex')

# sns.swarmplot(x='day',y='total_bill',data=tips)
# sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex',dodge='False')

sns.violinplot(x='tip',y='day',data=tips)
sns.swarmplot(x='tip',y='day',data=tips,color='Black',size=3)

# sns.catplot(x='sex',y='total_bill',data=tips,kind='bar')

plt.show()

