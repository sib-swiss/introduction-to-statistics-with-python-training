
## first a little plot to meet the data
fig,axes = plt.subplots(1,2 , figsize=(14,7),  sharey=True )
sns.histplot(y=df['weightDiff'] , kde=True ,  ax = axes[0] )
sns.rugplot(y=df['weightDiff']  ,  ax = axes[0] )
sns.violinplot(x='Diet', y='weightDiff' , data=df, kind = 'violin' , ax = axes[1])
#  assumptions

# QQplots
fig,axes = plt.subplots(1,3 , figsize=(14,7),  sharey=True )
## there are 3 levels of diet: 1 2 and 3
for i,diet in enumerate( [1,2,3] ) :
    stats.probplot( df.loc[ df.Diet==diet , 'weightDiff'] , plot=axes[ i ] )
    axes[i].set_title("diet "+str(diet))

# using groupby we can apply the test function to each condition automatically :
print('Checking the assumptions of the anova:')
print('SW test of normality')
print( df.groupby('Diet')['weightDiff'].apply(stats.shapiro) )

# test of homoscedasticity :
print('Bartlett test of homoscedasticity')
print( stats.bartlett(df['weightDiff'][ df['Diet']==1 ], 
    df['weightDiff'][ df['Diet']==2 ],
    df['weightDiff'][ df['Diet']==3 ] ) )
# the assumptions seem verified, we can perform the test

Fstat , pval = stats.f_oneway( df['weightDiff'][ df['Diet']==1 ], 
    df['weightDiff'][ df['Diet']==2 ],
    df['weightDiff'][ df['Diet']==3 ] )
print('automated 1-way anova / F-test:')
print('F-stat :',Fstat)
print('p-value:',pval)

if pval < 0.05 :
    # statistical significance should be accompanied by actual effect size:
    print('Mean weightloss per group:')
    print( df.groupby('Diet')['weightDiff'].mean() )
