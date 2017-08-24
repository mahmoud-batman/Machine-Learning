import random 

lst = ["Omar","Mahmoud","Mosata","Ahmed","Yassin","Jone","zyad","walid"]
address = "E:\\WORK\\PROGRAMMER\\omr_tasks\\"
def random_names( lstOFNames ,address , lenOflst ):    
    file = open("Votes.txt" , 'a')
    while lenOflst > 0 :
    
        print(lstOFNames[random.randint(0,(len(lstOFNames)-1))] + " " 
                         + lstOFNames[random.randint(0,(len(lstOFNames)-1))])
        
        file.write(lstOFNames[random.randint(0,(len(lstOFNames)-1))] + " " 
                         + lstOFNames[random.randint(0,(len(lstOFNames)-1))]+"\n")
        
        lenOflst -= 1
        
    file.close()
