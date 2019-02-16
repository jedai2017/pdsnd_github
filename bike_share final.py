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
    global city
    # To mark city as a global variable so it can be used by the user_stats function too
    city = input("Would you like to see data for Chicago, New York City, or Washington?\n")
    city = city.lower()
    while (city != "chicago") and (city != "new york city") and (city != "washington"):
        city = input("This is not a valid input, please input Chicago, New York City, or Washington.\n")
        city = city.lower()
    else:
        print("You selected the data from {}.\n".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Would you like to filter the data by month or not at all? You can input all, January, February, March, April, May or June.\n")
    month = month.lower()
    while (month != 'all') and (month != 'january') and (month != 'february') and (month != 'march') and (month != 'april') and (month != 'may') and (month != 'june'):
        month = input("This is not a valid input, please input all, January, February, March, April, May or June.\n")
        month = month.lower()
    else:
        print("You selected the data from {}.\n".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Would you like to filter the data by day of week or not at all? You can input all, Monday, Tuesday, ...., or Sunday.\n")
    day = day.lower()
    while (day != 'all') and (day != 'monday') and (day != 'tuesday') and (day != 'wednesday') and (day != 'thursday') and (day != 'friday') and (day != 'saturday') and (day != 'sunday'):
        day = input("This is not a valid input, pleaes input all, Monday, Tuesday, ...., or Sunday.\n")
        day = day.lower()
    else:
        print("You selected the data from {}.\n".format(day))

    print("You have selected data of {}, from month of {} and from {} day of week.\n".format(city, month, day))
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:',  popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:',  popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Combination']='from ' + df['Start Station']+ ' to '+ df['End Station']
    popular_trip_combo = df['Trip Combination'].mode()[0]
    print('Most Popular Trip Combination:',  popular_trip_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',  total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:',  mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city == "chicago" or city == "new york city":
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print("Washington data does not include gender information.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == "chicago" or city == "new york city":
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth is:', earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth is:', most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is:', most_common_birth_year)

    else:
        print("Washington data does not include year of birth information.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Based on user input, display 5 rows of raw data"""
    i = 0
    total_row = df.shape[0]
    show = int(input('Would you like to see raw data? Enter 1 for yes or 2 for no.\n'))
    while (show != 1) and (show != 2):
        show = int(input("This is not a valid input, please Enter 1 to show raw data or 2 for no.\n"))

    while show == 1:
        if (i + 5) >= total_row:
            print(df.iloc[i:])
            print('This is the end of the raw data.\n')
            break
        print(df.iloc[i:(i+4)])
        i += 5
        show = int(input('Would you like to see raw data? Enter 1 for yes or 2 for no.\n'))
        while (show != 1) and (show != 2):
            show = int(input("This is not a valid input, please Enter 1 to show raw data or 2 for no.\n"))

    else:
        print('No raw data is shown.\n')
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
