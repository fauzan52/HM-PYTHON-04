x = ['mangga', 'apel', 'jeruk', 'pepaya', 'rambutan']
for i in x :
    if i == 'jeruk' :
        print ('jeruk peras')
        continue
    elif i == 'rambutan' :
        x.append ('kelapa')
        break
    elif i == 'pepaya' :
        index = x.index ('pepaya')
        x [index] = 'manggis'
        break
    print (i)
else :
    print ("Sudah dicetak")
    
print (x)