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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs. I want to make it easier for the user to inut his choice byt inputing number instead of full name of the city.
    while True:
        city_number = input("Tell me which City you would like to explore? For Chicago press 1, for New York City press 2 or Washington press 3?")
        if str(city_number) not in ('1', '2', '3'):
            print("Your input is incorrect!")
        else:
            break

    if str(city_number) == '1':
        city = 'chicago'
    elif str(city_number) == '2':
        city = 'new york city'
    elif str(city_number) == '3':
        city = 'washington'


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_number = input("Enter the number of the month you would like to explore? For Example for February type 2, Data available is only from Janaury to June (1 to 6). For all months just press enter!")
        if str(month_number).lower() not in ('1', '2', '3', '4', '5', '6',''):
            print("Your input is incorrect!")
        else:
            break

    if str(month_number) == '1':
        month = 'january'
    elif str(month_number) == '2':
        month = 'february'
    elif str(month_number) == '3':
        month = 'march'
    elif str(month_number) == '4':
        month = 'april'
    elif str(month_number) == '5':
        month = 'may'
    elif str(month_number) == '6':
        month = 'june'
    elif str(month_number) == '':
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_number = input("Enter the number of the day you would like to explore? For Example for Wednesday type 3. For all days just press enter!")
        if str(day_number).lower() not in ('1', '2', '3', '4', '5', '6','7',''):
            print("Your input is incorrect!")
        else:
            break

    if str(day_number) == '1':
        day = 'monday'
    elif str(day_number) == '2':
        day = 'tuesday'
    elif str(day_number) == '3':
        day = 'wednesday'
    elif str(day_number) == '4':
        day = 'thursday'
    elif str(day_number) == '5':
        day = 'friday'
    elif str(day_number) == '6':
        day = 'saturday'
    elif str(day_number) == '7':
        day = 'sunday'
    elif str(day_number) == '':
        day = 'all'

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

    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


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
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the week:', popular_day)

    # TO DO: display the most common start hour
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
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start Station & End Station'] = "Start Station: " + df['Start Station'] + " & End Station: " + df['End Station']
    popular_combi_station = df['Start Station & End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip:', popular_combi_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Total Travel Time / Mean Travel Time"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_trip_duration = df['Trip Duration'].sum()
    print("The Total Travel Time is roughly %d hours" % round(total_trip_duration/3600,0))

    # TO DO: display mean travel time

    mean_trip_duration = df['Trip Duration'].mean()
    print("The Mean Travel Time is roughly %d minutes" % round(mean_trip_duration/60,0))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
  while True:
            raw_data = input('\nWould you like to see the raw data? Enter yes or no.\n')
            if raw_data not in ('yes', 'no'):
                print("Your input is incorrect!")
            elif raw_data == "no":
                break
            elif raw_data == "yes":
                i = 0
                j = 5
                more = "yes"
                while more == "yes":
                    print(df.iloc[i:j])
                    more = input('\nWould you like to see more data? Enter yes or no.\n')
                    if more not in ('yes', 'no'):
                        print("Your input is incorrect!")
                    elif more == "no": break
                    elif more == "yes":
                          i += 5
                          j += 5
            break
def user_stats(df):
    """Displays statistics on bikeshare users.

    Count of User Type / Earliest, Most recent and most common year of birth """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('This is the count of User Type:', user_types)


    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('This is the count of the different Gender:', gender_types)
    except:
        print('Gender is not available in this dataset')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()
        print ('The erliest year of birth is {}, the most recent year of birth is {} and the most common year of birth is {}'.format(int(earliest_yob), int(most_recent_yob), int(most_common_yob)))
    except:
        print('Birth Year is not available in this dataset')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
