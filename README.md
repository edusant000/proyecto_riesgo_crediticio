# Credit Scoring System with Business Profit Optimization

## Project Overview

This project presents a comprehensive Machine Learning solution for credit risk assessment, based on the "Default of Credit Card Clients in Taiwan" dataset. The goal is not only to predict the probability of default but also to optimize business decisions to maximize profitability.

Two main predictive models are developed:

1.  A **classification model** to predict whether a client will default on their payment next month.
2.  A **regression model** to estimate the payment amount a client will make.

The approach is distinguished by its rigorous temporal validation, creation of business-relevant features, and model optimization based on financial metrics rather than traditional technical metrics.

## Dataset

The data used for this project is the "Default of Credit Card Clients in Taiwan" dataset from the UCI Machine Learning Repository.

  * **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)

## Key Features

  * **Business-Driven Classification Model**: The final `Random Forest` model was optimized using a cost matrix to maximize an estimated potential profit of **$201,400**.
  * **Advanced Regression Model (`Hurdle Model`)**: A two-stage model was implemented to accurately handle data with excess zeros, achieving an **R² of 0.69**.
  * **Data Leakage Prevention**: Strict temporal validation (`TimeSeriesSplit` and ordering by ID as a time proxy) was used in all phases to ensure the model's robustness and real-world viability.
  * **Relevant Feature Engineering**: Creation of features that capture trends, utilization ratios, and historical client behavior.
  * **Interpretability & Stability Analysis**: Use of SHAP for prediction interpretability and PSI analysis to monitor future variable stability.

## Business Problem & Objectives

Ineffective credit risk management can lead to significant financial losses and the loss of valuable customers. This project addresses this problem with two clear objectives:

1.  **Classification (Default Risk)**: To predict in advance which clients have a high probability of defaulting on their payments in order to take preventive actions and mitigate losses.
2.  **Regression (Payment Amount)**: To estimate the amount clients will pay to improve cash flow management and personalize communication and collection strategies.

## Methodology & Pipeline

The project follows a structured data science workflow:

1.  **Exploratory Data Analysis (EDA)**: Identification of outliers, inconsistencies in categorical variables, and a significant class imbalance in the target variable.
2.  **Feature Engineering**: Creation of new variables such as `utilization_rate`, `payment_ratio`, `bill_amt_slope`, and temporal aggregates to enrich the data.
3.  **Modeling**:
      * **Classification**: Multiple algorithms were tested (Logistic Regression, Random Forest, XGBoost), and the best model (`Random Forest`) was selected based on an **economic profit function**.
      * **Regression**: A **Hurdle Model** was implemented to overcome the limitations of standard regression models with data containing many zeros.
4.  **Validation & Evaluation**: `TimeSeriesSplit` was used for cross-validation, and models were evaluated with a combination of technical (ROC-AUC, R²) and business (Profit Curve) metrics.

## Key Results & Performance

| Model | Key Metric | Value |
| :--- | :--- | :--- |
| **Classification (Random Forest)** | **Maximum Potential Profit** | **$201,400** |
| | ROC-AUC | 0.80 |
| **Regression (Hurdle Model)** | **R² Score** | **0.69** |
| | RMSE | $10,210 |

## Repository Structure

```
├── data/
│   ├── raw/
│   │   └── default_of_credit_card_clients.xls
│   └── processed/
│       ├── credit_card_clients_clean.csv
│       └── features_clasificacion.csv
│       └── features_regresion.csv
├── notebooks/
│   ├── 01_Analisis_Exploratorio.ipynb
│   ├── 02_Ingenieria_de_Caracteristicas.ipynb
│   ├── 03_Modelado_Clasificacion.ipynb
│   ├── 04_Modelado_Regresion.ipynb
│   └── 05_Modelo_Avanzado.ipynb
├── src/
│   └── (Optional: Python scripts with classes or functions)
├── environment.yml
└── README.md
```

## Setup & Usage

To replicate this project, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/edusant000/proyecto_riesgo_crediticio.git
    cd proyecto_riesgo_crediticio

    ```

2.  **Create the Conda environment from the environment.yaml file:**
    This command will create a new environment with all the necessary dependencies, including the correct Python version.

    ```bash
    conda env create -f environment.yml
    ```

3.  **Activate the newly created environment:**
    You will need to replace your_env_name with the name specified inside the environment.yaml file (it's usually defined at the top of the file under the name: key).

    ```bash
    conda activate your_env_name
    ```

4.  **Run the notebooks:**
    It is recommended to run the notebooks in the `/notebooks` folder in numerical order to replicate the entire workflow, from exploratory analysis to advanced modeling.

## ✍️ Author

**Eduardo Santoyo Castro**

  * [LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/eduardo-santoyo-castro-1b77bb1ab)
  * [GitHub](https://github.com/edusant000?tab=repositories)