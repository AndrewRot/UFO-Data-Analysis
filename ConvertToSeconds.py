import csv
import re


# -
# to
# about

string = ["5 sec", "5.6 seconds", "8 or 9 hours", "<5 min", "~4.5 to 8.33 hours", "no no",
          "stupid 5 - 8 seconds yea", "oh yea it took 5 HOURS yesterday", "99seconds", "f;asldkjf45fdjs;la"]

# TODO add more regex expressions to improve data lifespan - ask for help - since im bum at regex rn


def convert_sec(x):

    pattern_sec = "(\d+\.?\d*)\s*(s|S).*"
    pattern_min = "(\d+\.?\d*)\s*(m|M).*"
    pattern_hour = "(\d+\.?\d*)\s*(h|H).*"
    pattern_no_unit = "(\d+\.?\d*).*$"

    result = re.search(pattern_sec, x)
    if result:
        # print (result.group(1), result.group(2))
        return (float(result.group(1)))

    result = re.search(pattern_min, x)
    if result:
        # print (result.group(1), result.group(2))
        return (float(result.group(1)) * 60.0)

    result = re.search(pattern_hour, x)
    if result:
        # print (result.group(1), result.group(2))
        return (float(result.group(1)) * 3600.0)

    result = re.search(pattern_no_unit, x)
    if result:
        # print (result.group(1))
        return (float(result.group(1)))
    # if (x != " "):
        # print(x)

    return None

# for x in string:
#     z = convert_sec(x)
#     print(z)


def convert_duration_to_seconds():

    # data to read the ufo data file
    name = 'data/master.csv'
    transformed_data = 'data/master_transform_1.csv'
    duration_column = 4

    # convert the duration to seconds - write to a new file
    first_line = True
    with open(name, "r") as read_file, open(transformed_data, "w") as write_file:
        writer = csv.writer(write_file)
        for row in csv.reader(read_file):

            # preserve the column title
            if first_line:
                first_line = False
                writer.writerow(row[0:4] + ["Duration"] + row[5:13])
                continue

            time = convert_sec(row[duration_column])
            writer.writerow(row[0:4] + [time] + row[5:13])


