import random 

#list of set of names to create from them the names of the person randomly 
lst = ["Omar","Mahmoud","Mostafa","Ahmed","Yassin","Mohamed","zyad","walid"]

#the path of the destination to put the text file in it 
address = "E:\\WORK\\PROGRAMMER\\omr_tasks\\Votes\\"

#lenOflst : the argument to choose the length of the list of persons 
def random_names( lstOFNames ,address , lenOflst ):    
    file = open(""+address+"Votes.txt" , 'a')
    #while the length not finished
    while lenOflst > 0 :
        # we put random integer we get from random.randint in the list of names 
        # example : lstOfNames[0]  >> 'omar' , lstOfName[1] >> 'mahmoud'
        # so we get a random collection of names and write it in the text file  
        file.write(lstOFNames[random.randint(0,(len(lstOFNames)-1))] + " " 
                         + lstOFNames[random.randint(0,(len(lstOFNames)-1))] +"\n")
        #decrement the list length to end the loop 
        lenOflst -= 1
        
    file.close()
