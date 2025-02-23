from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import numpy as np
import random
from faker import Faker
from diffusers import StableDiffusionPipeline
import torch

app = Flask(__name__)
faker = Faker()

def generate_tabular_data(columns, num_rows):
    data = {}
    for col in columns:
        col_name, col_type = col["name"], col["type"]
        if col_type == "int":
            data[col_name] = np.random.randint(1, 100, num_rows)
        elif col_type == "float":
            data[col_name] = np.random.rand(num_rows) * 100
        elif col_type == "str":
            data[col_name] = [faker.name() for _ in range(num_rows)]
        elif col_type == "date":
            data[col_name] = [faker.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y") for _ in range(num_rows)]
    
    df = pd.DataFrame(data)
    df.to_csv("static/tabular_data.csv", index=False)
    return "static/tabular_data.csv"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
