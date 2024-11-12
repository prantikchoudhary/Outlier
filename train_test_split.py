from sklearn.model_selection import train_test_split

# Example dataset
X = data[['Weather condition']]  # Assume this is your input feature
y = data['No of cab bookings']    # Target variable

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
