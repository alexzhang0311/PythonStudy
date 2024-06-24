import pandas as pd

#A DataFrame is a table
pd1 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(pd1)

pd2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(pd2)

#The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructo

pd3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

#Series
#A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. 

se1 = pd.Series([1, 2, 3, 4, 5])
print(se1)

#A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name

se2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(se2)

#Read
#To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
wine_reviews = pd.read_csv("E:/code/frontend/frontend/AIOPS/train.csv",index_col=0)

print(wine_reviews.shape) #1460 Rows 81 Columns

# print(wine_reviews.head())
print(wine_reviews.head().MSSubClass)
print(wine_reviews.MSSubClass.head())
print(wine_reviews['LotFrontage'].head())

#Write
# pd3.to_csv("./pd3.csv")

#iloc & loc
#row-first, column-second

#index-based selection
print(wine_reviews.iloc[0:5,0])
print(wine_reviews.iloc[[0,1,2,3,4],0])
#label-based selection
print(wine_reviews.loc[0:5,'MSSubClass'])
#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.


print(wine_reviews.set_index("MSSubClass").head(5))

#Conditional selection
nb = wine_reviews.MSSubClass == 60
print(nb) #return result with bool type

wb = wine_reviews.loc[wine_reviews.MSSubClass > 60]
print(wb)

qb = wine_reviews.loc[(wine_reviews.MSSubClass > 60) & (wine_reviews.YrSold >= 2010)]
print(qb)

eb = wine_reviews.loc[(wine_reviews.MSSubClass > 60) | (wine_reviews.YrSold >= 2010)]
print(eb)

rb = wine_reviews.loc[wine_reviews.Street.isin(["Grvl"])]
print(rb)

tb = wine_reviews.loc[wine_reviews.Alley.notnull()]
print(tb)

#Assigning data
# wine_reviews['SaleType'] = 'Saled'
# print(wine_reviews)

# wine_reviews['index_backwards'] = range(len(wine_reviews),0,-1)
# print(wine_reviews)

#查看某一列的特征数据
print(wine_reviews.SaleType.describe())
#查看某一列中去重之后的数据
print(wine_reviews.SaleType.unique())
#查看某一列中去重之后的数据，以及出现次数
print(wine_reviews.SaleType.value_counts())
#排序
print(wine_reviews.sort_values('SaleType'))

for i,j in wine_reviews.SaleType.value_counts().items():
    print(i,j)

#rename

wine_reviews = wine_reviews.rename(columns={'MSSubClass':'msSubClass'})
wine_reviews = wine_reviews.rename(index={1:'一',2:"二"})
print(wine_reviews)

wine_reviews = wine_reviews.rename_axis("行号",axis="rows").rename_axis("列名",axis="columns")
print(wine_reviews.iloc[[0,1],0:5])

#combine
#with same columns
head2 = wine_reviews.iloc[:2,[0,1]]
tail2 = wine_reviews.iloc[-4:,[0,1]]
head4 = wine_reviews.iloc[:4,[0,1]]
# print(head2)
# print(tail2)
comBin = pd.concat([head2,tail2])
print(comBin)

#combine with index

idxBin = head2.join(head4,lsuffix='_H', rsuffix='_T')
print(idxBin)

#map
# print(wine_reviews.msSubClass.max())
# msSubClass 为190的房子价格与其平均价格的差值
BigClass = wine_reviews.loc[(wine_reviews.msSubClass == 190)]
priceMean = BigClass.SalePrice.mean()
# print(priceMean)
print(BigClass.SalePrice.map(lambda p: p - priceMean))

#apply
###axis='columns' 针对每一行数据进行操作，将SalePrice的数据减去价格平均值
def meanSales(row):
    row.SalePrice = row.SalePrice - priceMean
    return row

new_wine_reviews = BigClass.apply(meanSales,axis='columns')
print(new_wine_reviews.sort_values(by='SalePrice', ascending=True))


###axis='index' 针对每一列的所有数据进行操作;将'MSZoning','MSZoning','SaleCondition'列数据加上一个MSZoning
MSZoning = BigClass.MSZoning
def meanSalesindex(index):
    return index + '-' + MSZoning

old_wine_reviews = BigClass.loc[:,['MSZoning','MSZoning','SaleCondition']].apply(meanSalesindex,axis='index')
print(old_wine_reviews)


def filte(row):
    if row.SaleCondition != 'Normal':
        return row

print(wine_reviews.apply(filte,axis='columns'))

print(wine_reviews.SaleCondition.map(lambda row:row !='Normal').sum())


###group & sort
print(wine_reviews.groupby("YrSold").YrSold.count())
print(wine_reviews.YrSold.value_counts())


#You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data in any way we see fit
print(wine_reviews.groupby("YrSold").apply(lambda df:df.SalePrice.iloc[0]))
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))
print(reviews.groupby(['country']).price.agg(["len", "min", "max"]))
'''
        len	min	max
country			
Argentina	3800	4.0	230.0
Armenia	2	14.0	15.0
...	...	...	...
Ukraine	14	6.0	13.0
Uruguay	109	10.0	130.0
'''
countries_reviewed.reset_index()

countries_reviewed.sort_values(by='len', ascending=False)
countries_reviewed.sort_values(by=['country', 'len'])

###Data Type & Missing values

print(reviews.price.dtype)
#It's possible to convert a column of one type into another wherever such a conversion makes sense by using the astype() function
reviews.points.astype('float64')
reviews.index.dtype

###Missing Data
#Entries missing values are given the value NaN, short for "Not a Number". For technical reasons these NaN values are always of the float64 dtype.

reviews[pd.isnull(reviews.country)]

#replace missin values
reviews.region_2.fillna("Unknown")

#non-null value replace
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")


###Raname & Combining

#change cloumn name from "points" to "score"
reviews.rename(columns={'points': 'score'})

#change index name from '0' to 'firstEntry' and '1' to 'secondEntry'