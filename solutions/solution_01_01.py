
# 1. Select towns with less than 1000 inhabitants, or with more than 1 Foreigner. How many such towns are there?


mask=( df['Total']<1000 ) | ( df['Foreigner']>0 ) 
print( "there are" ,mask.sum() , "towns with less than 1000 inhabitants, or more than 1 Foreigner." )
# applying sum on a set of False/True make them behave like 0/1. Thus the sum is the number of True.


#2. Create a new column is the `DataFrame` representing the fraction of population which is Reformed in each town.


df['fraction reformed'] = df['Reformed']/df['Total']
print( df['fraction reformed'].head()  )

# optional : What is the minimum/maximum value for this fraction?

print( 'minimum:' , df['fraction reformed'].min())
print( 'maximum:' , df['fraction reformed'].max())

