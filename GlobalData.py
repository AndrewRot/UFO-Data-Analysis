from enum import Enum
from datetime import datetime


# Date Limits (between January 1, 2005 and September 22, 2016.)
class DateRange(Enum):
    LOWERDATE = datetime(2005, 1, 1)
    UPPERDATE = datetime(2016, 9, 22)


# mapping of the column names to the indexes
class Column(Enum):
    DATE = 0
    CITY = 1
    STATE = 2
    SHAPE = 3
    DURATION = 4
    SUMMARY = 5
    POSTED = 6
    DATEOFSIGHTING = 7
    TIMEOFSIGHTING = 8
    MERIDIAN = 9
    Month = 10
    Day = 11
    Year = 12


# for pandas csv reader
class ColumnName(Enum):
    DATE = "Date / Time"
    CITY = "City"
    STATE = "State"
    SHAPE = "Shape"
    DURATION = "Duration"
    SUMMARY = "Summary"
    POSTED = "Posted"
    DATEOFSIGHTING = "Date"
    TIMEOFSIGHTING = "Time"
    MERIDIAN = "Meridian"
    MONTH = "Month"
    DAY = "Day"
    YEAR = "Year"


# Time of Days
#  Night (00:00-05:59), Morning (06:00-
# 11:59), Afternoon (12:00-17:59), and Evening (18:00-23:59)
# Idea on how to map this smartly given to me by corey tapeley
time_of_day = {
    0: "Night",
    1: "Morning",
    2: "Afternoon",
    3: "Night",
}


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# !Beware that this is only american abbreviations - the data contains UFO sightings
# from other territories outside the United States.
us_region = {
    'AL': 'South',
    'AK': 'West',
    'AZ': 'West',
    'AR': 'South',
    'CA': 'West',
    'CO': 'West',
    'CT': 'Northeast',
    'DE': 'South',
    'FL': 'South',
    'GA': 'South',
    'HI': 'West',
    'ID': 'West',
    'IL': 'Midwest',
    'IN': 'Midwest',
    'IA': 'Midwest',
    'KS': 'Midwest',
    'KY': 'South',
    'LA': 'South',
    'ME': 'Northeast',
    'MD': 'South',
    'MA': 'Northeast',
    'MI': 'Midwest',
    'MN': 'Midwest',
    'MO': 'South',
    'MS': 'South',
    'MT': 'West',
    'NE': 'Midwest',
    'NV': 'West',
    'NH': 'Northeast',
    'NJ': 'Northeast',
    'NM': 'West',
    'NY': 'Northeast',
    'NC': 'South',
    'ND': 'Midwest',
    'OH': 'Midwest',
    'OK': 'South',
    'ON': 'Northeast',
    'OR': 'West',
    'PA': 'Northeast',
    'RI': 'Northeast',
    'SC': 'South',
    'SD': 'Midwest',
    'TN': 'South',
    'TX': 'South',
    'UT': 'West',
    'VT': 'Northeast',
    'VA': 'South',
    'WA': 'South',
    'WV': 'South',
    'WI': 'Midwest',
    'WY': 'West',
}

