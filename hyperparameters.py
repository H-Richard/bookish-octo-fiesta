"""
CSCC11 - Introduction to Machine Learning, Fall 2020, Assignment 2
B. Chan, E. Franco, D. Fleet

This file specifies the hyperparameters for the two real life datasets.
Note that different hyperparameters will affect the runtime of the 
algorithm.
"""

# ====================================================
# TODO: Use Validation Set to Tune hyperparameters for the Amazon dataset
# Use Optimal Parameters to get good accuracy on Test Set
AMAZON_HYPERPARAMETERS = {
    "num_trees": 1,
    "features_percent": 1,
    "data_percent": 1,
    "max_depth": 10,
    "min_leaf_data": 10,
    "min_entropy": 1,
    "num_split_retries": 10
}
# ====================================================

# ====================================================
# TODO: Use Validation Set to Tune hyperparameters for the Occupancy dataset
# Use Optimal Parameters to get good accuracy on Test Set
OCCUPANCY_HYPERPARAMETERS = {
    "num_trees": 1,
    "features_percent": 1,
    "data_percent": 1,
    "max_depth": 10,
    "min_leaf_data": 10,
    "min_entropy": 1,
    "num_split_retries": 10
}
# ====================================================
