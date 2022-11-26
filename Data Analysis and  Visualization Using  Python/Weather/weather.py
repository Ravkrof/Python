import pandas as pd
import matplotlib.pyplot as plt

# Create data frame and display the information of the data set.
w_df = pd.read_csv(r'weatherAUS.csv')


# print(w_df)

def q1():
    # short summary of the dataframe
    w_df.info()
    # Statistical description of dataframe
    print(w_df.describe().T)


def q2():
    # Treat NA values by ‘0’
    # Printing Total number of NA values under an entire Dataset
    print(w_df.isna().sum().sum())
    w_df.fillna(0, inplace=True)
    print(w_df.isna().sum().sum())
    # print(w_df["Evaporation"]) testing change in column entries


def q3():
    # Treat NA values by mean value of the column values.
    # Identifying dtypes of the columns
    print(w_df.info())
    l = w_df.select_dtypes(exclude='object')
    print(l)
    for i in list(l):
        l[i].fillna(int(l[i].mean()), inplace=True)
    print(l)


def q4():
    # Display the length of the dataset. Display first 5 records of the dataset. Display last five records of the
    # data set.
    print("The length of the dataset is:", len(w_df))
    # df.head() has default value as 5
    print(w_df.head())
    print(w_df.tail())


def q5():
    # Display average min and average max temperature city-wise.
    print(w_df.groupby('Location')['MinTemp'].mean())
    print(w_df.groupby('Location')['MaxTemp'].mean())


def q6():
    # Plot bar graph to showcase min, max temperature and rainfall . ( x-axis: time, y-axis: country, Title: ‘Min-Max
    # Temperature’)
    w_df[["MinTemp", "MaxTemp", "Rainfall"]].head(10).plot(kind='bar')
    plt.xlabel("Time")
    plt.ylabel("Country")
    plt.title("Min-Max Temperature")
    plt.show()


def q7():
    # Display the details where wind direction does change at different observation times.
    l = []
    for index in w_df.index:
        if w_df['WindDir9am'][index] == w_df['WindDir3pm'][index]:
            # print(w_df.iloc[index])
            l.append(index)
    print(len(l))


def q8():
    # Which day highest air pressure has been observed and which place/places?
    b = 0
    a = 0
    for index in w_df.index:
        if (w_df['Pressure9am'][index] + w_df['Pressure3pm'][index]) > b:
            b = w_df['Pressure9am'][index] + w_df['Pressure3pm'][index]
            a = index
    print(w_df["Date"][a], w_df["Location"][a])


def q9():
    # How many records have ‘NA’ entry?
    print(sum([True for idx, row in w_df.iterrows() if any(row.isnull())]))


def q10():
    # Display total number of records year-wise.
    w_df['Year'] = pd.DatetimeIndex(w_df['Date']).year
    print((w_df.groupby(['Year']).count())['Date'])


# Menu driven function for ease of execution
def control():
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
