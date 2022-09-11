import requests
import json

# class for handling routes calling using class methods
class JsonPlaceholder:
    def __init__(self,url) -> None:
        self.url=url


    # to retrieve all posts
    def posts(self):
        url=self.url+"posts/"
        response = requests.get(url)        # To execute get request 
        return response
    
    # to retrieve all comments
    def comments(self):
        url=self.url+"comments/"
        response = requests.get(url)        # To execute get request 
        return response
    
    # to retrieve all users
    def users(self):
        url=self.url+"users/"
        response = requests.get(url)        # To execute get request 
        return response
    
    # to retrieve post with specific no.
    def postWithid(self,id):
        url=self.url+"posts/"+str(id)
        response = requests.get(url)        # To execute get request 
        return response
    
    # to retrieve comments according to post no. 
    def getComments(self,postId):
        url=self.url+"posts/"+str(postId)+"/comments"
        response = requests.get(url)        # To execute get request 
        return response



if __name__=='__main__':
    # Initializing JSON placeholder Object
    jsonPlaceHolder=JsonPlaceholder("https://jsonplaceholder.typicode.com/")


    # 1. Retrieve all posts
    resp=jsonPlaceHolder.posts()
    #  Checking for status
    if(resp.status_code!=404):
        print("Request Done Successfully")
        respj=json.loads(resp.text)
        print("-----------JSON format to list ----------")
        print(respj)
        print("------------------------------------------------")
        print("Total no of posts Retrieved are :-",len(respj))
    else:
        print("Eror 404: Unable to Retrieve Data")

    # 2.Retrieve post #10
    post10=jsonPlaceHolder.postWithid(9)
    #  Checking for status
    if(post10.status_code!=404):
        print("Successfullt Retrieved Post 10")
        respj=json.loads(post10.text)
        print("Title for Post #10 :- ",respj['title'])
        print("Encoding Property returned in the object is :- ",post10.encoding)
        print("X-Powered-By key value for object :- ",post10.headers['X-Powered-By'])
    else:
        print("Unable to Retrive data")


    # 3.Retrieve all posts from User ID 7
    #  Checking for status
    if(resp.status_code!=404):
        print("Request Done Successfully")
        respj=json.loads(resp.text)
        count=0
        for i in respj:
            if i['userId']==7:
                count+=1
        print("Total no of posts From User Id 7 are :-",count)
    else:
        print("Eror 404: Unable to Retrieve Data")

    #  4 Commnets from post 8
    #  Checking for status
    comments=jsonPlaceHolder.getComments(8)

    if(comments.status_code!=404):
        print("Request Done Successfully")
        respj=json.loads(comments.text)
        print("-----Comments on post 8--------")
        print(respj)
        print("-------------------------------")
        for i in respj:
            i['name'],i['email']=i['email'],i['name']
        # print(respj)
        for i in respj:
            r = requests.put('https://jsonplaceholder.typicode.com/posts/8/', data =i)
            if(r.status_code!=404):
                r=json.loads(r.text)
                print(r)
            else:
                print("Unable to update comment")
    else:
        print("Eror 404: Unable to Retrieve Data")

    # 5. Post 101
    #  Checking for status
    print("-------Try to Retrieve 101 post------------")
    post101=jsonPlaceHolder.postWithid(101)
    if(post101.status_code!=404):
        print("Successfully Retrieved Post 101")
        #print("Title fo Post#101")
        print("Encoding Property returned in the object is :- ",post101.encoding)
        print("X-Powered-By key value for object :- ",post101.headers['X-Powered-By'])
    else:
        print("Unable to Retrive data for Post 101")



