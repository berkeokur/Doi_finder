import pandas as pd
from habanero import Crossref

# Create a CrossRef client
cr = Crossref()

# Load the Excel file into a DataFrame
excel_file_path = "./file.xlsx"
df = pd.read_excel(excel_file_path, engine='openpyxl')

# Select the first 100 rows using the head() method
df_first_100_rows = df.head(10)

# Iterate over the selected rows
for index, row in df_first_100_rows.iterrows():
    # Extract the article title from column "M"
    article_title = row['Article Title']
    
    # Extract and split the author names from column "Authors" (assuming names are comma-separated)
    author_names = row['Authors']
    first_author_name = author_names.split(',')[0] if pd.notna(author_names) else ""
    
    # Check if the article title and first author name are not empty
    if pd.notna(article_title) and first_author_name:
        # Search for DOI using the article title and first author name
        query = f"title:{article_title + ' ' + first_author_name}"
        results = cr.works(query=query, limit=10)
        
        # Initialize variables to store the DOI and DOI link
        doi = None
        doi_url = None
        
        # Check if any results were found
        if results['message']['total-results'] > 0:
            # Iterate over the top 10 results
            for result in results['message']['items'][:10]:
                # Check if the result contains a DOI
                if 'DOI' in result:
                    doi = result['DOI']
                    doi_url = f"https://doi.org/{doi}"
                    
                    # If the article title exactly matches the original query, use this result
                    if article_title.lower() == result['title'][0].lower():
                        break  # Exit the loop, using this result
                        
            # If there was no match with the original queried article title, use the first result
            if doi is None:
                first_result = results['message']['items'][0]
                doi = first_result['DOI']
                doi_url = f"https://doi.org/{doi}"
                
        # Assign the DOI number to column "BJ" and the DOI link to column "BK"
        df.at[index, 'DOI'] = doi
        df.at[index, 'DOI Link'] = doi_url

# Save the updated DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False, engine='openpyxl')
