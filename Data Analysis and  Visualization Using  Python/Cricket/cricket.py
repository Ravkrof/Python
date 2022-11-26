import pandas as pd
import re

pd.options.mode.chained_assignment = None
# Convert data table into data frame and display the description.
mric_df = pd.read_csv(r'most_runs_in_cricket.csv')


def q1():
    # short summary of the dataframe
    mric_df.info()
    # Statistical description of dataframe
    print(mric_df.describe().T)


def q2():
    # Display the length of the dataset. Display first 10 records of the dataset. Display last five records of the
    # data set.
    print("The length of the dataset is:", len(mric_df))
    # df.head() has default value as 5
    print(mric_df.head(10))
    print(mric_df.tail())


def q3():
    # Display the name of the player/players who played maximum match, maximum innings, scored maximum runs.
    print(mric_df.set_index('Player')['Mat'].idxmax(), " No. of Matches(Maximum):", mric_df['Mat'].max())
    print(mric_df.set_index('Player')['Inns'].idxmax(), " No. of Innings(Maximum):", mric_df['Inns'].max())
    print(mric_df.set_index('Player')['Runs'].idxmax(), " No. of Runs(Maximum):", mric_df['Runs'].max())


def q4():
    # Display the name of the player/players who played minimum match, minimum innings, scored minimum runs( non zero).
    print(mric_df.set_index('Player')['Mat'].idxmin(), " No. of Matches(Minimum):", mric_df['Mat'].min())
    print(mric_df.set_index('Player')['Inns'].idxmin(), " No. of Innings(Minimum):", mric_df['Inns'].min())
    print(mric_df.set_index('Player')['Runs'].idxmin(), " No. of Runs(Minimum):", mric_df['Runs'].min())


def q5():
    # Display total number of players and their average performance, country-wise.
    print((mric_df.groupby(['Country']).count())['Player'])
    # Average Performance
    print(mric_df.groupby('Country')['Ave'].mean())


def q6():
    # Display the player’s details who scored highest run in least BF.
    b = 0
    a = 0
    for index in mric_df.index:
        # converting BF to int and removing '+'
        mric_df['BF'][index] = int(mric_df['BF'][index].replace('+', ''))
        if (mric_df['Runs'][index] / mric_df['BF'][index]) > b:
            b = (mric_df['Runs'][index] / mric_df['BF'][index])
            a = index
    print(mric_df.iloc[a])


def q7():
    # Display the longest span player’s details. Display the number of players from this country
    l = []
    for index in mric_df.index:
        yearsplit = mric_df['Span'][index].strip().split("-")
        l.append(int(yearsplit[1]) - int(yearsplit[0]))
    print(mric_df.iloc[l.index(max(l))])
    print("Number of players from same country: ",
          mric_df[mric_df['Country'] == mric_df["Country"][l.index(max(l))]]['Player'].count())


def q8():
    # Display the details of the players who are currently active.
    for index in mric_df.index:
        if '2022' in mric_df['Span'][index]:
            print(mric_df.iloc[index])


def q9():
    # Display the details of the players having ‘M’/ ’m’ as one of the character in their name.
    for index in mric_df.index:
        if 'M' in mric_df['Player'][index] or 'm' in mric_df['Player'][index]:
            print(mric_df.iloc[index])


def q10():
    # Display details of players with : maximum & minimum 100,4s and 6s
    print('Max 100', mric_df.set_index('Player')['100'].idxmax())
    print('Min 100', mric_df.set_index('Player')['100'].idxmin())

    print('Max 4s', mric_df.set_index('Player')['4s'].idxmax())
    print('Min 4s', mric_df.set_index('Player')['4s'].idxmin())

    print('Max 6s', mric_df.set_index('Player')['6s'].idxmax())
    print('Min 6s', mric_df.set_index('Player')['6s'].idxmin())


def clean_country_from_name():
    tmp = []
    for index in mric_df.index:
        # Storing each player's teams that he has played for in a list
        tmp.append(re.findall(r'\(.*?\)', mric_df['Player'][index])[0])
        mric_df['Player'][index] = re.sub(r'\(.*?\)', '', mric_df['Player'][index]).strip()
    country = []
    for x in tmp:
        x = x.replace('(', '').replace(')', '')
        x = x.split('/')
        for i in x:
            # As we just want country we can ignore everything in the list. Included Ireland because player 79- Eoin
            # Morgan has played for 2 countries so we're choosing England instead
            if i not in ['World', 'ICC', 'Asia', 'Afr', 'IRE']:
                country.append(i)
    mric_df['Country'] = country


# Menu driven function for ease of execution
def control():
    clean_country_from_name()
    while True:
        print("Press anything other than 1-10 to Exit")
        ch = int(input("Enter Question Number: "))
        if ch == 1:
            q1()
        elif ch == 2:
            q2()
        elif ch == 3:
            q3()
        elif ch == 4:
            q4()
        elif ch == 5:
            q5()
        elif ch == 6:
            q6()
        elif ch == 7:
            q7()
        elif ch == 8:
            q8()
        elif ch == 9:
            q9()
        elif ch == 10:
            q10()
        else:
            print("Invalid/Exit")
            break


control()
