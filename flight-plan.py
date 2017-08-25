import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_2010 = pd.read_csv("2010-summary.csv" , error_bad_lines=False)
data_2011 = pd.read_csv("2011-summary.csv" , error_bad_lines=False)
data_2012 = pd.read_csv("2012-summary.csv" , error_bad_lines=False)
data_2013 = pd.read_csv("2013-summary.csv" , error_bad_lines=False)
data_2014 = pd.read_csv("2014-summary.csv" , error_bad_lines=False)
data_2015 = pd.read_csv("2015-summary.csv" , error_bad_lines=False)

data = [data_2010 ,data_2011,data_2012,data_2013,data_2014,data_2015]

"""
realation between countries annually 
"""

def annual(src , dest):
    count1_lst = []
    count2_lst = []
    yrs_lst = ["2010","2011","2012","2013","2014","2015"]
    for i in range(6):
        try:
            count1 = float(data[i][data[i]["ORIGIN_COUNTRY_NAME"] == src][data[i]["DEST_COUNTRY_NAME"] == dest]["count"])
            count2 = float(data[i][data[i]["DEST_COUNTRY_NAME"] == src][data[i]["ORIGIN_COUNTRY_NAME"] == dest]["count"])

            count1_lst.append(count1)
            count2_lst.append(count2)
        except:
            count1 = 0
            count2 = 0
            count1_lst.append(count1)
            count2_lst.append(count1)
    plt.plot(yrs_lst, count1_lst , 'o-'  ,label=""+src+" --> "+dest+"")
    plt.plot(yrs_lst, count2_lst , 'o-' , label=""+dest+" --> "+src+"")
    plt.legend()
    plt.title("number of journeys")
    
annual("Egypt" , "United States")   
annual("United Arab Emirates" , "United States")   


"""
top visitor countries
"""
def top_visitor(country , year , ntop ):

    i = int(year) - 2010
    data1 = data[i][data[i]["DEST_COUNTRY_NAME"] == country ]
    data_sorted = data1.sort_values(["count"] , ascending = False)    
    
    #this in case you choose the united state to avoid the united state from the graph
    data_sorted = data_sorted[1: ]
    
   # print(data_sorted[0:127])
    dt = list(data_sorted[0:int(ntop)]["ORIGIN_COUNTRY_NAME"])
    lst = list(data_sorted[0:int(ntop)]["count"])
    x = len(data_sorted[0:int(ntop)])
    x_lst = []  
    for i in range(x) :
        x_lst.append(i)
    plt.xticks(x_lst, dt , rotation = '90' , fontsize = 8)
    plt.plot(x_lst , normalize(lst) , 'o-')
    plt.title("top_"+str(ntop)+" visitors to "+str(country)+" in "+str(year)+"")
    
def normalize(lst):
    return list(map(lambda x : x / sum(lst) , lst))

top_visitor("United States" , 2010 , 20)

"""
top direction countries
"""
def top_directions(country , year , ntop ):
 #  country = 'Egypt'
    i = int(year) - 2010
    data1 = data[i][data[i]["ORIGIN_COUNTRY_NAME"] == country ]
    data_sorted = data1.sort_values(["count"] , ascending = False)    
    
    #this in case you choose the united state to avoid the united state from the graph
    data_sorted = data_sorted[1: ]
    
    dt = list(data_sorted[0:int(ntop)]["DEST_COUNTRY_NAME"])
    lst = list(data_sorted[0:int(ntop)]["count"])
    x = len(data_sorted[0:int(ntop)])
    x_lst = []  
    for i in range(x) :
        x_lst.append(i)
    
    
    plt.xticks(x_lst, dt , rotation = '90' , fontsize = 8)
    plt.plot(x_lst , normalize(lst) , 'o-')
    plt.title("top_"+str(ntop)+" directions from "+str(country)+" in "+str(year)+"")
    
    
top_directions("United States" , 2011, 20)


    
    
    
    
    
    


 
