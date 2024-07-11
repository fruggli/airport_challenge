import pandas as pd

# Load the airports dataset
url = "https://davidmegginson.github.io/ourairports-data/airports.csv"
airports_df = pd.read_csv(url)

# Filter airports with a Wikipedia link
airports_with_wiki = airports_df[airports_df['wikipedia_link'].notnull()]

# Select only relevant columns: airport name and Wikipedia link
airports_with_wiki_list = airports_with_wiki[['id', 'wikipedia_link']]

# Save the filtered dataset to a new CSV file
airports_with_wiki.to_csv("airports_w_wiki.csv", index=False)


airports_with_wiki_list

