# Customer Segmentation using K-Means

This project is part of the Prodigy Infotech Machine Learning Internship, focusing on creating a K-means clustering algorithm to group customers of a retail store based on their purchase history.

## Author

- **Author:** Muhammad Awais Akhter
- **GitHub:** [awais-akhter](https://github.com/awais-akhter)

## Problem Statement

The task involves implementing a K-means clustering algorithm to group customers of a retail store based on their purchase history. The dataset used for this project can be accessed via the following Kaggle link:
[Dataset Link](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

## Implementation Details

### Libraries Used

- `numpy`, `pandas`, `matplotlib`, `seaborn`: Data manipulation and visualization
- `OneHotEncoder` and `StandardScaler` from `sklearn`: Data preprocessing
- `KMeans` from `sklearn.cluster`: K-means clustering algorithm
- `PCA` from `sklearn.decomposition`: Dimensionality reduction
- `silhouette_score` from `sklearn.metrics`: Evaluation metric for clustering

### Workflow

- **Data Loading**: Loaded the customer dataset from Kaggle.
- **Data Preprocessing and Visualization**: Checked for missing values, performed one-hot encoding for categorical features, scaled numerical features, and visualized the data using pair plots.
- **Clustering using K-Means Algorithm**:
  - Utilized PCA for dimensionality reduction.
  - Determined the optimal number of clusters using the elbow method and knee locator.
  - Conducted K-means clustering using all features and evaluated the clusters' silhouette coefficient.
  - Used 2 features (Annual Income and Spending Score) for clustering and validated the results.

### Conclusion

The project successfully implemented K-means clustering to group customers based on their purchase behavior. Visualizations, elbow method, and silhouette coefficient were used for cluster evaluation.

## Execution

To run this code locally, follow these steps:
1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).
2. Set up the Jupyter Notebook environment or Python with necessary libraries.
3. Execute the code cells in the provided `Mall_Customer_Segmentation.ipynb` file.

## Acknowledgments

- Kaggle for hosting the dataset used in this project.

Feel free to explore the code and dataset further for insights and improvements!
