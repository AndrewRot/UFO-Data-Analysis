import matplotlib.pyplot as plt
import GlobalData as gd
import pandas as pd
import numpy as np


# A boxplot of the duration of UFO sightings of each shape (one boxplot per shape).
def graph_sightings_by_shape():
    # Now load the data that we want to plot
    data = pd.read_csv('data/master_transform_2.csv', index_col='Date', parse_dates=True)
    duration_shape = data.filter(items=[gd.ColumnName.SHAPE.value, gd.ColumnName.DURATION.value])

    # Circle *************************************************************************
    circle_data_duration = duration_shape[duration_shape[gd.ColumnName.SHAPE.value] == 'Circle']
    circle_data_duration.plot.box(return_type='dict', whis=1.5, showfliers=False)
    plt.title('Duration of UFO Sightings by Shape (Circle)')
    plt.ylabel('Duration (seconds)', fontsize=16)

    # Triangle ***********************************************************************
    triangle_data = duration_shape[duration_shape[gd.ColumnName.SHAPE.value] == 'Triangle']
    triangle_data.plot.box(return_type='dict', whis=1.5, showfliers=False)
    plt.title('Duration of UFO Sightings by Shape (Triangle)')
    plt.ylabel('Duration (seconds)', fontsize=16)

    # Fireball ***********************************************************************
    fireball_data = duration_shape[duration_shape[gd.ColumnName.SHAPE.value] == 'Fireball']
    fireball_data.plot.box(return_type='dict', whis=1.5, showfliers=False)
    plt.title('Duration of UFO Sightings by Shape (Fireball)')
    plt.ylabel('Duration (seconds)', fontsize=16)

    print("Outliers have been removed from the data according to each shape. The three box plots represent the"
          " duration of the sighting according to each shape of the UFO")


# A time series figure with the number of sightings per year (one line per shape
def graph_sightings_by_shape_per_year():

    # Now load the data that we want to plot
    data = pd.read_csv('data/master_transform_2.csv', index_col='Date', parse_dates=True)

    # extract # of sighting each year
    # Circle *************************************************************************
    circle_data_dates = data[data[gd.ColumnName.SHAPE.value] == 'Circle'].filter(items=[gd.ColumnName.YEAR.value])
    circle_data_dates = circle_data_dates['Year'].value_counts().reset_index()
    circle_data_dates.columns = ['Year', 'Count']
    circle_data_dates = circle_data_dates.sort_values(by="Year")
    # print (circle_data_dates)

    # Triangle ***********************************************************************
    triangle_data_dates = data[data[gd.ColumnName.SHAPE.value] == 'Triangle'].filter(items=[gd.ColumnName.YEAR.value])
    triangle_data_dates = triangle_data_dates['Year'].value_counts().reset_index()
    triangle_data_dates.columns = ['Year', 'Count']
    triangle_data_dates = triangle_data_dates.sort_values(by="Year")
    # print(triangle_data_dates)

    # Fireball ***********************************************************************
    fireball_data_dates = data[data[gd.ColumnName.SHAPE.value] == 'Fireball'].filter(items=[gd.ColumnName.YEAR.value])
    fireball_data_dates = fireball_data_dates['Year'].value_counts().reset_index()
    fireball_data_dates.columns = ['Year', 'Count']
    fireball_data_dates = fireball_data_dates.sort_values(by="Year")
    # print(fireball_data_dates)

    compiled_dates = [circle_data_dates, triangle_data_dates, fireball_data_dates]
    plt.figure()
    for frame in compiled_dates:
        plt.plot(frame['Year'], frame['Count'])
        plt.title('UFO Sightings Per Year by Shape')
        plt.ylabel('# of Sightings', fontsize=16)
        plt.xlabel('Year', fontsize=16)


# A bar chart for sightings by state.
def graph_sightings_by_state():
    plt.figure(figsize=[17, 5])
    data = pd.read_csv('data/master_transform_2.csv')
    data = data.filter(items=[gd.ColumnName.STATE.value])
    state_count_data = data['State'].value_counts().reset_index()
    state_count_data.columns = ['State', 'Count']
    state_count_data = state_count_data.sort_values(by="State")

    plt.bar(state_count_data['State'], state_count_data['Count'], align='center', alpha=0.8)
    plt.title('UFO Sightings Per State')
    plt.ylabel('# of Sightings', fontsize=16)
    plt.xlabel('State', fontsize=16)


# Normalize the sightings by state population. What do you observe? Anything interesting?
def normalize_sightings_by_state():
    plt.figure(figsize=[17, 5])

    data = pd.read_csv('data/master_transform_2.csv')
    data = data.filter(items=[gd.ColumnName.STATE.value])
    state_count_data = data['State'].value_counts().reset_index()
    state_count_data.columns = ['State', 'Count']
    state_count_data = state_count_data.sort_values(by="State")

    min = np.min(state_count_data["Count"])
    max = np.max(state_count_data["Count"])

    # Normalized Data
    normalized_data = []

    for index, row in state_count_data.iterrows():
        normalized_data.append(tuple((row["State"], (row['Count'] - min) / (max - min))))

    df = pd.DataFrame(list(normalized_data))
    print(normalized_data)

    plt.bar(df[0], df[1], align='center', alpha=0.8)
    plt.title('UFO Sightings Per State (Normalized)')
    plt.ylabel('# of Sightings', fontsize=16)
    plt.xlabel('State', fontsize=16)






