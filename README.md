# Synthetic-Data-Generator

## Project Overview

This project focuses on generating synthetic data for various applications, including machine learning, data analysis, and privacy-preserving research. The generated data maintains statistical properties of real-world datasets while ensuring anonymity and data security. It supports both structured and unstructured data generation.

## Features

1. Generates synthetic data for structured and unstructured formats

2. Supports multiple data types (numerical, categorical, text, etc.)

3. Customizable data generation based on user-defined constraints

4. Ensures statistical similarity with real-world datasets

5. Provides visualization tools for data analysis

## Installation

To use this project, clone the repository and install the required dependencies:
### Clone the repository
https://github.com/Adithya-Siddam/Synthetic-Data-Generator.git
### Navigate to the project directory
cd synthetic-data-generation

### Install dependencies
pip install -r requirements.txt

### Usage
**Run the main script to generate synthetic data:**

python generate_data.py --config config.json


### Output

The generated data will be saved in the specified output format (CSV, JSON, etc.) in the output/ directory.

### Dependencies

**This project requires the following Python libraries:**

1. Pandas

2. NumPy

3. Scikit-learn

4. Faker (for synthetic text data)

**You can install them using:**

pip install pandas numpy scikit-learn faker
