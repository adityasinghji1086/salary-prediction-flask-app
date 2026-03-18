import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# load data
data = pd.read_csv("data/salary_data.csv")

X = data[["YearsExperience"]]
y = data["Salary"]

# train model
model = LinearRegression()
model.fit(X, y)

# create folder if not exists
os.makedirs("model", exist_ok=True)

# save model
pickle.dump(model, open("model/model.pkl", "wb"))

print("Model trained & saved")
