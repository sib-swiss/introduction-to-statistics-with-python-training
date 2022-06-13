
#sns.pairplot(df)

corre=df.corr()
plt.figure(figsize=(5,5))
sns.heatmap(corre,cmap='plasma')
plt.title('correlations')
plt.show()

sns.violinplot(y='gender',x='height',data=df , color="0.8" )
sns.stripplot(y='gender',x='height',data=df , zorder=1 )
plt.show()

sns.violinplot(y='smoker_nonsmoker',x='height',data=df , color="0.8" )
sns.stripplot(y='smoker_nonsmoker',x='height',data=df , zorder=1 )
plt.show()

#Not normal (do the normality test if you want). So no t test. Let's go for non parametric

stat , pval =  stats.mannwhitneyu( df.height[df.gender=='M'] , 
                               df.height[df.gender=='F']  )
print('Mann-Whitney rank test p-value for gender :' , pval)


stat , pval =  stats.mannwhitneyu( df.height[df.smoker_nonsmoker=='NS'] , 
                               df.height[df.smoker_nonsmoker=='S']  )
print('Mann-Whitney rank test p-value for smoker :' , pval)

sns.violinplot(y='birth_place',x='height',data=df , color="0.8" )
sns.stripplot(y='birth_place',x='height',data=df , zorder=1 )
plt.show()

#Under represented labels : not a good feature

sns.violinplot(y='hair_colour',x='height',data=df , color="0.8" )
sns.stripplot(y='hair_colour',x='height',data=df , zorder=1 )
plt.show()

sns.violinplot(y='eye_colour',x='height',data=df , color="0.8" )
sns.stripplot(y='eye_colour',x='height',data=df , zorder=1 )
plt.show()

sns.violinplot(y='diet',x='height',data=df , color="0.8" )
sns.stripplot(y='diet',x='height',data=df , zorder=1 )
plt.show()

# Again, no ANOVA for us here, so we replace it with a Kruskal-Wallis test. 
# H1 is a significant association of the factor with a change in the average of the numerical variable

print('Kruskal test for hair colour')
s,pval = stats.kruskal(df.height[df.hair_colour=='lb'] , df.height[df.hair_colour=='db'], df.height[df.hair_colour=='bl'])
print('\t\t->',pval)

print('Kruskal test for eye colour')
s,pval = stats.kruskal(df.height[df.eye_colour=='1'] , df.height[df.eye_colour=='2'], df.height[df.eye_colour=='3'], df.height[df.eye_colour=='4'])
print('\t\t->',pval)

print('Kruskal test for diet')
s,pval = stats.kruskal(df.height[df.diet=='1'] , df.height[df.diet=='2'], df.height[df.diet=='3'], df.height[df.diet=='4'])
print('\t\t->',pval)
