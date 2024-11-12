import pandas as pd
import matplotlib.pyplot as plt

# Get feature importance from the Random Forest Regressor Model
feature_importance = random_forest_model.feature_importance
feature_names = X_train.columns

#Plot Feature Importance
plt.figure(figsize=(10,6))
plt.barh(importance_df['Feature'],importance_df['Importance'],colour='teal')

plt.xlabel('Importance')
plt.title('Feature Importance in Random Forest Model')
plt.gca().invert_yaxis()
plt.show()

