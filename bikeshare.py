import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
while True:
    try:

        city = input("insert the city name: ").lower
        if city in CITY_DATA:


        print("ok, let\'s go on")
            break
       elif city not in CITY_DATA:

           print("city is not in our list")
    except:

        pass
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list =  ['january', 'february', 'march', 'april', 'may', 'june']
    month = input("insert the month name: ").lower
    if month in month_list:

        print("ok, let\'s go on")
    else:
        print("no month to show")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("insert the day name: ").lower
    if day in day_list:

        print("ok, let\'s go on")
    else:
        print("no day to show")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
"""
    while True:



# load data file into a dataframe
        df = pd.read_csv(CITY_DATA[city])
# convert the start time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from start time column to create new coulmn
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

#filter by month
       if month != 'all':


    #use the index of the month to get the following int
           month = ['january', 'february', 'march', 'april', 'may', 'june']
           month = month.index(month) + 1
# filter by day of the week
       if day_of_week != 'all':


    # filter by day
           df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    while True:
        try:


    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
            start_time = time.time()

    # TO DO: display the most common month
            most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
            most_common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
#extract hour from the start time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour
# find the most popular hour
        most_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    while True:


    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

    # TO DO: display most commonly used start station
        most_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station

        most_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
#create new column with the combination of start and end station
        df['combination'] = df['Start Station'] + df['End Station']
#display most frequent combination
        most_combination = df['combination'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    while True:



    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
        average_travel_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    while True:



    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of user types
        if 'User Type' in df.columns:
            count_user_type = df.groupby(['User Type'])['User Type'].count()
            user_count = df['User Type'].value.counts()

    # TO DO: Display counts of gender
        if 'Gender' in df.columns:

            count_gender = df.groupby(['Gender'])['Gender'].count()

    # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:

            most_recent_year = df['Birth Year'].max()
            earliest_year = df['Birth Year'].min()
            most_common_year = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        show = input(" would you like to see more data rows? Enter sure or no.\n')
                     if show.lower() = 'sure':

                         print(df.head())
                         continue

                     print(df.head(10))




        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

print("i have done")
if __name__ == "__main__":
	main()
