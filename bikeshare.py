import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
        
        city=input("which city you would like to explore from the following (Chicago, New York, Washington)? >: ")
        city=city.lower()
        cities=['chicago','new york','washington']
        if city in cities:
            break
        print("please enter a valid city name from the following (Chicago, New York, Washington) >: ")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month =input("which month do want to review from the following (January, February, March, April, May, June) or enter 'all'>: ")
        month=month.lower()
        months=['january','february','march','april','may','june','all']
        if month in months:
            break
        print("please enter a valid month from the following (January, February, March, April, May, June) or enter 'all'>: ")



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("which day do you want to review from the following (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or enter 'all' >: ")
        day=day.lower()
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        if day in days:
            break
        print("please enter a valid day from the following (Monday,Tuesday, Wednesday,Thursday,Friday,Saturday) or enter 'all' >: ")


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name

    if month !='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day !='all':
        df=df[df['day_of_week']==day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("The most common month is '{}'\n".format(common_month))

    # TO DO: display the most common day of week
    common_dayofweek=df['day_of_week'].mode()[0]
    print("The most common day of the week is '{}'\n".format(common_dayofweek))

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_starthour=df['hour'].mode()[0]
    print("The most common start hour is '{}'\n".format(common_starthour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("The most common Start Station is ",common_start_station,'\n')

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("The most common End Station is ",common_end_station,'\n')


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination']=df['Start Station']+" >> "+df['End Station']
    common_combination=df['Station Combination'].mode()[0]
    print("The most frequent combination of Start and End Station is ",common_combination,'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # TO DO: display mean travel time
    travel_time=df['Trip Duration'].sum()
    print("The total travel duration is '{}' seconds\n".format(travel_time))
    
    trip_mean=df['Trip Duration'].mean()
    print("The mean travel time is'{}' seconds\n".format(trip_mean))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df.groupby(['User Type'])['User Type'].count()
    print("Here are counts of user types:\n",user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df.groupby(['Gender'])['Gender'].count()
        print("Here are counts of Gender:\n",gender_counts)
    else:
         print("\n*GENDER COLUMN ISN'T AVAILABLE*\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year'in df.columns:
        
        print('The earliest year of birth is',int(df['Birth Year'].min()),'\n')
        print('The most recent year of birth is',int(df['Birth Year'].max()),'\n')
        print('The most common year of birth',int(df['Birth Year'].mode()[0]),'\n')
    else:
        print("\n*BIRTH YEAR COLUMN ISN'T AVAILABLE*\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    #i=5 for the first 5 rows
    i=5
    show_data=input('would you like to dsiplay 5 lines of the raw data? Enter yes or no >: ').lower()
    while show_data.lower()!='no':
        print(df.iloc[0:i])
        show_data=input('Would you like to display 5 more rows of raw data? Enter yes or no >: ').lower()
        i+=5



def main():
    while True:
        city, month, day = get_filters()
        df=load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()