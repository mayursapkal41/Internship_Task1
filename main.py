import pandas as pd
df = pd.read_csv("netflix_titles.csv")

print("Missing values before cleaning:\n", df.isnull().sum())
df = df.dropna(subset=['title', 'type'])  
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unrated')
df['duration'] = df['duration'].fillna('Unknown')

df = df.drop_duplicates()

df['country'] = df['country'].str.strip().str.title()
df['type'] = df['type'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()  

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')  


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df.to_csv("netflix_titles_cleaned.csv", index=False)

print("Cleaned dataset saved as 'netflix_titles_cleaned.csv'")
print("Missing values after cleaning:\n", df.isnull().sum())
print("Final shape:", df.shape)
