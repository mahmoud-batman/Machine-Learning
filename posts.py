"""
get posts
"""
import os 
import facebook
import json 
import requests

if __name__ == '__main__':
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBAC1rZBmVaZC6ExQcgwGRUnUYgy2UFB1LN3JN0DxSwqIHdavN2HWJZAC11O9aUrxKFfN8lZBmVSuwjSei4M8VmpP3qDZBZChbvmhUOQXOZAaT1BBqVCQUA8iJB8IhZBZBN3LBso1JiRkn5knclEZAEBCOFM98M5iqFkF7hGZC5qZBANPwksCgPFtb8hGuuXOmm1KZAVwZDZD',
                              version='2.7')
    all_fields = ['message' , 'created_time' ,'description','caption','link','place','status_type']
    all_fields = ','.join(all_fields)
    posts = graph.get_connections(id = 'me' , connection_name = 'posts' , fields = all_fields)
    
    #keep paging 
    while True :
        try:
            with open("E:\\WORK\\PROGRAMMER\\10)webCrawling\\FaceBook\\getpost\\my_post.json" , 'a') as f :
                for post in posts['data']:
                    f.write(json.dumps(post) + "\n")
                # ???? 
                posts = requests.get(posts['paging']['next']).json()
        except keyError:
            break