import csv
import GlobalData
from datetime import datetime


# select dates between January 1, 2005 and September 22, 2016.
# with format '4/16/05', '7/2/41', '11:30:00', 'AM',
def filter_by_date():

    # data to read the ufo data file
    name = 'data/master_transform_1.csv'
    transformed_data = 'data/master_transform_2.csv'

    # extract dates that we care about
    first_line = True
    with open(name, "r") as read_file, open(transformed_data, "w") as write_file:
        writer = csv.writer(write_file)
        for row in csv.reader(read_file):

            # persist the first line
            if first_line:
                writer.writerow(row[0:13])
                first_line = False
                continue

            date_extracted = row[GlobalData.Column.DATEOFSIGHTING.value]
            m,d,y = date_extracted.split("/")
            y = int(y) + 2000 # convert to year 2000

            row_date = datetime(int(y), int(m), int(d))
            # print(GlobalData.DateRange.LOWERDATE.value, " ", row_date, " ", GlobalData.DateRange.UPPERDATE.value)

            # make sure proper date
            if GlobalData.DateRange.LOWERDATE.value < row_date < GlobalData.DateRange.UPPERDATE.value:
                # print(row)
                # copy over entire row of valid data
                writer.writerow(row[0:13])
