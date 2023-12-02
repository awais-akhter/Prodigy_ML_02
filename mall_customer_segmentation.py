# -*- coding: utf-8 -*-
"""Mall_Customer_Segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o10jPceU1ZQSUnYHfCYZf5lFUE3kZbWI

# **Prodigy Infotech - Machine Learning Internship**

### **TASK 4 - Group Customers using K-Means**

### Author : Muhammad Awais Akhter

[![alt text](https://logoeps.com/wp-content/uploads/2014/02/25231-github-cat-in-a-circle-icon-vector-icon-vector-eps.png "Git Hub Link")](https://github.com/awais-akhter)

### Problem Statement: Create a K-means clustering algorithm to group customers of a retail store based on their purchase history.

##### Dataset link :- https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

### Importing Data
"""

# Importing Basic Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the csv file
customer_data = pd.read_csv("PRODIGY_ML_02/Mall_Customers.csv")

customer_data

"""This is the customer dataset we will be working on. It has 4 features and one ID column.
The features are:


1. Numerical Features


> *   Age
*   Annual Income
*   Spending Score




2. Categorial Features


> *   Gender




"""

# Summary of the data
customer_data.describe()

"""### Data Preprocessing and Visualization

#### Missing data
"""

# Checking for missing values
customer_data.isna().sum()

"""There is no missing data"""

customer_data.head()

"""#### Pairplot"""

numerical_columns = ["Age", "Annual Income (k$)","Spending Score (1-100)"]
categorical_columns = ["Gender"]

# Visulaizing the relation between all features
sns.pairplot(customer_data[numerical_columns])
plt.show()

"""#### Encoding the Categorical features using OneHotEncoder("""

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
encoded_customer_data = ohe.fit_transform(customer_data[categorical_columns])
encoded_df = pd.DataFrame(encoded_customer_data.toarray(), columns=ohe.get_feature_names_out(categorical_columns))
encoded_df

customer_data.drop('Gender', axis = 1, inplace = True)

customer_data_enc = pd.concat([customer_data, encoded_df], axis = 1)
customer_data_enc.head()

customer_data_enc.set_index("CustomerID", inplace=True)

customer_data_enc.head()

"""#### Scaling the data using StandardScaler()"""

from sklearn.preprocessing import StandardScaler

std_sc = StandardScaler()
def MyStandardScaler(df, col_names):
    features = df[col_names]
    std_sc.fit(features.values)
    features = std_sc.transform(features.values)
    df[col_names] = features
    return df

customer_data_enc_scaled = MyStandardScaler(customer_data_enc, numerical_columns)
customer_data_enc_scaled

"""#### Splitting the data to train and test sets"""

from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(customer_data_enc_scaled, test_size = 0.2, random_state=42)

X_train.shape, X_test.shape

"""## USING KMEANS CLUSTERING"""

from sklearn.cluster import KMeans
np.random.seed(0)

"""### Clustering using all features by feature reduction using PCA"""

from sklearn.decomposition import PCA

pca = PCA(n_components = 2)

X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

"""#### Using Elbow Plot to find optimal number of clusters"""

wcss = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, n_init = 10)
    kmeans.fit(X_train_reduced)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.title('Elbow Method')
plt.show()

"""#### Using Knee Locator to find the knee/elbow point"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install kneed
from kneed import KneeLocator

kneeL = KneeLocator(range(1,11),wcss,curve = "convex", direction = "decreasing")

kneeL.elbow

"""Hence, We use number of clusters = 4

#### Doing the actual KMeans Clustering
"""

num_clusters = 4

kmeans = KMeans(n_clusters=num_clusters, n_init = 'auto')

kmeans.fit(X_train_reduced)

labels = kmeans.labels_
centers = kmeans.cluster_centers_
X_train_reduced

plt.scatter(X_train_reduced[:,0], X_train_reduced[:,1],c = labels)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('K-means Clustering (PCA-reduced Space)')
plt.show()

"""As we can see there are 4 distinct groups of customers which is clustered by using our KMeans Algorithm.

#### Evaluating the clustering using Silhouette Coefficient
"""

from sklearn.metrics import silhouette_score

sil_coeff = []
for k in range(2,12):
        kmeans_eval = KMeans(n_clusters=k,n_init='auto')
        kmeans_eval.fit(X_train_reduced)
        sil = silhouette_score(X_train_reduced,kmeans_eval.labels_)
        sil_coeff.append(sil)

plt.plot(range(2,12),sil_coeff)
plt.xticks(range(2,12))
plt.xlabel('No. of clusters')
plt.ylabel('Silhouette Coefficient')
plt.show()

"""Here, the optimal number of clusters is varying on every run. This discrepancy is potentially due to the dimensionality reduction (PCA).
So, we use 2 actual features to perform clustering.

### Clustering using 2 features : Annual Income and Spending Score
"""

X_train.head()

X_train_new = X_train[["Annual Income (k$)" , "Spending Score (1-100)"]]
X_test_new = X_test[["Annual Income (k$)" , "Spending Score (1-100)"]]

"""#### Elbow Plot"""

wcss2 = []
for k in range(1,11):
    kmeans2 = KMeans(n_clusters=k, n_init = 10)
    kmeans2.fit(X_train_new)
    wcss2.append(kmeans2.inertia_)

plt.plot(range(1,11), wcss2)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.title('Elbow Method')
plt.show()

"""#### Knee Locator"""

kneeL2 = KneeLocator(range(1,11),wcss2,curve = "convex", direction = "decreasing")

kneeL2.elbow

"""We use number of clusters = 5

#### KMeans
"""

num_clusters2 = 5

kmeans2 = KMeans(n_clusters = num_clusters2, n_init = 10)

"""##### For training data"""

kmeans2.fit(X_train_new)
labels2 = kmeans2.labels_
centers2 = kmeans2.cluster_centers_
X_train_new

plt.scatter(X_train_new["Annual Income (k$)"], X_train_new["Spending Score (1-100)"],c = labels2)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('K-means Clustering using 2 features')
plt.show()

"""##### For test data"""

kmeans2.fit(X_test_new)
labels2 = kmeans2.labels_
centers2 = kmeans2.cluster_centers_

plt.scatter(X_test_new["Annual Income (k$)"], X_test_new["Spending Score (1-100)"],c = labels2)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('K-means Clustering using 2 features')
plt.show()

"""#### Silhouette Coefficient"""

sil_coeff2 = []
for k in range(2,12):
        kmeans_eval2 = KMeans(n_clusters=k,n_init='auto')
        kmeans_eval2.fit(X_train_new)
        sil2 = silhouette_score(X_train_new,kmeans_eval2.labels_)
        sil_coeff2.append(sil2)

plt.plot(range(2,12),sil_coeff2)
plt.xticks(range(2,12))
plt.xlabel('No. of clusters')
plt.ylabel('Silhouette Coefficient')
plt.show()

"""As we can see highest Silhouette Coefficient is when number of clusters = 5. This means our assumption of 5 clusters turned out to be correct.

### END OF THE CODE
"""