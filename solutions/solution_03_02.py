stat , pval = stats.ks_2samp( mice_data.loc[ mice_data.genotype=='WT' , 'weight'] , 
                mice_data.loc[ mice_data.genotype=='KO' , 'weight'])

print("KS test p-value :", pval)
