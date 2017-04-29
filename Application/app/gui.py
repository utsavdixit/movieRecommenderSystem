"""
gui.py
Authors: Utsav Dixit
Description: This module is creating a user interface framework for the
             movie recommender application.
"""
#Importing the library and packages used
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import Tk
from tkinter import*
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#class gui 
class guiProj: 
    #constructor of the class guiProj
    def __init__(self,master):
        self.master=master
        master.title("Movie Recommender System")
          
        self.labelmain = Label(master, text="Enter The Details of Users! Maximum 5 Users!")
        self.labelmain.grid(columnspan=5, sticky=W)
        
        self.labelage = Label(master, text="Age")
        self.labelage.grid(row= 3, column=2)
       
        self.labelgender = Label(master, text="Gender(M/F)")
        self.labelgender.grid(row=3, column=3)
       
        self.labelocc = Label(master, text="Occupation ID")
        self.labelocc.grid(row=3, column=4)
       
        self.labelzip = Label(master, text="Zip-Code")
        self.labelzip.grid(row=3, column=5)
       
        self.labeluser1 = Label(master, text="User 1 :")
        self.labeluser1.grid(row=4, column=1)
       
        self.labeluser2 = Label(master, text="User 2 :")
        self.labeluser2.grid(row=5, column=1)
       
        self.labeluser3 = Label(master, text="User 3 :")
        self.labeluser3.grid(row=6, column=1)
       
        self.labeluser4 = Label(master, text="User 4 :")
        self.labeluser4.grid(row=7, column=1)
       
        self.labeluser5 = Label(master, text="User 5 :")
        self.labeluser5.grid(row=8, column=1)
        
        #Drop down menu for age field        
        self.varage = StringVar(root)
        self.varage.set('Select' )
        self.agechoices = {'Select':'', 'Under 18':1, '18-24':18, '25-34':25, '35-44':35,'45-49':45, '50-55':50, '56+':56}
        self.ageoption = OptionMenu(root, self.varage, *self.agechoices.keys())
        self.varage1 = StringVar(root)
        self.varage1.set('Select')
        self.agechoices1 = {'Select':'', 'Under 18':1, '18-24':18, '25-34':25, '35-44':35,'45-49':45, '50-55':50, '56+':56}
        self.ageoption1 = OptionMenu(master, self.varage1, *self.agechoices1.keys())
        self.varage2 = StringVar(root)
        self.varage2.set('Select' )
        self.agechoices2 = {'Select':'', 'Under 18':1, '18-24':18, '25-34':25, '35-44':35,'45-49':45, '50-55':50, '56+':56}
        self.ageoption2 = OptionMenu(master, self.varage2, *self.agechoices2.keys())
        self.varage3 = StringVar(root)
        self.varage3.set('Select' )
        self.agechoices3 = {'Select':'', 'Under 18':1, '18-24':18, '25-34':25, '35-44':35,'45-49':45, '50-55':50, '56+':56}
        self.ageoption3 = OptionMenu(master, self.varage3, *self.agechoices3.keys())
        self.varage4 = StringVar(root)
        self.varage4.set('Select' )
        self.agechoices4 = {'Select':'', 'Under 18':1, '18-24':18, '25-34':25, '35-44':35,'45-49':45, '50-55':50, '56+':56}
        self.ageoption4 = OptionMenu(master, self.varage4, *self.agechoices4.keys())
       
        #Drop down menu for gender field
        self.vargen = StringVar(root)
        self.vargen.set('Select' )
        self.genchoices = {'Select':'', 'Male':'M','Female':'F'}
        self.genoption = OptionMenu(root, self.vargen, *self.genchoices.keys())
        self.vargen1 = StringVar(root)
        self.vargen1.set('Select' )
        self.genchoices1 = {'Select':'', 'Male':'M','Female':'F'}
        self.genoption1 = OptionMenu(root, self.vargen1, *self.genchoices1.keys())
        self.vargen2 = StringVar(root)
        self.vargen2.set('Select' )
        self.genchoices2 = {'Select':'', 'Male':'M','Female':'F'}
        self.genoption2 = OptionMenu(root, self.vargen2, *self.genchoices2.keys())
        self.vargen3 = StringVar(root)
        self.vargen3.set('Select' )
        self.genchoices3 = {'Select':'', 'Male':'M','Female':'F'}
        self.genoption3 = OptionMenu(root, self.vargen3, *self.genchoices3.keys())
        self.vargen4 = StringVar(root)
        self.vargen4.set('Select' )
        self.genchoices4 = {'Select':'', 'Male':'M','Female':'F'}
        self.genoption4 = OptionMenu(root, self.vargen4, *self.genchoices4.keys())
        
        #Drop Down menu for Occupation field
        self.varocc = StringVar(root)
        self.varocc.set('Select' )
        self.occchoices = {'Select':'', 'other or not specified':0, 'academic/educator':1, 'artist':2, 'clerical/admin':3,'college/grad student':4, 'customer service':5, 'doctor/health care':6,'executive/managerial':7,'farmer':8,'homemaker':9,'K-12 student':10,'lawyer':11,'programmer':12,'retired':13,'sales/marketing':14,'scientist':15,'self-employed':16,'technician/engineer':17,'tradesman/craftsman':18,'unemployed':19,'writer':20}
        self.occoption = OptionMenu(root, self.varocc, *self.occchoices.keys())
        self.varocc1 = StringVar(root)
        self.varocc1.set('Select' )
        self.occchoices1 = {'Select':'', 'other or not specified':0, 'academic/educator':1, 'artist':2, 'clerical/admin':3,'college/grad student':4, 'customer service':5, 'doctor/health care':6,'executive/managerial':7,'farmer':8,'homemaker':9,'K-12 student':10,'lawyer':11,'programmer':12,'retired':13,'sales/marketing':14,'scientist':15,'self-employed':16,'technician/engineer':17,'tradesman/craftsman':18,'unemployed':19,'writer':20}
        self.occoption1 = OptionMenu(root, self.varocc1, *self.occchoices1.keys())
        self.varocc2 = StringVar(root)
        self.varocc2.set('Select' )
        self.occchoices2 = {'Select':'', 'other or not specified':0, 'academic/educator':1, 'artist':2, 'clerical/admin':3,'college/grad student':4, 'customer service':5, 'doctor/health care':6,'executive/managerial':7,'farmer':8,'homemaker':9,'K-12 student':10,'lawyer':11,'programmer':12,'retired':13,'sales/marketing':14,'scientist':15,'self-employed':16,'technician/engineer':17,'tradesman/craftsman':18,'unemployed':19,'writer':20}
        self.occoption2 = OptionMenu(root, self.varocc2, *self.occchoices2.keys())
        self.varocc3 = StringVar(root)
        self.varocc3.set('Select' )
        self.occchoices3 = {'Select':'', 'other or not specified':0, 'academic/educator':1, 'artist':2, 'clerical/admin':3,'college/grad student':4, 'customer service':5, 'doctor/health care':6,'executive/managerial':7,'farmer':8,'homemaker':9,'K-12 student':10,'lawyer':11,'programmer':12,'retired':13,'sales/marketing':14,'scientist':15,'self-employed':16,'technician/engineer':17,'tradesman/craftsman':18,'unemployed':19,'writer':20}
        self.occoption3 = OptionMenu(root, self.varocc3, *self.occchoices3.keys())
        self.varocc4 = StringVar(root)
        self.varocc4.set('Select' )
        self.occchoices4 = {'Select':'', 'other or not specified':0, 'academic/educator':1, 'artist':2, 'clerical/admin':3,'college/grad student':4, 'customer service':5, 'doctor/health care':6,'executive/managerial':7,'farmer':8,'homemaker':9,'K-12 student':10,'lawyer':11,'programmer':12,'retired':13,'sales/marketing':14,'scientist':15,'self-employed':16,'technician/engineer':17,'tradesman/craftsman':18,'unemployed':19,'writer':20}
        self.occoption4 = OptionMenu(root, self.varocc4, *self.occchoices4.keys())
        
        #Assignment of values provided by user for age
        self.u1age = self.ageoption
        self.u1age.grid(row=4, column =2)
        self.u2age = self.ageoption1
        self.u2age.grid(row=5, column =2)   
        self.u3age = self.ageoption2
        self.u3age.grid(row=6, column =2)       
        self.u4age = self.ageoption3
        self.u4age.grid(row=7, column =2)       
        self.u5age = self.ageoption4
        self.u5age.grid(row=8, column =2)
        
        #Assignment of values provided by user for gender
        self.u1gender = self.genoption
        self.u1gender.grid(row=4, column =3)       
        self.u2gender = self.genoption1
        self.u2gender.grid(row=5, column =3)       
        self.u3gender = self.genoption2
        self.u3gender.grid(row=6, column =3)       
        self.u4gender = self.genoption3
        self.u4gender.grid(row=7, column =3)       
        self.u5gender = self.genoption4
        self.u5gender.grid(row=8, column =3)
        
        #Assignment of values provided by user for occupation
        self.u1occ = self.occoption
        self.u1occ.grid(row=4, column =4)       
        self.u2occ = self.occoption1
        self.u2occ.grid(row=5, column =4)       
        self.u3occ = self.occoption2
        self.u3occ.grid(row=6, column =4)       
        self.u4occ = self.occoption3
        self.u4occ.grid(row=7, column =4)       
        self.u5occ = self.occoption4
        self.u5occ.grid(row=8, column =4)       
        
        #Assignment of values provided by user for zip-code entry field
        self.u1zip = Entry(master)
        self.u1zip.grid(row=4, column =5)       
        self.u2zip = Entry(master)
        self.u2zip.grid(row=5, column =5)       
        self.u3zip = Entry(master)
        self.u3zip.grid(row=6, column =5)
        self.u4zip = Entry(master)
        self.u4zip.grid(row=7, column =5)
        self.u5zip = Entry(master)
        self.u5zip.grid(row=8, column =5)
       
        
        #submit button : it will call recommend method upon a mouse click 
        self.submit_button = Button(master, text="Recommend Movies!", command=self.recommend)
        self.submit_button.grid(row=9, column=3)
       
    
    #This function is called upon the mouse click by the user after the deatils were entered   
    def recommend(self):
        #A new window will be openend upon a mouse click to the button
        self.top = Toplevel()
        
        # This new window will fetch the recommend movie list from the model and present it to user
        self.top.title("Recommendation list for your group")
        
        #fetching the values of age provided by the user
        u1age=self.agechoices[self.varage.get()] 
        u2age=self.agechoices1[self.varage1.get()] 
        u3age=self.agechoices2[self.varage2.get()] 
        u4age=self.agechoices3[self.varage3.get()] 
        u5age=self.agechoices4[self.varage4.get()] 
        
        #fetching the values of gender provided by the user
        u1gender=self.genchoices[self.vargen.get()]
        u2gender=self.genchoices1[self.vargen1.get()] 
        u3gender=self.genchoices2[self.vargen2.get()]
        u4gender=self.genchoices3[self.vargen3.get()]
        u5gender=self.genchoices4[self.vargen4.get()]
        
        #fetching the values of occupation provided by the user
        u1occ=self.occchoices[self.varocc.get()]
        u2occ=self.occchoices1[self.varocc1.get()]
        u3occ=self.occchoices2[self.varocc2.get()]
        u4occ=self.occchoices3[self.varocc3.get()]
        u5occ=self.occchoices4[self.varocc4.get()]
        
        #fetching the values of zip-code provided by the user
        u1zip=self.u1zip.get()
        u2zip=self.u2zip.get()
        u3zip=self.u3zip.get()
        u4zip=self.u4zip.get()
        u5zip=self.u5zip.get()
       
        #the values entered are saved as a dataframe which will act as the testng dataframe for the prediction
        table=[[u1age,u1gender,u1occ,u1zip,''],[u2age,u2gender,u2occ,u2zip,''],[u3age,u3gender,u3occ,u3zip,''],[u4age,u4gender,u4occ,u4zip,''],[u5age,u5gender,u5occ,u5zip,'']]
        
        #This will break the calculation if the user have provided no detail for atleast one user
        null_pos = []
        for _ in range(len(table)):
            for u in table[_]:
                if u == '' and table[_].index(u) != 4:
                    null_pos.append(_)
                    break
        null_pos.reverse()
        for _ in null_pos:
            del table[_]
            
        if len(table) ==0:
            outputstring= 'No user details were provided'
            self.labelmain = Label(self.top, text=outputstring)#, image=background_image)
            self.labelmain.pack()
            return -1
        
        
        #cols will store names of attributes in the dataset
        cols=['age','gender','occupation_id','zipcode','genre']
        df=pd.DataFrame(table,columns=cols)
        
        #FullDS will store the dataset provided on the given path
        fullDS=pd.read_csv('../data/fullDS.csv')
        train=fullDS
        
        #tesing file will be the dataframe of details given by the user
        test = df
        
        # Used a label encoder to convert categoric attributes to numeric attributes
        number = LabelEncoder()
        train['gender'] = number.fit_transform(train['gender'].astype('str'))
        test['gender'] = number.fit_transform(test['gender'].astype('str'))
        
        #Target variable is also a categoric attribute
        train["genre"] = number.fit_transform(train["genre"].astype('str'))
        test["genre"] = number.fit_transform(test["genre"].astype('str'))
        
        # Feature will have the list of features for modelling
        features=['age', 'occupation_id','zipcode','gender']
        
        x_test=test[list(features)].values
        
        #loading the pickle dump which stores the object to the model created on the dataset
        with open('../data/rft.RF', 'rb') as f:
            rf = pickle.load(f)
        
        #predicting the value of target variable for the testing dataset.
        final_status = rf.predict(x_test)
        
        #fetching the movie recommendation list from the movie database 
        rating5=train[train['rating']==5]
        finaldf=pd.DataFrame()
        finalgenre=np.unique(final_status)
        
        #providing the user with random movies of recommended genre with highest rating
        for x in range(len(finalgenre)):            
            flist = rating5[rating5['genre'] ==finalgenre[x].item()]
            if len(flist) > 5:
                finaldf = finaldf.append(flist.sample(5))
            else:
                finaldf = flist
     
        #output will store the final list of recommended movies for the group
        output=finaldf['title']
        outputstring=output.to_string(index=False)
       
        #passing the result of recommended movie list to the display window
        self.labelmain = Label(self.top, text=outputstring)
        self.labelmain.pack()
      
      
#Tkinter root creation
root = Tk()
my_gui = guiProj(root)
root.mainloop()
