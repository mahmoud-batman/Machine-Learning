"""
get location 
get friends 

"""
import os 
import json 
import facebook 

if __name__== "__main__":
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBAC1rZBmVaZC6ExQcgwGRUnUYgy2UFB1LN3JN0DxSwqIHdavN2HWJZAC11O9aUrxKFfN8lZBmVSuwjSei4M8VmpP3qDZBZChbvmhUOQXOZAaT1BBqVCQUA8iJB8IhZBZBN3LBso1JiRkn5knclEZAEBCOFM98M5iqFkF7hGZC5qZBANPwksCgPFtb8hGuuXOmm1KZAVwZDZD'
                              , version='2.7')
    
    profile = graph.get_object(id= 'me',fields = "name , location{location}")
    friends = graph . get_connections ( id = 'me' , connection_name = 'friends' )
            
    print(json.dumps(friends, indent = 2))
    print(json.dumps(profile, indent = 2))
