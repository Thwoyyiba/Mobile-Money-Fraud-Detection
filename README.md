### Machine Learning Project
Title of ML Project: Fraud Detection in Mobile Money Transactions
Name: Thwoyyiba Nasreen
Organization: Entri Elevate 
Date: 26/06/2025
## Introduction
In the modern digital financial system, online transactions have become an essential part of daily life, providing fast and convenient payment solutions. However, the rapid growth of digital transactions has also increased the risk of fraudulent activities, causing financial losses and security challenges for individuals and organizations. Traditional fraud detection methods often struggle to identify complex patterns and new types of fraudulent behavior.

Machine learning provides an effective approach for detecting fraud by analyzing large volumes of transaction data, identifying hidden patterns, and detecting unusual activities. This project focuses on developing a machine learning-based fraud detection system that classifies transactions as fraudulent or legitimate by studying various transaction attributes and behavioral patterns. The proposed model aims to improve fraud identification accuracy and support faster decision-making in financial security systems.
## Problem Statement
Fraudulent transactions have become a major concern in the financial sector due to the increasing use of digital payment systems and online banking services. Identifying fraudulent activities is challenging because fraud patterns are constantly changing and may appear similar to legitimate transactions. Traditional detection approaches based on fixed rules are often unable to detect complex and hidden fraud patterns effectively.

The objective of this project is to develop a machine learning model that can analyze transaction-related features and accurately classify transactions as fraudulent or genuine. By using historical transaction data, the model aims to identify suspicious activities, reduce financial risks, and improve the efficiency of fraud detection systems while minimizing incorrect predictions.
## Objective
To develop a classification model that predicts whether a transaction is fraudulent or legitimate(genuine).
## Data Description 
Source:  https://data.world/wayvy/synthetic-fraud-detection-dataset ,csv file
### Features:
step → transaction time step, Represents a unit of time where 1 step equals 1 hour.

type → transaction type

amount → transaction amount

oldbalanceOrg → sender previous balance

newbalanceOrig → sender new balance

oldbalanceDest → receiver previous balance

newbalanceDest → receiver new balance


isFlaggedFraud → existing fraud flag/Indicates if the transaction was flagged as suspicious.

Time of day → transaction timing

nameOrig →	Unique identifier of the account/customer who initiated the transaction. It helps 
track the sender's transaction activity.

branch  →	Represents the bank branch or transaction location associated with the account or transaction.

nameDest →	Unique identifier of the account/customer receiving the transaction amount. It helps analyze the receiver's transaction behavior.

unusallogin	 →Indicates whether the login activity is unusual or suspicious compared to normal user behavior. It can help identify possible unauthorized access.
### Target Variable:
 A binary label indicating whether the transaction is fraudulent (1) or not (0).
 ## Methodology
The project follows a structured approach:
### 1. Data Preprocessing & Cleaning
Data preprocessing is an important step in preparing the dataset for machine learning. The raw transaction data was analyzed and cleaned to improve data quality and model performance.

#### Handling Missing Values:
The dataset was checked for missing or null values. Appropriate methods were applied to handle missing data and ensure the dataset was complete for analysis.

#### Removing Duplicate Records:
Duplicate transaction records were identified and removed to avoid repeated data affecting the model's learning process.

#### Data Type Conversion:
Features such as dateoftransaction were converted into appropriate formats to extract useful information and improve analysis.

#### Encoding Categorical Features:
Categorical variables such as branch, accttype, nameOrig, and nameDest were converted into numerical values using encoding techniques like Label Encoding to make them suitable for machine learning algorithms.

#### Handling Outliers:
Numerical features such as transaction amount and balance-related values were analyzed using statistical methods and visualizations to identify unusual values.

#### Feature Selection:
Relevant features were selected to improve model performance and remove unnecessary information.

After preprocessing and cleaning, the dataset was transformed into a structured format suitable for training and evaluating the fraud detection model.
### 2. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the structure, distribution, and relationships within the transaction dataset. The main goal of EDA is to identify important patterns, detect anomalies, and understand the factors that influence fraudulent transactions.

#### Data Distribution Analysis:
The distribution of numerical features such as transaction amount, account balances, and transaction time was analyzed using statistical methods and visualization techniques like histograms.

#### Fraud Transaction Analysis:
The target variable isFraud was analyzed to understand the number of fraudulent and legitimate transactions. A count plot was used to visualize the class distribution and identify imbalance in the dataset.

#### Feature Relationship Analysis:
Correlation analysis was performed to identify relationships between numerical features and understand which attributes have more influence on fraud detection.

#### Categorical Feature Analysis:
Features such as branch, accttype, and transaction-related categories were analyzed using bar charts and count plots to identify patterns in different groups.

#### Outlier Detection:
Box plots were used to detect unusual transaction amounts or balance changes that may indicate suspicious activities.

#### Visualization Insights:
Various visualizations including histogram, box plot, heatmap, and count plot were used to gain better insights into transaction behavior and identify important patterns related to fraudulent activities.

The EDA process helped in understanding the dataset
### 3. Feature Engineering

