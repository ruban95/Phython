#!/usr/bin/env python
# coding: utf-8

# In[81]:


import re
import pandas as p

def check_email(email):
        regex ="^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        flag=True
        if(not re.search(regex,email)):
            flag=False
        if flag:
            return flag

    


# In[19]:


def pass_validation(password):
    spec_char=['!','@','#','$','%','^','&','*','_','-','.','~']
    flag=True
    
    if(len(password)<5):
        print("password length must be greater than 5 char")
        flag=False
    if(len(password)>16):
        print("password length must be less than 16 char")
        flag=False
    if not any(char in spec_char for char in password):
        print("password must contain atleast one special char")
        flag=False
    if not any(char.isupper() for char in password):
        print("password must contain atleast one upper case char")
        flag=False
    if not any(char.islower() for char in password):
        print("password must contain atleast one lower case char")
        flag=False
    if not any(char.isdigit() for char in password):
        print("password must contain atleast one numeric char")
        flag=False    
    if flag:
        return flag
    
        
    


# In[82]:


email=input("Enter your email id:")


# In[7]:


password=input("Enter your password:")


# In[83]:


print(check_email(email))


# In[13]:


print(pass_validation(password))


# In[ ]:



    
    
    


# In[132]:


###sign up functionality 
def signup():
    email=input("Enter your Email Id:")
    print(check_email(email))
    password=input("Enter password:")
    print(pass_validation(password))
    with open("email_pass_details.txt", "a+") as f:
        f.seek(0)
        data=f.read(100)
        if len(data)>0:
            f.write(",")
        ###ensuring record is not present in file    
        if email in useremailvalidation():
            print("***email already registered,please use different email address***")
        else:
            if check_email(email)==True:
                if pass_validation(password)==True: 
                    f.write(email+',')
                    f.write(password)
                    ##print("data stored in the file")
                    print("***email registered successfully*****")
                    
           
    f.close()


# In[137]:


###Reading prevoius user list to ensure no duplicate Record is created with same email_id
def useremailvalidation():
    with open("email_pass_details.txt", "r") as a:
                c=a.read()        
                username=list(c.split(","))            
                #print(username)
                return username
    a.close()         


# In[136]:


signup()


# In[168]:


###email_id and password matching in the Record validation
def Convert(username):
    print("Enter Your Registered Email_id and Password")
    email=input("enter your email:")
    password=input("enter your password:")
    
    user_details = {username[i]: username[i + 1] for i in range(0, len(username)-1, 2)}
    password1=user_details.get(email)
    #print(user_details)
    if email in user_details.keys():
            #print("username exist ")
            if password==user_details.get(email):
                print("""******Successfully completed Guvi Task1******""")
                
            else:
                print("&&&&-----incorrect passcode------&&&&&")
                while 1:
                    print("*****forget Password******")
                    print("1.To retrive the password")
                    print("2.Back to login page")
                    print("3.Exit")
                    ch=int(input("Enter your choice"))
                    if ch==1:                        
                        print(f"your passcode is:{password1}")
                        break
                    elif ch==2:
                        login()
                        break
                    elif ch==3:
                         break
                    else:
                         Print("Wrong choice")    
    else:
        print("&&&&&----email_id not registered-----&&&&&&")
        while 1:
            print("*****incorrect email******")
            print("1.To Signup")
            print("2.Back to login page")
            print("3.Exit")        
            ch=int(input("Enter your choice"))
            if ch==1:
                signup()
                break            
            elif ch==2:
                login()
                break            
            elif ch==3:
                break
            else:
                Print("Wrong choice")    
          
    return user_details


# In[158]:


###Login functionality
def login():
    
    with open("email_psw_details.txt", "r") as a:
        c=a.read()
        #print(c)
        username=list(c.split(","))
        #print(username)  
        Convert(username)      
   
   ## print(username,passw)
    a.close()    
    


# In[127]:


login()


# In[169]:


###Task1
while 1:
    print("*****Login system******")
    print("1.signup")
    print("2.login")
    print("3.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        signup()
        break
    elif ch==2:
        login()
        break
    elif ch==3:
        break
    else:
        Print("Wrong choice")


# In[ ]:





# In[ ]:




