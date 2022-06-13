experiment_distrib = stats.binom(n=10,p=0.5)

print('probability of obtaining 7 heads:' , experiment_distrib.pmf( 7 ) )
print('probability of obtaining 7 heads or less:' , experiment_distrib.cdf( 7 ) )
print('probability of obtaining 7 heads or more:' , 1-experiment_distrib.cdf(6)  )

# results at least as extreme as 7 are : 0,1,2,3 and 7,8,9,10
print('probability of obtaining a result as extreme as 7 heads:',
      experiment_distrib.cdf(3) + ( 1- experiment_distrib.cdf(6)) )

# results at least as extreme as 1 are : 0,1 and 9,10
print('probability of obtaining a result as extreme as 1 heads:',
      experiment_distrib.cdf(1) + ( 1- experiment_distrib.cdf(8)) )
