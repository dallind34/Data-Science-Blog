import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('Top_Tech_House_Songs_From_Playlists.csv')

# EDA

most_popular_key = data['Key'].mode()[0]
average_tempo = data['Tempo'].mean()
average_danceability = data['Danceability'].mean()
average_loudness = data['Loudness'].mean()
average_energy = data['Energy'].mean()
most_popular_mode = data['Mode'].mode()[0]
average_valence = data['Valence'].mean()
average_speechiness = data['Speechiness'].mean()

analysis_results = {
    'Most Popular Key': most_popular_key,
    'Average Tempo (BPM)': average_tempo,
    'Average Danceability': average_danceability,
    'Average Loudness (dB)': average_loudness,
    'Average Energy': average_energy,
    'Most Popular Mode': most_popular_mode,
    'Average Valence': average_valence,
    'Average Speechiness': average_speechiness
}

key_mapping = {
    0: 'C', 1: 'C♯ / D♭', 2: 'D', 3: 'D♯ / E♭', 4: 'E', 5: 'F',
    6: 'F♯ / G♭', 7: 'G', 8: 'G♯ / A♭', 9: 'A', 10: 'A♯ / B♭', 11: 'B'
}

key_counts = data['Key'].value_counts()


print("Number of songs in each key:")
for key, count in key_counts.items():
    print(f"{key_mapping[key]} = {count} songs")

print("\nNumber of songs in each mode:")
mode_counts = data['Mode'].value_counts()
for mode, count in mode_counts.items():
    print(f"{mode} = {count} songs")

for metric, value in analysis_results.items():
    print(f"{metric}: {value}")



plt.figure(figsize=(10, 6))
sns.histplot(data['Tempo'], bins=40, kde=True, color="skyblue")
plt.xlim(115, 140) 
plt.title('Distribution of Tempo for Tech House Songs')
plt.xlabel('Tempo (BPM)')
plt.ylabel('Count')
plt.show()

data['Key_Name'] = data['Key'].map(key_mapping)

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Key_Name', order=[key_mapping[i] for i in range(12)], palette="viridis")
plt.title('Distribution of Keys for Tech House Songs')
plt.xlabel('Key')
plt.ylabel('Count')
plt.show()

# ---- LINEAR REGRESSION MODEL ----


X = data[['Tempo', 'Danceability', 'Energy', 'Loudness', 'Valence', 'Speechiness']]
y = data['Popularity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print("\n---- Linear Regression Model ----")
print(f"Mean Squared Error (MSE): {mse_linear}")
print(f"R-squared: {r2_linear}")

coefficients = pd.DataFrame(linear_model.coef_, X.columns, columns=['Coefficient'])
print("\nFeature Coefficients (Linear Regression):")
print(coefficients)

# ---- RANDOM FOREST MODEL ----

rf_model = RandomForestRegressor(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
mae_rf = mean_absolute_error(y_test, y_pred_rf)

print("\n---- Random Forest Model ----")
print(f"Mean Squared Error (MSE): {mse_rf}")
print(f"R-squared: {r2_rf}")
print(f"Mean Absolute Error (MAE): {mae_rf}")

feature_importance = pd.DataFrame(rf_model.feature_importances_, index=X.columns, columns=['Importance']).sort_values(by='Importance', ascending=False)
print("\nFeature Importances (Random Forest):")
print(feature_importance)

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance.index, y=feature_importance['Importance'])
plt.title('Feature Importances for Predicting Popularity (Random Forest)')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.show()

