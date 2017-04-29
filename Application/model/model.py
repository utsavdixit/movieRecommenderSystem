"""
model.py
Authors: Utsav Dixit
Description: This module is random forest model on the dataset.
            We're storing this model object using pickle for future usage.
"""
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import sklearn as sk
        
class guiProj: 

     #This is the main methiod  
    def main():
        
        #Count of decision trees used for random forest
        RFT_COUNT = 10           
        
        #path to fullDS
        fullDS=pd.read_csv('../data/fullDS.csv')
        
        #labelencoder object to convert categoric variables
        number = LabelEncoder()
        train['gender'] = number.fit_transform(train['gender'].astype('str'))
        
        #Target variable is also a categorical so convert it
        train["genre"] = number.fit_transform(train["genre"].astype('str'))
      
        #Fragmenting the data into two parts: training set and validation set
        msk = np.random.rand(len(train)) < 0.75
        Train = train[msk]
        validate = train[~msk]
        
        #Genrating the modle based on the feature list and target variable
        features=['age','gender','occupation_id','zipcode']
        x_train = Train[list(features)].values
        y_train = Train["genre"].values
        x_validate = validate[list(features)].values
        y_validate = validate["genre"].values
        
     
        #this will generate a random forest model on the provided data
        rf = RandomForestClassifier(n_estimators=RFT_COUNT)
        rf.fit(x_train, y_train)
    
        
        #This will generate a classification report which will state the accuracy of the model
        #status = rf.predict(x_validate)
        #print(type(status))
        #print(sk.metrics.classification_report(y_validate,status))
        #print(sk.metrics.accuracy_score(y_validate,status)) 
        
        #Storing the model into a pickle object for future usage
        with open('../data/rft.RF', 'wb') as f:
            pickle.dump(rf, f)
      
#==============================================================================
    if __name__=='__main__':
        main()
