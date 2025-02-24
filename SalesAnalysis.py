import pandas as pd
df = pd.read_csv("C:\\powerbi\\sales.csv",encoding = 'latin-1')
print(df.head(10))

#check if any missing values are there in file
print(df.isnull().sum())


#fill or drop the rows having missing values
df['Sales'] = df['Sales'].fillna(0)
df ['Quantity']=df['Quantity'].fillna(0)


#remove duplicate based on specific column
df = df.drop_duplicates(subset = ['Order ID'])

print(df.head(10))

#change datatype to date
df['Order Date'] = pd.to_datetime(df['Order Date'],errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'],errors='coerce')

#ensure numeric fields have numeric data only
df['Sales'] = pd.to_numeric(df['Sales'],errors = 'coerce')# error = 'coerce' will set to nan if text is not convert to number
df['Discount'] = pd.to_numeric(df['Discount'],errors = 'coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'],errors = 'coerce')
df['Profit'] = pd.to_numeric(df['Profit'],errors = 'coerce')


df.to_csv("C:\\powerbi\\salesproject.csv",index=False)
