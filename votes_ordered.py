from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

source = "E:\\WORK\\PROGRAMMER\\omr_tasks\\Votes\\Votes.txt"
destination = 'E:\\WORK\\PROGRAMMER\\omr_tasks\\Votes\\Votes_ordered.csv'

def vote_ordered(src, dest):
    #open the name list file votes.txt 
    file = open(src, 'r') 
    names = file.read()
    #replace the new line with space 
    names =names.replace('\n' ,',').split(',')
    #remove the last empty character 
    names  = names[:-1]
    #close the file 
    file.close()
    # creates a dictionary of the name(key) and it frequency (value)
    freqs = Counter(names)
    
    # here we have three levels of sorting 
    ''' first sort (the outer) : is to sort by the frequency (values):
            supposed to be like that >> sorted(freq.items(), key = lambda p: p[1] , reverse=True))
            but first sort must be sorted by the first name also so we do the second sort.
        second sort (the middle) : 
            supposed to be like that >> sorted(freq.items(), key = lambda p: p[0].split(" ")[0]))
            but second sort must be sorted  by the second name also so we do the third sort.
        third sort (the inner) :
            supposed to be like that >> sorted(freq.items(), key = lambda p: p[0].split(" ")[1]))
    so we put each level inside the other as we mentioned 
    '''
    sorted_count = sorted(
                        sorted(
                                sorted(freqs.items(),  
                                           key = lambda p: p[0].split(" ")[1] ),  
                                               key = lambda p: p[0].split(" ")[0]) ,
                                                  key = lambda p: p[1] , reverse=True)
    #sorted_count is a list of tuples so we put it in a dataframe  
    df = pd.DataFrame(sorted_count)
    #convert the dataframe into a csv file 
    df.to_csv(dest, header=None , index=None , sep=' ', mode='a')
    
    # ploting the names to its frequency
    alphab = list(df[0]) #names
    frequencies = list(df[1])#freq
    pos = np.arange(len(alphab))
    width = 1  
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2) )
    ax.set_xticklabels(alphab ,rotation = 90, fontsize = 8 ,color='blue', fontweight='bold',alpha=0.8)
    plt.bar(pos, frequencies, width, color='rgb')
    plt.show()
    
