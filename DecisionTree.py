import matplotlib.pyplot as plt
import GlobalData as gd
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import math
import sklearn.datasets as datasets
from functools import reduce
from sklearn.externals.six import StringIO
from IPython.display import Image
from IPython.display import display
from sklearn.tree import export_graphviz
import pydotplus


def generate_decision_tree():

    data = pd.read_csv('data/master_transform_2.csv')

    # replace empty cells with NaN for truncation
    data['State'].replace('', np.nan, inplace=True)
    data['Time'].replace('', np.nan, inplace=True)
    data['Shape'].replace('', np.nan, inplace=True)
    data['Year'].replace('', np.nan, inplace=True)

    # drop Nans
    data.dropna(subset=['State'], inplace=True)
    data.dropna(subset=['Time'], inplace=True)
    data.dropna(subset=['Shape'], inplace=True)
    data.dropna(subset=['Year'], inplace=True)


    # split the data into two sets
    # Training set consists of all sightings made between January 1, 2005 and December 31,
    #  2013. Test set consists of all sightings made between January 1, 2014 and
    # September 22, 2016
    training_data_array = []
    test_data_array = []

    for index, row in data.iterrows():
        year = int(row["Year"])
        if 2005 <= year <= 2013:
            training_data_array.append(row)
        else:
            test_data_array.append(row)

    # use helper function to extract data
    training_data = extract_fields(pd.DataFrame(training_data_array))
    testing_data = extract_fields(pd.DataFrame(test_data_array))

    # Reduce list / flatten to then feed through the decision tree
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(pd.get_dummies(pd.DataFrame(training_data["extracted_data"])), training_data["extracted_labels"])

    x = decision_tree.score(pd.get_dummies(pd.DataFrame(testing_data["extracted_data"])), testing_data["extracted_labels"])
    print("Accuracy of decision tree: ", x)

    # generate decision tree graphic
    dot_data = StringIO()
    export_graphviz(decision_tree, out_file=dot_data, filled=True, rounded=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())

    return decision_tree


# separate data from their labels
def extract_fields(data):

    # transform the data and extract info we want
    extracted_data = []
    extracted_labels = []

    for index, row in data.iterrows():

        # extracted_region
        extracted_region = "a"
        if row["State"] in gd.us_region:
            extracted_region = gd.us_region[row["State"]]
            # print(extracted_region)

        # Extract the hour on : and grab first index
        extracted_hour = row["Time"].split(":")[0]
        time_integer = math.floor(int(extracted_hour) / 6)
        time_of_day = gd.time_of_day[time_integer]

        shape_label = row["Shape"]

        new_row = [extracted_region, time_of_day]
        extracted_data.append(new_row)

        extracted_labels.append(shape_label)

    # wrap up the package of data - data and their labels - to return to the big boy class
    data_package = {
        "extracted_data": extracted_data,
        "extracted_labels": extracted_labels
    }

    return data_package


