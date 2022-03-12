import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def data_cleaning(df,sub_length):
    #Attributte with negative value
    dirty = ['time_response','domain_spf','asn_ip','time_domain_activation','time_domain_expiration','qty_ip_resolved','ttl_hostname','qty_redirects','url_google_index','domain_google_index']
    
    # Remove when to much missing values
    df= df.drop(columns=['domain_spf','time_domain_expiration','time_domain_activation'])

    # Bool value for google very few value just drop the row
    df = df.drop(df[(df['url_google_index'] ==-1) | (df['domain_google_index'] ==-1)].index)

    
    
    #For numeric value there realy extend so we replace the missing one by the median
    df=replace_by_median(df,'time_response')
    df=replace_by_median(df,'asn_ip')
    df=replace_by_median(df,'qty_ip_resolved')
    df=replace_by_median(df,'ttl_hostname')
    df=replace_by_median(df,'qty_redirects')

    # For sub length les's assume that -1 is a mistake instead of 0
    df[df==-1]=0

    # Check boolean
    #   print(df['email_in_url'].value_counts() )
    #   print(df['url_shortened'].value_counts() )

    return df

def data_transform(df,table1):
    # The quantity are transformed in pertance par length
    df[table1[0:18]] = df.apply(lambda row : row[table1[0:18]]/row['length_url'], axis = 1)

    return df

def data_normalize(df,sub_length):

    # Normalization
    att_to_norm = ['length_url','asn_ip','time_response','qty_ip_resolved','qty_nameservers','qty_mx_servers','ttl_hostname','qty_redirects']
    att_to_norm = att_to_norm +sub_length
    scaler = MinMaxScaler()
    df[att_to_norm] = scaler.fit_transform(df[att_to_norm])

    return df

def replace_by_median(df,att):
    m = df[att].median()
    df[att] = df[att].replace(-1,m)
    return df

def des(df):
    print(df.describe().transpose() )

if __name__ == "__main__":
    data = pd.read_csv('dataset/dataset_small.csv')
    # Keep only the value of all URL and extra to start and the length of each part
    table_1 = list(data.iloc[:,:19].columns)
    table_6 = list(data.iloc[:,-16:].columns)
    sub_length= ['domain_length','directory_length','file_length','params_length','qty_params']
    df = data[table_1+table_6+sub_length]
    
    print('Cleaning...')
    df = data_cleaning(df,sub_length)
    
    print('Transform...')
    df = data_transform(df,table_1)
    df.to_csv('dataset/clean_data_no_norm.csv', index=False)
    print('Normalization...')
    df = data_normalize(df,sub_length)

    df.to_csv('dataset/clean_data.csv', index=False)
