# 1. Compute the effect size of the diet on the weights 

n1 = len(CHOWdata)
n2 = len(HFDdata)

CHOWmean = np.mean(CHOWdata)
HFDmean = np.mean(HFDdata)

# now, what to do when we have not one, but two standard deviation...
# the correct answer is to pool the variance : https://en.wikipedia.org/wiki/Pooled_variance
CHOWsigmaSq = np.var(CHOWdata , ddof=1) # ddof, for delta degree-of-freedom handles the n-1 dividor
HFDsigmaSq = np.var(HFDdata , ddof=1)

pooled_variance = ( ( CHOWsigmaSq*(n1-1) ) + (HFDsigmaSq * (n2-1) ) )/(n1-1+n2-1)

# OK that one was a bit of a trick. You already get credit if you had the idea that something has to be done.

#from there, the effect size can be computed as before:
effect_size = ( CHOWmean - HFDmean )/ ( pooled_variance )**0.5
print("the effect size of diet on mice weight is",effect_size)
                                              

# 2. Compute the statistical power of the corresponding t-test for that effect size
print( 'power:' , P.power(effect_size=effect_size , nobs1=n1 , ratio=n2/n1 , alpha=0.05) )
