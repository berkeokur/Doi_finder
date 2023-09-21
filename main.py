import pandas as pd
from habanero import Crossref
from tqdm import tqdm
from fuzzywuzzy import fuzz

def get_user_input(prompt, valid_columns):
    while True:
        user_input = input(prompt)
        if user_input in valid_columns:
            return user_input
        else:
            print("Column not found. Try again.")

def main():
    # Create a CrossRef client
    cr = Crossref()

    # Initialize df as None outside the try-except block
    df = None

    # Ask the user for the file name and validate its existence
    while True:
        filename = input("Enter the file name: ")
        try:
            df = pd.read_excel(f"{filename}")
            break
        except FileNotFoundError:
            print("File not found. Try again.")

    # Ask the user for column names and validate their existence
    if df is not None:
        title_column = get_user_input("Enter the column name containing the article title: ", df.columns)
        first_author_column = get_user_input("Enter the column name containing the first author's name (leave blank if not applicable): ", df.columns)
        doi_column = get_user_input("Enter the column name containing the DOI number: ", df.columns)
        doi_link_column = get_user_input("Enter the column name containing the DOI link: ", df.columns)

    # Initialize a new DataFrame for the updated data
    updated_df = df.copy()

    # Temporary row limit
    df = df.head(40)

    # Create a tqdm progress bar
    with tqdm(total=len(df)) as pbar:
        # Create a dictionary to store query and result information
        query_results = {}

        # Iterate over the selected rows
        for index, row in df.iterrows():
            article_title = row[title_column]
            first_author_name = row[first_author_column] if first_author_column else ""

            if pd.notna(article_title):
                if pd.notna(first_author_name):
                    query = f"title:{article_title} author:{first_author_name}"
                else:
                    query = f"title:{article_title}"
                try:
                    results = cr.works(query=query, limit=10)

                    # Convert the article title to lowercase
                    article_title_lower = article_title.lower()

                    # Initialize variables for closest result
                    closest_result = None
                    closest_score = None

                    # Iterate through the results to find the closest match
                    for result in results['message']['items'][:10]:
                        result_title_lower = result['title'][0].lower()
                        similarity_score = fuzz.ratio(article_title_lower, result_title_lower)

                        if closest_result is None or similarity_score > closest_score:
                            closest_result = result
                            closest_score = similarity_score

                    # Check if a close match was found
                    if closest_result is not None:
                        doi = closest_result.get('DOI', '')
                        doi_url = f"https://doi.org/{doi}"
                        updated_df.at[index, doi_column] = doi
                        updated_df.at[index, doi_link_column] = doi_url

                except Exception as e:
                    print(f"An error occurred while querying CrossRef: {str(e)}")

            # Update the progress bar
            pbar.update(1)

    # Save the updated DataFrame to a new Excel file
    output_filename = input("Enter the output file name (or leave blank to overwrite the input file): ").strip()
    if not output_filename:
        output_filename = filename
    updated_df.to_excel(output_filename, index=False, engine='openpyxl')
    print(f"Updated data saved to {output_filename}")

if __name__ == "__main__":
    main()
