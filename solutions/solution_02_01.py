
# 1. What would be the normal law followed by the mean of this sample of size 10, according to the CLT ?

# a sample of size 10, with a mean of 0.5 and standard deviation of 0.5:
# the mean of this sample follows a normal law of mean 0.5 and standard deviation of 0.5/np.sqrt(10)

# 2. Do you think the sample is large enough to use a normal law here ?

# let's do some simulations to decide
sampleSize=10
expectedMu = 0.5
expectedStdev = 0.5/np.sqrt(sampleSize)


sample_means = [samplingMean() for i  in range(100)]
approximation_normal = stats.norm(loc = expectedMu , scale = expectedStdev)
theoretical_binomial = stats.binom(n=10 , p = 0.5)

fig,ax = plt.subplots(figsize=(14,7))

sns.histplot(sample_means, stat='density' , kde=True, ax=ax , label = 'drawn samples')

x = np.linspace(0,1,100)
sns.lineplot( x=x , y=approximation_normal.pdf(x ) ,
             ax=ax , color="orange" , label = 'normal approximation')
sns.scatterplot( x=np.arange(11)/10 , 
                 y=theoretical_binomial.pmf(np.arange(11))*10 , 
                s=100,  color = 'green' ,ax=ax , label = 'actual binomial law')
