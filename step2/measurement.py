from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Load dataset
df = pd.read_csv('measurements.csv')

# Feature matrix (with column names)
X = df[['chest_cm', 'waist_cm', 'hip_cm']]
y = df['size']

# Train classifier
clf = DecisionTreeClassifier().fit(X, y)

# Predict using a DataFrame with same column names
user = pd.DataFrame([[92, 80, 96]], columns=['chest_cm', 'waist_cm', 'hip_cm'])
print(clf.predict(user))  # Output: ['M']

