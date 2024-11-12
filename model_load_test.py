from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Example dataset
X = data[['Weather condition']]  # Assume this is your input feature
y = data['No of cab bookings']    # Target variable

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)

# Save the Random Forest model to a file
joblib.dump(random_forest_model, 'random_forest_model.pkl')

# Load the saved Random Forest model
loaded_model = joblib.load('random_forest_model.pkl')

# Load the new test data (ensure it’s in the same format as the training data)
test_data = pd.read_csv('new_test_data.csv')
X_test_new = test_data[['Weather condition']]  # Replace with actual features

# Make predictions using the loaded model
predictions = loaded_model.predict(X_test_new)

# Store predictions in the test data for analysis
test_data['Predicted_Demand'] = predictions

# Print or analyze the predictions
print(test_data[['date and time', 'No of cab bookings', 'Predicted_Demand']])

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate evaluation metrics if actual values are available (Optional)
actual_demand = test_data['No of cab bookings']
mae = mean_absolute_error(actual_demand, predictions)
mse = mean_squared_error(actual_demand, predictions)
r2 = r2_score(actual_demand, predictions)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")
