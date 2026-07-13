import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# dataset load
data = pd.read_csv("data/crop_yield.csv")

X = data.drop("yield", axis=1)
y = data["yield"]

# model train
model = RandomForestRegressor()
model.fit(X, y)

# save model
pickle.dump(model, open("models/yield_model.pkl", "wb"))

print("Yield model trained and saved!")