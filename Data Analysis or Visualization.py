#https://github.com/cicilymathew945/Data-Analysis

import pandas as pd 
import os 
import glob 
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

#This function creates a report of rows in data file with null values in fileds 'unit price' and 'Quantity' that are dropped from file
def Dropped_data_report(file):
    x=file[file['Quantity'].isna()|file['unitprice'].isna()]
    x.to_csv('Missing_data.csv', mode='a',header='False')

#This function drops rows of the file with null values in fileds 'unit price' and 'Quantity'
#Function also splits the date fields into 'day', 'month', 'year' fields.
def Data_wrangling(file): 
    Dropped_data_report(file)   
    file = file.dropna(subset=['Quantity','unitprice'])
    file['OrderDate'] = pd.to_datetime(file['OrderDate'])
    #split date field to day, month & year
    file['day'] = file['OrderDate'].dt.day
    file['month'] = file['OrderDate'].dt.month_name()
    file['year'] = file['OrderDate'].dt.year
    return file

#Function top 3 product that sold by quantity in each year in seperate graphs
def Popular_product(file):
    l1=pd.DataFrame()
    l1=file.groupby(['Item'])['Quantity'].sum().nlargest(3).to_frame()
    l1.plot.bar()
    plt.title("Top 3 Popular poducts "+ csvnames[i])  

#Function to create a new column 'Gross revenue' and round by 2 decimal places
def Avg_monthly_rev(file):    
    file['Gross_R']=(file.Quantity)*(file.unitprice)+(file.tax)
    file['Gross_R'].round(2)

    monthly_avg={'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}
    m=pd.DataFrame(monthly_avg.items(), columns=['month', 'Gross_R'])
    l1=file.groupby(['month'])['Gross_R'].mean()
    year=file['year'].head(1)
    m2=pd.DataFrame([l1]).T
    m2=m2.reset_index()
    result = pd.concat([m, m2],  join='outer').groupby(['month'], sort=False)['Gross_R'].sum().round(2)
    x=result.to_frame()
    ax1.plot(x)
    ax1.tick_params(axis='x', labelrotation=45)

#Function to create bins based on the min value product sold and max value product sold to analyze the total orders
def Price_bins_order(file):
    group_names=['Low', 'Medium','High']
    file['Price-binned']=pd.cut(file['unitprice'],bins,labels=group_names,include_lowest=True)
    file.groupby(file['Price-binned'])['Quantity'].sum()
    #Histogram of binned Prices
    plt.title("Number of items sold for each Price Range of products "+ csvnames[i])
    plt.xlabel("Price category")
    plt.ylabel("Number of items sold")
    plt.hist(file['unitprice'],bins)
    plt.legend(filtered_f['year'], loc="upper left")
    plt.show()     
    
# use glob to get all the csv files in the folder 
path = os.getcwd() 
if os.path.exists('Missing_data.csv'):

    os.remove('Missing_data.csv')
csv_files = glob.glob(os.path.join(path, "*.csv"))
csvnames = []

for file in glob.glob("*.csv"):
    csvnames.append(file.replace('.csv',''))

#Define schema
headerList=['SalesOrderNumber', 'SalesOrderLineNumber','OrderDate', 'CustomerName','Email', 'Item', 'Quantity', 'unitprice','tax']

#User Input for the graph to display
choice=input("We can Anlayze the data and view the different charts on request. Enter the chart viewing option from below\n 1. Analyze data files and View Avg Monthly revenue Chart\n 2. Display Price ranges Vs Sold Items Count \n 3. Top 3 Popular product of the Year")
i=0

if int(choice) == 1:
    fig,ax1=plt.subplots()

# loop over the list of csv files 
for csv in csv_files:       
    # read each csv file and analyse
    file = pd.read_csv(csv,names=headerList, header=0) 
    f=Data_wrangling(file)
    #filter only requ fields for processing
    filtered_f=f.filter(['month','year','Item','Quantity','unitprice','tax'])
    
    match choice:
        case "1":#Analyze all data files and view monthly avg revenue chart 

            print(file.head())
            print(file.describe()) 
            Avg_monthly_rev(filtered_f)
                        
        case "2":#Display bins based on price range of items sold
            bins=np.linspace(min(filtered_f['unitprice']),max(filtered_f['unitprice']),4)
            Price_bins_order(filtered_f)
            i=i+1
            
        case "3":            
            Popular_product(filtered_f)
            i=i+1           

        case _:
            print("Invalid option")

if int(choice)==1:
    plt.title("Monthly Revenue Chart")
    plt.legend(csvnames, loc="lower left")
    plt.show()


