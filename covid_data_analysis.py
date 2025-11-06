import pandas as pd
df = pd.read_csv("covid_dataset.csv")
print("First 5 rows:\n", df.head())

if df.isnull().values.any():
    print("\nNull values found:")
    print(df.isnull().sum())

    
    df = df.fillna(df.median(numeric_only=True))
    print("\nMissing values filled with column median.")
    
    df.to_csv('cleaned_covid_Stats.csv', index=False)
    print("\n Cleaned dataset saved as 'cleaned_Covid_Stats.csv'")
else:
    print("\nNo null values found in the dataset.")
    

print("Number of records exist for each country in the dataset:")
Count=(df['Country'].value_counts())
print(Count)

print("Total number of cases exceeds 1,000,000")
df_filtered = df[df['total_cases'] > 1000000]
print(df_filtered)

print("Increase 'total_cases' column by 10%")
df = df[df['deaths'] >= 10]
print(df)

print("Increase all the values in the 'total_cases' column by 10%")
df['total_cases'] = df['total_cases'] * 1.10
print(df['total_cases'])

print("Mean number of cases for each continent")
mean_cases = df.groupby('continent')['total_cases'].mean()
print(mean_cases)

print("Filter record from '2020-01-01' to '2020-12-31'")
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
Filtered_Data = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2020-12-31')]
print(Filtered_Data)


print("Calculate death rate for each country")
df['death_rate'] = df['deaths'] / df['total_cases']
death_rate_country = df.groupby('Country')['death_rate'].mean()
print(death_rate_country)

print("People in the age group 60")
df_age60 = df[df['age'] == 60]
print(df_age60)

print("Visualizing Covid Data")
import matplotlib.pyplot as plt

country_cases = df.groupby('Country')['total_cases'].max()
top_countries = country_cases.nlargest(10)

top_countries = top_countries / 1_000_000

plt.figure(figsize=(10, 5))
top_countries.plot(kind='bar', color='skyblue')

plt.xlabel('Country')
plt.ylabel('Total Cases (in Millions)')
plt.title('Top 10 Countries by Total Cases')
min_val = top_countries.min()
max_val = top_countries.max()
plt.ylim(0, max_val * 2.5) 
plt.tight_layout()  
plt.show(block=False)
plt.pause(5)

print("Graph Showed")

print("Recovery Rate")
df['recovery_rate'] = df['recoveries'] / df['total_cases']
recovery_rate_country = df.groupby('Country')['recovery_rate'].mean()
print(recovery_rate_country)

print("Replace negative values in the 'total_cases'&'deaths'")
Total_Cases = df['total_cases'].clip(lower=0)
Deaths = df['deaths'].clip(lower=0)
print(Total_Cases)
print(Deaths)