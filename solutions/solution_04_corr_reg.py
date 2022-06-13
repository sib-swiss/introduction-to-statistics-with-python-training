sns.pairplot(df)

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

#Again, no ANOVA for us here

print('Kruskal test for hair colour')
stats.kruskal(df.height[df.hair_colour=='lb'] , df.height[df.hair_colour=='db'], df.height[df.hair_colour=='bl'])

print('Kruskal test for eye colour')
stats.kruskal(df.height[df.eye_colour=='1'] , df.height[df.eye_colour=='2'], df.height[df.eye_colour=='3'], df.height[df.eye_colour=='4'])

print('Kruskal test for diet')
stats.kruskal(df.height[df.diet=='1'] , df.height[df.diet=='2'], df.height[df.diet=='3'], df.height[df.diet=='4'])

corre=df.corr(method='pearson')

from scipy.stats import kendalltau, pearsonr, spearmanr

def kendall_pval(x,y):
    return kendalltau(x,y)[1]    
    
def pearsonr_pval(x,y):
    return pearsonr(x,y)[1]
    
def spearmanr_pval(x,y):
    return spearmanr(x,y)[1]

corre_pval=df.corr(method=pearsonr_pval)
df_corr_pval = pd.DataFrame(corre_pval,columns=corre.columns)

import statsmodels.stats.multitest as ssm
corre_pval_adj=np.array([list(ssm.multipletests([np.array(corre_pval)[i][j]if j!=i else 1 for j in range(np.array(corre_pval).shape[1])]
                                                ,alpha=0.05,method='fdr_bh',is_sorted=False,returnsorted=False)[1]) 
                         for i in range(np.array(corre_pval).shape[0])])
df_corr_pval_adj = pd.DataFrame(corre_pval_adj,columns=corre.columns)

dico_columns={j:i for i,j in enumerate(list(df_corr_pval_adj.columns))}
oo=['height','shoe_size','weight','R_wrist_girth','L_wrist_girth',
   'nb_siblings_M','nb_siblings','nb_siblings_F','height_M','height_F']
new_dico_columns={j:i for i,j in enumerate(oo)}

dico_swap={dico_columns[s]:new_dico_columns[s] for s in dico_columns.keys()}
dico_swap={new_dico_columns[s]:dico_columns[s] for s in dico_columns.keys()}

the_matrix2=np.array(df_corr_pval_adj)
the_matrix=np.array([[the_matrix2[dico_swap[i],dico_swap[j]] for j in range(len(the_matrix2))]for i in range(len(the_matrix2))])

def highlight_cell(x,y, ax=None, **kwargs):
    rect = plt.Rectangle((x-.5, y-.5), 1,1, fill=False, **kwargs)
    ax = ax or plt.gca()
    ax.add_patch(rect)
    return rect

a=sns.clustermap(corre,z_score=None,row_cluster=True,col_cluster=True,method='ward',cmap='coolwarm',
                vmax=1,vmin=-1, annot=True, annot_kws={"size": 15})

a.ax_heatmap.set_title('Clustered pearson correlation\nbetween covariables',pad=100)
b=a.ax_heatmap
pp=0
for i in range(len(the_matrix)):
    for j in range(len(the_matrix)):
        if the_matrix[i][j]<0.05:
            if pp==0:
                highlight_cell(i+0.5,j+0.5,ax=b,color='k',linewidth=3,label='Significant multiple\ntesting adjusted pvalue<0.05')
            else:
                highlight_cell(i+0.5,j+0.5,ax=b,color='k',linewidth=3)
            pp+=1
b.legend(loc='best', bbox_to_anchor=(1, 0.8, 0.8, 0.5))
plt.show()

sns.violinplot(y='gender',x='shoe_size',data=df , color="0.8" )
sns.stripplot(y='gender',x='shoe_size',data=df , zorder=1 )
plt.show()

sns.violinplot(y='diet',x='shoe_size',data=df , color="0.8" )
sns.stripplot(y='diet',x='shoe_size',data=df , zorder=1 )
plt.show()

print('Kruskal test for diet vs shoe size')
stats.kruskal(df.shoe_size[df.diet=='1'] , df.shoe_size[df.diet=='2'], df.shoe_size[df.diet=='3'], df.shoe_size[df.diet=='4'])

print('Kruskal test for diet vs height')
stats.kruskal(df.height_M[df.diet=='1'] , df.height_M[df.diet=='2'], df.height_M[df.diet=='3'], df.height_M[df.diet=='4'])




ordered_loglike=[]
for p in ['shoe_size','height_M','nb_siblings_F']:
    model=smf.ols(formula='height ~ '+p, data=df)
    
    results = model.fit()

    res=results.summary()

    print(res)


    #### a little bit of gymnastic to get this summary saved and usable.

    results_as_html = res.tables[0].as_html()

    result_general_df2=pd.read_html(results_as_html, header=0, index_col=0)[0]
    list1=["Dep. Variable:"]+list(result_general_df2.index)+[result_general_df2.columns[1]]+list(result_general_df2[result_general_df2.columns[1]])
    list2=[result_general_df2.columns[0]]+list(result_general_df2[result_general_df2.columns[0]])+[result_general_df2.columns[2]]+list(result_general_df2[result_general_df2.columns[2]])

    dico_i={s:v for s,v in zip(list1,list2)}

    result_general_df=pd.DataFrame([[dico_i[v]] for v in list1],index=list1,columns=['Value'])


    



    results_as_html = res.tables[1].as_html()
    result_fit_df=pd.read_html(results_as_html, header=0, index_col=0)[0]
    ordered_loglike.append([p,float(result_general_df['Value']["Log-Likelihood:"]),result_fit_df])
    
ordered_loglike=sorted(ordered_loglike,key=itemgetter(1),reverse=True)

print([v[0] for v in ordered_loglike])



list_co=[]
ordered_loglike_multi=[]
for p in [v[0] for v in ordered_loglike]:
    list_co.append(p)
    model=smf.ols(formula='height ~ '+'+'.join(list_co), data=df)
    results = model.fit()

    res=results.summary()

    print(res)


    #### a little bit of gymnastic to get this summary saved and usable.

    results_as_html = res.tables[0].as_html()

    result_general_df2=pd.read_html(results_as_html, header=0, index_col=0)[0]
    list1=["Dep. Variable:"]+list(result_general_df2.index)+[result_general_df2.columns[1]]+list(result_general_df2[result_general_df2.columns[1]])
    list2=[result_general_df2.columns[0]]+list(result_general_df2[result_general_df2.columns[0]])+[result_general_df2.columns[2]]+list(result_general_df2[result_general_df2.columns[2]])

    dico_i={s:v for s,v in zip(list1,list2)}

    result_general_df=pd.DataFrame([[dico_i[v]] for v in list1],index=list1,columns=['Value'])


    



    results_as_html = res.tables[1].as_html()
    result_fit_df=pd.read_html(results_as_html, header=0, index_col=0)[0]
    ordered_loglike_multi.append(['_'.join(list_co),float(result_general_df['Value']["Log-Likelihood:"]),result_fit_df])
    
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