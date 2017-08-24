import random 

lst = ["Omar","Mahmoud","Mosata","Ahmed","Yassin","Jone","zyad","walid"]

def random_names( lstOFNames , lenOflst ):    
    file = open("E:\\WORK\\PROGRAMMER\\omr_tasks\\Votes.txt" , 'a')
    while lenOflst > 0 :
    
        print(lstOFNames[random.randint(0,(len(lstOFNames)-1))] + " " 
                         + lstOFNames[random.randint(0,(len(lstOFNames)-1))])
        
        file.write(lstOFNames[random.randint(0,(len(lstOFNames)-1))] + " " 
                         + lstOFNames[random.randint(0,(len(lstOFNames)-1))]+"\n")
        
        lenOflst -= 1
        
    file.close()