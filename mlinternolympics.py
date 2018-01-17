#Name-Rahul Verma
#Institution- Jaypee University of Engineeing and Technology

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics


def load_data():

    #loading csv file.
    df=pd.read_csv('olympics.csv',skiprows=1);

    #renaming summer  medals
    df.rename(columns={'01 !':'Gold'},inplace=True);
    df.rename(columns={'02 !':'Silver'},inplace=True);
    df.rename(columns={'03 !':'Bronze'},inplace=True);

    
    #renaming winter medals
    df.rename(columns={'01 !.1':'Gold1'},inplace=True);
    df.rename(columns={'02 !.1':'Silver1'},inplace=True);
    df.rename(columns={'03 !.1':'Bronze1'},inplace=True);
    
    #renaming total medals
    df.rename(columns={'01 !.2':'Gold2'},inplace=True);
    df.rename(columns={'02 !.2':'Silver2'},inplace=True);
    df.rename(columns={'03 !.2':'Bronze2'},inplace=True);

    #not given in the qn ,but i did it for simplicity
    df.rename(columns={'Unnamed: 0':'Country'},inplace=True);
    
    #splitting country name into two columns , one -Country name and Country 
    df['Country'],df['Code']=df['Country'].str.split('(',1).str;
    df.set_index('Country',inplace=True);

    del df['Code'];

    del df['Total']; 
    del df['Total.1']; 
    del df['Combined total']; 

   # print df.head(); 
   # df.to_csv('new.csv');
    return df;


def first_country(df):
    a=df.iloc[0];
    #print a;
    return a;


def gold_medal(df):
    #drop end row as it always be max
    df=df[:-1];
    i=df['Gold'].idxmax();
    #a=df.iloc[i];
    #print 'country with max gold medals in summer is',i;
    return i;


def biggest_difference_in_gold_medal(df):
    #again drop the end row
    df=df[:-1];
    a=(df['Gold']-df['Gold1']).abs().idxmax();
#    print a;
    return a;


def get_points(df):
    Points=3*(df['Gold']+df['Gold1']+df['Gold2'])+2*(df['Silver']+df['Silver1']+df['Silver2'])+1*(df['Bronze']+df['Bronze1']+df['Bronze2']);
    
    #add points column to existing dataframe
    df['Points']=Points;
    #print df;
    return Points;

def  k_means(pd2):
    #ELBOW ANALYSIS
    # doing k means clustering for gold,silve,bronze medals in summer 
    x1=pd2['Gold'];
    x2=pd2['Silver'];
    x3=pd2['Bronze'];

    
    plt.plot();
    plt.title('K Means Cluster');
    plt.scatter(x1,x2,x3);
    plt.show();
    

    X=pd2[['Gold','Silver','Bronze']];

    from sklearn.preprocessing import StandardScaler
    scaler=StandardScaler();
    X_scaled=scaler.fit_transform(X);

    cluster_range=range(1,20)
    cluster_errors=[]

    for num_clusters in cluster_range:
        clusters=KMeans(num_clusters)
        clusters.fit(X_scaled)
        cluster_errors.append(clusters.inertia_)

    clusters_df=pd.DataFrame({"num_clusters":cluster_range, "cluster_errors": cluster_errors} )
    
    #to plot graph uncomment these
    
    print clusters_df[0:10]
    plt.figure(figsize=(12,6));
    plt.plot( clusters_df.num_clusters, clusters_df.cluster_errors, marker = "o" );
    plt.xlabel('Number of clusters');
    plt.ylabel('Error');
    plt.title('Elbow Analysis for finding k');
    plt.show();


    # as there is a sharp dip on 2.5, so value of k should be 2 or 3
    return 3;

pd1=load_data();
#print pd1

pd2=first_country(pd1);
#print pd2

pd3=gold_medal(pd1);
#print pd3


pd4=biggest_difference_in_gold_medal(pd1);
#print pd4

pd5=get_points(pd1);
#print pd5

k_means(pd1);

