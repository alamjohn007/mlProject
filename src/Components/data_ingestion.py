import os
import pandas
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exceptions import CustomException

#Craete a Data class to set up the Class Variables

@dataclass
class IngestionConfig:
    train_data_path = os.path.join('artifcats', 'train.csv')
    test_data_path = os.path.join('artifcats', 'test.csv')
    raw_data_path = os.path.join('artifcats', 'raw_data.csv')

class DataIngestion:

    def __init__(self):
        self.ingestionconfig = IngestionConfig()
    
    def data_ingestions(self):
        
        #logging.info("The data Ingestion process initiated")

        try:            
            #read the data
            #logging.info("Reading Data from student database")
            df = pd.read_csv(r'.\Data\stud.csv')           
            
            #Create Artifacts 
            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path), exist_ok= True)

            #Create trainset and test set
            train_set , test_set = train_test_split(df, test_size=0.20, random_state= 42)

            #save the train, test to the artifacts folders
        
            train_set.to_csv(self.ingestionconfig.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestionconfig.train_data_path, index = False, header = True)


        except Exception as e:
               raise CustomException(str(e))
        

if __name__ == "__main__":
    
    obj = DataIngestion()
    obj.data_ingestions()