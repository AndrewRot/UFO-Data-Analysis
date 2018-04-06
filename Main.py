import ConvertToSeconds
import FilterByDate
import GraphSightings
import DecisionTree
import matplotlib.pyplot as plt


def main():

    # Extract and Filter the data
    ConvertToSeconds.convert_duration_to_seconds()
    FilterByDate.filter_by_date()

    # Plot box plots and time series
    GraphSightings.graph_sightings_by_shape()
    GraphSightings.graph_sightings_by_shape_per_year()
    GraphSightings.graph_sightings_by_state()
    GraphSightings.normalize_sightings_by_state()

    # Generate decision tree
    DecisionTree.generate_decision_tree()

    plt.show()


main()
