import joblib

# Save the model to a file to run later on testing data
joblib.dump(best_rf_model, 'taxi_demand_prediction_model.pkl')
