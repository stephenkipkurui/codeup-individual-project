import pandas as pd



def get_police_shootings_data():
    '''
    This function acquires data from shootings.csv file saved localy and initially downloaded from www.kaggle.com.
    Please refer to the final report for link to the data source.
    '''
    df = pd.read_csv('shootings.csv')
    return df