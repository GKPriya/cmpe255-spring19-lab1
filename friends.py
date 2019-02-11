
# coding: utf-8

# In[1]:


import numpy as np
users =[

    { "id":0, "name": "Hero" },

    { "id":1, "name": "Dunn" },

    { "id":2, "name": "Sue" },

    { "id":3, "name": "Chi" },

    { "id":4, "name": "Thor" },

    { "id":5, "name": "Clive" },

    { "id":6, "name": "Hicks" },

    { "id":7, "name": "Devin" },

    { "id":8, "name": "Kate" },

    { "id":9, "name": "Klein" }    

]



friendship = [

    (0, 1),

    (0, 2),

    (1, 2),

    (1, 3),

    (2, 3),

    (3, 4),

    (4, 5),

    (5, 6),

    (6, 7),

    (6, 8),

    (7, 8),

    (8, 9)

]


# In[2]:


def helper():
    for i in users:
        
        i['friends']=[]
        i['count'] = 0
        #adding friends into the list of friends in the dictinary of each user
        for j,k in friendship:
            if j == i['id'] :
                i['friends'].append(k)
              
            if k == i['id'] :
                i['friends'].append(j)
   
        i['count'] = (len(i['friends']))  
        
    


# In[3]:


#finding  the number of friends for each user
def num_friends(user):
    '''

    Find number of friends for a given user

    '''
    
    # TODO
    for i in users:
        
        # creating a new key value pair of friends in the dictionary user which will contain the friends list of that particular user

        helper()
        
        if user==i['id'] or user==i['name']:
            
            print(i['name'] +' has '+ repr(i['count'])+' friends')
            print("The id of " + i['name'] + ' is '+repr(i['id']))
           
            for x in i['friends']:
                
                for i in users:
                    
                    if i['id'] == x:
                        
                        print(repr(user) + ' is friends with ' + i['name'])
                        
          


# In[4]:


num_friends(0)


# In[5]:


num_friends('Dunn')


# In[6]:


print(users)


# In[7]:


def sort_by_num_friends():
     

    '''README.md

    Sort from "most friends" to "least friends"

    '''
    
   # take second element for sort
    for i in users:
        helper()
        
       
    def takeSecond(elem):
      
        return elem["count"]

    # sort list with key
    sortedList = sorted(users,reverse=True, key=takeSecond)
    
    for user in sortedList:
        print(user['name'] + ' has ' + repr(user['count'])+" friends")
 
         

    

    pass


# In[8]:


sort_by_num_friends()

