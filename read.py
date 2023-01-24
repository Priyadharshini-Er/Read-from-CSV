#Program for reading content from CSV file
#Developed by: Priyadharshini.P
#Register number: 22008758
import pandas as pd
df=pd.read_csv("nba.csv")
print(df.head(10))
print(df.tail())
print("Number of rows:",len(df.axes[0]))
print("Number of colums:",len(df.axes[1]))