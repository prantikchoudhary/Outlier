import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file.xlsx'  # Replace with your file path
sheet_name = 'Sheet1'  # Replace with the name of your sheet, if necessary

# Read the Excel file and load only specific columns
# Here, specify the columns you want to export, e.g., 'Date and Time', 'No of cab bookings', 'Weather condition'
columns_to_export = ['Date and Time', 'No of cab bookings', 'Weather condition']
data = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_to_export)

# Display the data variable
print(data)
