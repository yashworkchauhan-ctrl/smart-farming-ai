import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# load dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# features and target
X = data.drop("label", axis=1)
y = data["label"]

# train model
model = RandomForestClassifier()
model.fit(X, y)

# save model
pickle.dump(model, open("models/crop_model.pkl", "wb"))

print("Model trained and saved successfully!")