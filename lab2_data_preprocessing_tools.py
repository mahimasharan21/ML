# -*- coding: utf-8 -*-
"""Copy of Lab2  data_preprocessing_tools.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/18iTmZNpg8a4hl_xwHQAHOiTTjeGJ2NXe
# Data Preprocessing Tools
"""

import pandas as pd
raw_data = {'Country': ['France', 'Spain ', 'Germany'], 
        'Age': [44, 27,30], 
        'Salary': [72000, 48000, 54000], 
        'Purchased': ['No','Yes', 'No'],
}
df = pd.DataFrame(raw_data, columns = ['Country', 'Age', 'Salary', 'Purchased'])
df

"""## Importing the libraries"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('/content/sample_data/Data.csv')
X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values
z = dataset.iloc[:, 3].values

print(X)

print(y)

"""## Taking care of missing data"""

import numpy as np
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:4])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)

"""## Encoding categorical data
### Encoding the Independent Variable
"""

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

"""As you can see from the snippet above, we’ll name the transformer simply “encoder.” We’re using the OneHotEncoder() constructor to provide a new instance as the estimator. And then we’re specifying that only the first column has to be transformed. We’re also making sure that the remainder columns are passed through without any changes."""

print(X)

"""### Encoding the Dependent Variable"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

print(X_train)

print(X_test)

print(y_train)

print(y_test)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])

print(X_train)

print(X_test)
