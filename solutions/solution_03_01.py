# 1. Test the association between majority religion (`'majority_religion'`) and majority language 
table = pd.crosstab( dfFractions['majority religion'] , dfFractions['majority language'] )

print(table)

## chi square test
chi2,pval , df, expected = stats.chi2_contingency(table , correction=False)
print("Chi-square test")
print('\tchi2:', chi2)
print('\tp-value:', pval)


# seeing what happens with the fisher test
try:
    oddsratio , pvalue = stats.fisher_exact(table)
    print("Fisher's exact test")
    print('\todds ratio:',oddsratio)
    print('\tp-value:',pvalue)
except Exception as e:
    print('error in fisher test:',e)

print('')
# 2. How could you make Fisher's test work here?
# there are two main options :
# * grouping together several categories to reduce the number of rows, columns
# * removing some of the categories (the less frequent ones for instance)
# -> the first option is not obvious here (which to merge?), so we go with the second one

subTable = table.iloc[:,:2] # keep french and german speakers only
oddsratio , pvalue = stats.fisher_exact(subTable)
print("Fisher's exact test on sub-table")
print('\todds ratio:',oddsratio)
print('\tp-value:',pvalue)
