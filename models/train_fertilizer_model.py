import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# load dataset
data = pd.read_csv("data/Fertilizer Prediction.csv")

# remove extra spaces from column names
data.columns = data.columns.str.strip()

print("Columns:", data.columns)

# encode categorical columns
le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

data["Soil Type"] = le_soil.fit_transform(data["Soil Type"])
data["Crop Type"] = le_crop.fit_transform(data["Crop Type"])
data["Fertilizer Name"] = le_fert.fit_transform(data["Fertilizer Name"])

# features
X = data[[
    "Temparature",
    "Humidity",
    "Moisture",
    "Soil Type",
    "Crop Type",
    "Nitrogen",
    "Potassium",
    "Phosphorous"
]]

# target
y = data["Fertilizer Name"]

model = DecisionTreeClassifier()

model.fit(X, y)

# save model
pickle.dump(model, open("models/fertilizer_model.pkl", "wb"))

print("✅ Fertilizer model trained successfully")