Feature engineering was performed to transform the raw transaction data into meaningful features that improve the performance of the machine learning model. The process involved converting categorical data into numerical format and creating additional features to capture important transaction patterns.

#### Encoding Categorical Features
  Categorical variables such as `branch`, `accttype`, `nameOrig`, and `nameDest` were converted into numerical values using encoding techniques. Label Encoding was applied to transform categorical values into machine-readable numerical representations.

#### Date Feature Transformation
  The `dateoftransaction` feature was processed to extract useful information such as transaction day, month, and time-related patterns, which helps the model understand transaction behavior.

#### Creating New Features
  New features were generated from existing transaction details to improve fraud detection, such as transaction frequency, unusual login indicators, and balance difference between previous and current account values.

#### Feature Selection:
  Important features were selected based on their relevance and contribution to fraud prediction. Unnecessary or less informative features were removed to improve model efficiency.

After feature engineering, the dataset was converted into a suitable format for training machine learning models and improving fraud detection accuracy.
### 4. Feature Scaling

Feature scaling was applied to ensure that numerical features have a similar range and contribute equally during the machine learning model training process. Scaling helps improve model performance, especially for algorithms that are sensitive to feature magnitude.

#### Standardization
  Numerical features such as `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, and `newbalanceDest` were standardized using **StandardScaler**. This technique transforms the data based on the mean and standard deviation, bringing values into a common scale.

#### Normalization
  **MinMaxScaler** can be applied to transform numerical features into a range between 0 and 1. This helps maintain consistent feature ranges and improves model convergence.

#### Handling Outliers

Outliers were detected using the **IQR method** and treated using the **capping technique**. Extreme values in numerical features were limited to the upper and lower IQR boundaries instead of removing them, helping to reduce their impact on the machine learning model.


After applying feature scaling, the processed dataset was prepared for machine learning model training with improved accuracy and efficiency.
### 5. Model Building

The processed dataset was divided into training and testing sets to evaluate the performance of the machine learning models. The training dataset was used to train the models, while the testing dataset was used to measure their prediction accuracy.

* **Data Splitting:**
  The dataset was split into training and testing data using the `train_test_split` method.

* **Model Selection:**
  Different classification algorithms were applied for fraud detection, including:

   * Random Forest Classifier
   * Logistic Regression
   * Support Vector Machine (SVM)
   * K-Nearest Neighbors (KNN)
   * Decision Tree
   

* **Model Training:**
  The selected machine learning models were trained using the training dataset to learn patterns and classify transactions as fraudulent or legitimate.

The performance of each model was compared to select the best-performing model for fraud detection.
### 6. Model Evaluation

The trained machine learning models were evaluated using different classification metrics to measure their performance in detecting fraudulent transactions.

#### Evaluation Metrics:
  The models were evaluated using:

  * Accuracy Score
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

#### Model Comparison:
  The performance of multiple models was compared to identify the best model based on prediction accuracy and ability to correctly detect fraudulent transactions.

#### Final Model Selection:
  The model with the best evaluation results was selected as the final fraud detection model for predicting whether a transaction is fraudulent or legitimate.
### 7. Hyperparameter Tuning

Hyperparameter tuning was performed to improve the performance of the machine learning model by optimizing important model parameters. Different parameter combinations were tested to identify the best configuration for accurate fraud detection.

#### GridSearchCV:
  GridSearchCV was used to evaluate multiple combinations of hyperparameters and select the best-performing parameters based on validation results.

#### RandomizedSearchCV:
  RandomizedSearchCV was applied to test random parameter combinations efficiently and improve model performance with reduced computation time.

#### Model Optimization:
  The tuned model was compared with the original model, and the optimized parameters were selected to achieve better prediction accuracy and fraud detection performance.
  ### 8. Model Deployment

The final trained fraud detection model was deployed to make real-time predictions on new transaction data.

#### Model Saving:
  The trained machine learning model was saved using the **Joblib** library as a `.pkl` file. This allows the model to be loaded and used for future predictions without retraining.

#### User Interface Development:
  A simple web-based user interface was created using **Flask** to allow users to enter transaction details and receive fraud prediction results.

#### Real-World Prediction:
  The deployed application takes new transaction inputs, processes the data using the same preprocessing steps, and predicts whether the transaction is fraudulent or legitimate.

The deployment process helps convert the machine learning model into a practical application for real-time fraud detection.
##  Conclusion
This project focused on developing a machine learning-based fraud detection system to identify fraudulent transactions from financial transaction data. The dataset was preprocessed, analyzed, and used to train multiple classification models. The performance of the models was evaluated using metrics such as accuracy, precision, recall, F1-score, and confusion matrix.

The selected model was able to identify patterns in transaction behavior and classify transactions as fraudulent or legitimate. By applying feature engineering, scaling, and hyperparameter tuning, the model performance was improved.

The developed fraud detection system can be practically used by financial institutions, digital payment platforms, and online services to detect suspicious transactions, reduce financial losses, and improve transaction security. Future improvements can include using advanced algorithms, real-time data processing, and continuous model updates to handle new fraud patterns.

## References

Dataset source: Data world :https://data.world/wayvy/synthetic-fraud-detection-dataset  in CSV format.
