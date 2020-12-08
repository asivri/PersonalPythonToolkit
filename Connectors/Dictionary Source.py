import pandas as pd

def create_dataframe(links):

    # Create the dataframe from the csv file
    file_cvt = pd.read_csv(links)

    # Display the first 5 rows
    filter_lines = file_cvt.head(5)
    return filter_lines

##  Return the column values greater than the base number
def column_greater (csv_file, column, base_number):

    # Get the File
    read_dataframe = pd.read_csv(csv_file)
    # Get the column
    read_column = read_dataframe[column]
    # Filter the column only if it's greater
    values = read_dataframe[(read_column > base_number)]
    return values

