from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

source = "E:\\WORK\\PROGRAMMER\\omr_tasks\\Votes\\Votes.txt"
destination = 'E:\\WORK\\PROGRAMMER\\omr_tasks\\Votes\\Votes_ordered.csv'

def vote_ordered(src, dest):
    src = source
    file = open(src, 'r') 
    names = file.read()
    names =names.replace('\n' ,',').split(',')
    names  = names[:-1]
    file.close()
    freqs = Counter(names)
    sorted_count = sorted(
                        sorted(
                                sorted(freqs.items(),  
                                           key = lambda p: p[0].split(" ")[1] ),  
                                               key = lambda p: p[0].split(" ")[0]) ,
                                                  key = lambda p: p[1] , reverse=True)

    df = pd.DataFrame(sorted_count)
    dest = destination
    df.to_csv(dest, header=None , index=None , sep=' ', mode='a')
    
    alphab = list(df[0])
    frequencies = list(df[1])
    pos = np.arange(len(alphab))
    width = 1.0     # gives histogram aspect to the bar diagram
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2) )
    ax.set_xticklabels(alphab ,rotation = 90, fontsize = 8 ,color='blue', fontweight='bold',alpha=0.8)
    plt.bar(pos, frequencies, width, color='rgb')
    plt.show()