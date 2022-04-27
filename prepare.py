import pandas as pd
import numpy as np
from acquire import get_police_shootings_data
from sklearn.model_selection import train_test_split
import datetime

def encode_data(df):
    '''
    Encode categorical features to numeric for analysis
    ''' 
    df['enc_sign_mentally_ill'] = df.signs_of_mental_illness.map({'False':0, 'True':1})
    df['enc_manner_death'] = df.manner_of_death.map({'shot':0, 'shot and Tasered':1})

     # Encode binary categorical variables to numeric
    df['enc_arm_category'] = df.arms_category.map({'Unarmed': 0, 'Unknown': 1, 'Blunt instruments': 2, 
                                                   'Other unusual objects':3, 'Sharp objects':4, 'Vehicles':5, 
                                                   'Multiple':6, 'Electrical devices':7, 'Piercing objects':8, 
                                                   'Explosives':9, 'Guns':10})

     # Encode multivariate variables to numeric
    df['enc_armed'] = df.armed.map({"Unarmed": 0, "Unknown": 1, "knife": 2, "sword": 2, "scissors": 2, 
                                    "box cutter": 2, "machete": 2, "pick-axe":2, "lawn mower blade": 2,
                                    "straight edge razor": 2,"samurai sword": 2, "meat cleaver": 2, "pole and knife": 2, 
                                    "sharp object": 2, "baseball bat and fireplace poker": 2,"bow and arrow": 2,
                                    "glass shard": 2, "contractor's level": 3,"pitchfork": 3, "screwdriver": 3, 
                                    "box cutter": 3, "ax": 3, "shovel":3,"garden tool": 3, "chainsaw": 3, 
                                    "chain saw": 3, "stapler": 3, "chain":3,"vehicle":4, "car":4, "gun and car":5, 
                                    "vehicle and gun":5, "gun and knife":5, "hatchet and gun":5, "gun and vehicle":5, 
                                    "gun and sword":5, "gun":5,"BB gun":5, "guns and explosives":5, "BB gun and vehicle":5,
                                    "machete and gun":5,"air pistol":5, "knife and mace":5, "Taser":5,"pipe":6,
                                    "crossbow":6, "baseball bat":6, "metal pipe":6,"metal stick":6,"pole":6, "baton":6,
                                     "piece of wood":6, "blunt object":6, "crowbar":6, "metal object":6, 
                                    "baseball bat and bottle":6,"metal pole":6, "ice pick":6, "brick":6, "rock":6, "chair":6, 
                                    "toy weapon":7, "beer bottle":8,"fireworks":9,"incendiary device":9,"fireworks":9, 
                                    "walking stick":10, "grenade": 11,
                                    "flashlight":11, "hand torch":11 })
  
    df['enc_attack_level'] = df.threat_level.map({'undetermined': 0, 'attack': 1, 'other':2})
    df['enc_flee'] = df.flee.map({'Not fleeing': 0, 'Foot': 1, 'Car':2, 'other':3})
    df['enc_gender'] = df.gender.map({'F': 0, 'M': 1})
    df['enc_body_camera'] = df.body_camera.map({'F': 0, 'T': 1})
    df['enc_race'] = df.race.map({'White': 0, 'Black': 1, 'Hispanic':2, 'Native':3, 'Asian':4, 'other':5})
    
    # Fill NaNs unknowns with 1 == Unknown (initial df had no NaNs)
    df = df.fillna(1)
    
    return df


def prepare_police_shootings_data():
    '''
    Main prepare function for police df data preparation. Function performs all necessary 
    data preparation functions for exploration.
    
    '''
    # Get dataframe from acquire.py
    df = get_police_shootings_data()
    
    # Drop unnecessary columns
    df = df.drop(columns = ['id', 'name'])
                 
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Check % of rows and columns nulls ans drop 
    
    # Fill remaining nulls with column average mean
    df = df.reset_index(drop = True)
    
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month
    df['day'] = pd.DatetimeIndex(df['date']).day
    df['week']= pd.DatetimeIndex(df['date']).weekofyear
    df['quarter']= pd.DatetimeIndex(df['date']).quarter
    df['gun_violence'] = np.where(df['arms_category']== 'Guns', 1, 0)

    # Encode df
    df = encode_data(df)
    
    # lower cols names
    df.columns = df.columns.str.lower()
    
    # Set datetime 
    df.date = pd.to_datetime(df.date)
    
    # Index date columns and sort index
    df = df.set_index('date').sort_index()
    
    # Split the data into train, validate and test
    train_validate, test = train_test_split(df, test_size = 0.2, random_state = 123)
    train, validate = train_test_split(train_validate, test_size = 0.3, random_state = 123)
    
    return train, validate, test


def prepare_modeling_data(target = 'gun_violence',seed = 123):
    '''
    This function is an extension to the prepare_police_shootings_data above and intended for 
    medeling. All categorical data have been stripped, encoded and target variable set in the 
    header aswell as seed.
    '''
    train, validate, test = prepare_police_shootings_data()
    
    train = train.drop(columns = ['manner_of_death', 'armed', 'gender', 'race','city', 
                          'state', 'signs_of_mental_illness','threat_level','flee',
                          'body_camera','arms_category'])
    validate = validate.drop(columns = ['manner_of_death', 'armed', 'gender', 'race','city', 
                          'state', 'signs_of_mental_illness','threat_level','flee',
                          'body_camera','arms_category'])
    test = test.drop(columns = ['manner_of_death', 'armed', 'gender', 'race','city', 
                          'state', 'signs_of_mental_illness','threat_level','flee',
                          'body_camera','arms_category'])

    return train, validate, test