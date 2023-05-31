k = 'box' 

category='canton name'
represented_variable="60+ y.o." 

sns.catplot( x = represented_variable , y= category ,
             data=dfFractions , kind = k , orient='h',height=10, aspect=2 )
plt.grid()

# alternative for the curious
#sns.kdeplot( x = represented_variable , hue= category ,
#             data=dfFractions )
