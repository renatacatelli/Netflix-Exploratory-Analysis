import pandas as pd
import matplotlib.pyplot as plt

#Reading a CSV with more data
netflix_df = pd.read_csv(r"C:\Users\renat\Documents\Data Science Projects\Investigating Netflix Movies and Guest Stars in the Office\netflix_titles.csv")
#print(netflix_df)
#column_names = netflix_df.columns
#print(column_names)

#DataFrame subset in which the column 'type' has the value 'Movie'
netflix_df_movies = netflix_df[netflix_df['type'] == 'Movie']

#Print the resulting DataFrame
#print(netflix_df_movies)

#Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies[['title', 'country', 'release_year', 'duration', 'listed_in']]

#Print the first five rows
print(netflix_movies_col_subset[0:5])

# Eliminar las filas con valores faltantes en las columnas "duration" y "year"
netflix_movies_col_subset.dropna(subset=['duration', 'release_year'], inplace=True)

netflix_movies_col_subset['duration'] = netflix_movies_col_subset['duration'].str.replace(" min","")
netflix_movies_col_subset["duration"] = netflix_movies_col_subset["duration"].astype(float)

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, row in netflix_movies_col_subset.iterrows():
    if row['listed_in'] == "Children":
        colors.append("red")
    elif row['listed_in'] == "Documentaries":
        colors.append("blue")
    elif row['listed_in'] == "Comedies":
        colors.append("green")
    else:
        colors.append("black")

# Inspect the first 10 values in your list      
colors[0:10]

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()