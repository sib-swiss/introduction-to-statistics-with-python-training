

# we begin by computing a model for each covariables independently
ordered_loglike=[]
for p in ['shoe_size','height_M','nb_siblings_F']:
    model=smf.ols(formula='height ~ '+p, data=df)
    
    results = model.fit()

    #res=results.summary()
    #print(res)
    
    ordered_loglike.append([p,results.llf,results.params])
    
ordered_loglike=sorted(ordered_loglike,key=itemgetter(1),reverse=True)


## we can sort the co-variable by their log likelihood. We will then add them one by one to the model
print("retained order of co-variables :")
print("\t\t",[v[0] for v in ordered_loglike])
print('')

list_co=[]
ordered_loglike_multi=[]
for p in [v[0] for v in ordered_loglike]:
    list_co.append(p)
    model=smf.ols(formula='height ~ '+'+'.join(list_co), data=df)
    results = model.fit()

    res=results.summary()
    print(res)
    ordered_loglike_multi.append(['_'.join(list_co), results.llf ,results.params])
    
ordered_loglike_multi=sorted(ordered_loglike_multi,key=itemgetter(1),reverse=True)


print()
print('Modles',[v[0] for v in ordered_loglike_multi])
print('Log-Likelihood',[v[1] for v in ordered_loglike_multi])
print()

ordered_log_name=[v[0] for v in ordered_loglike_multi][::-1]
ordered_log_value=[v[1] for v in ordered_loglike_multi][::-1]

for i in range(1,len(ordered_log_value)):
    pval=1-stats.chi2.cdf(2*(ordered_log_value[i]-ordered_log_value[i-1]),1)
    print("The log likelihood difference between model {0} and model {1} \n is associated to a P value={2}".format(ordered_log_name[i-1],ordered_log_name[i],pval))
    print()
