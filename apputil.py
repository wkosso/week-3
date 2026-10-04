import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
pd.options.display.max_rows = 100  # default is 60 rows

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)


# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n<=1:
        return n 
    else: 
        # Recursive case: return the sum of the two preceding Fibonacci numbers
        return fibonacci(n-1) + fibonacci(n-2)


# Recursive case: divide n by 2 and append the remainder
def to_binary(n):
    # Base case: if n is 0, return 0
    if n == 0 or n == 1:
        # Base case: if n is 0, return 0
        return str(n)
    # Recursive case: divide n by 2 and append the remainder
    return to_binary(n // 2) + f"{n % 2}"


# Task 1: Identify columns with missing values after replacing '?' with NaN in the gender column.
def task_1():

    df = df_bellevue.copy()
    df['gender'] = df['gender'].replace('?', np.nan)
    # Identify columns with missing values after replacing '?' with NaN in the gender column.
    print(
        "In the gender column, ? was used to mean missing values, "
        "but Python did not count it as missing. "
        "I replaced it with NaN so it gets counted. "
        "The values g and h also look wrong, but I left them alone."
    )
    # Return the list of column names with missing values, sorted by the number of missing values.
    return df.isna().sum().sort_values().index.tolist()

# Task  (call the function to get the result)
task_1()


# Task 2: Count the number of admissions per year, excluding rows with missing or unreadable dates.
def task_2():
    # Convert the 'date_in' column to datetime, coercing errors to NaN
    dates = pd.to_datetime(df_bellevue['date_in'], errors='coerce')
    missing = dates.isna().sum()
    # Count the number of missing or unreadable dates
    if missing > 0:
        print(
            f"{missing} rows have a missing or unreadable date_in, "
            "so they are left out of the yearly counts."
        )
    counts = dates.dt.year.value_counts().sort_index()
    result = counts.reset_index()
    result.columns = ['year', 'total_admissions']
    result['year'] = result['year'].astype(int)
    return result


task_2()


def task_3():
    df = df_bellevue.copy()
    df['gender'] = df['gender'].replace('?', np.nan)
    missing_age = df['age'].isna().sum()
    print(
        "In the gender column, ? means no answer, so I turned it into "
        "NaN and those rows are left out of the groups. "
        "The values g and h look wrong, but they stay as their own "
        "groups because I can't know what they meant. "
        f"{missing_age} rows have no age, and they are skipped when "
        "the average is calculated."
    )
    return df.groupby('gender')['age'].mean()


task_3()


def task_4():
    # Task 4: Replace marital statuses in the 'profession' column with NaN and count the top 5 professions.
    df = df_bellevue.copy()
    not_jobs = ['married', 'spinster', 'widow']
    df['profession'] = df['profession'].replace(not_jobs, np.nan)
    print(
        "The profession column has marital statuses (married, spinster, "
        "widow) in it, which are not professions. I turned them into NaN "
        "so they are not counted. Rows with no profession are also "
        "left out of the counts."
    )
    # Count the number of missing or unreadable professions
    missing_profession = df['profession'].isna().sum()
    if missing_profession > 0:
        print(
            f"{missing_profession} rows have a missing or unreadable profession, "
            "so they are left out of the counts."
        )
    return df['profession'].value_counts().head(5).index.tolist()


task_4()