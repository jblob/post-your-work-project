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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # [Hier kommt später deine Logik für Monat, Tag, Stunde hin]

    # Modernisierter F-String:
    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(f"Most Commonly Used Start Station: {most_common_start}")

    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(f"Most Commonly Used End Station: {most_common_end}")

    # display most frequent combination of start station and end station trip
    # Wir verketten die Spalten direkt als Strings
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['Trip Combination'].mode()[0]
    print(f"Most Frequent Combination of Trip: {most_common_trip}")

    # Punkt 4: Hier direkt den F-String für die Zeitmessung eingebaut
    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # [Hier kommt später deine Logik für Summe und Mittelwert hin]

    # Modernisierter F-String:
    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # [Hier kommt später deine Logik für User Types, Gender, Birth Year hin]

    # Modernisierter F-String:
    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
