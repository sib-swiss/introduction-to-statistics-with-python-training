
##creating an object corresponding to our null hypothesis
## of 10 coin toss of a fair coin (p=0.5)
experiment_distrib = stats.binom(n=10,p=0.5)

#.pmf() gives the probability of realisation of a particular number 
for i in range(11):
    print('probability of getting',i,'head :',experiment_distrib.pmf(i)) # proba of getting 0 head
    
# 1. How likely was this result, provided the coin is fair? 
print('probability of obtaining 7 heads:' , experiment_distrib.pmf( 7 ) )

# 2. How likely was it to come up with at most 7 heads , provided the coin is fair? 
#  getting at most 7 = poba of getting 0, or 1, or 2, or ..., or 7

# one (tedious) possibility:
# experiment_distrib.pmf(0) + experiment_distrib.pmf(1) + experiment_distrib.pmf(2) + ... 

# better: Cumulative Density Function -> sum of probability of everything before a given number 
print('probability of obtaining 7 heads or less:' , experiment_distrib.cdf(7) )

# 3. How likely was it to come up with at least 7 heads , provided the coin is fair? 

# the probability to get 7 heads or more is the probability of NOT doing 6 or less:
print('probability of obtaining 7 heads or more:' , 1-experiment_distrib.cdf(6)  )

# 4. How likely was it to come up with a result at least as different from the expected mean of 5, provided the coin is fair? 

# results at least as extreme as 7 are : 0,1,2,3 and 7,8,9,10
print('probability of obtaining a result as extreme as 7 heads:',
      experiment_distrib.cdf(3) + ( 1- experiment_distrib.cdf(6)) )

# 5. How about if you come up with 1 heads out of 10 ? Do you think the coin is fair in that case? 

# results at least as extreme as 1 are : 0,1 and 9,10
print('probability of obtaining a result as extreme as 1 heads:',
      experiment_distrib.cdf(1) + ( 1- experiment_distrib.cdf(8)) )
