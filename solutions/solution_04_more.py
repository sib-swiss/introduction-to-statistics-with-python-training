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
s,pval = stats.kruskal(df.shoe_size[df.diet=='1'] , df.shoe_size[df.diet=='2'], df.shoe_size[df.diet=='3'], df.shoe_size[df.diet=='4'])
print('\t\t->',pval)
print('Kruskal test for diet vs height')
s,pval = stats.kruskal(df.height_M[df.diet=='1'] , df.height_M[df.diet=='2'], df.height_M[df.diet=='3'], df.height_M[df.diet=='4'])
print('\t\t->',pval)
