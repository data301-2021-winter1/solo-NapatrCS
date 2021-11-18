import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns


def load_and_process_goals(df):
    df1 = (
    wine.rename(columns={"Sv%": "saves"})
    .assign(Positive_Winrate=lambda x: np.where((x.saves > 50), 1, 0))
    .query("W% > 50 and color_filter == 1")
    .sort_values("W%", ascending=False)
    .reset_index(drop=True)
    .loc[:, ["W%", "hue"]]
)
    return df1


def load_and_process_players(df):
    df = find_and_delete_duplicates(df)
    years = [2000, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    df = df[['Player', 'Club', 'G', 'SHTS', 'SOG', 'SOG%', 'Year']]
    df1 = df[df.Year.isin(years) == True]
    df2 = (df1.sort_values(by=['Player', 'Year'], ascending=[True, True])
           .groupby(['Player', 'Year']).agg({'SHTS': 'sum', 'SOG': 'sum', 'Club': 'sum'})
           )
    return df2


def find_and_delete_duplicates(csv):
    csv = pd.read_csv(csv)
    if len(csv[csv.duplicated()]) > 0:
        print("No. of duplicated entries: ", len(csv[csv.duplicated()]))
        print(csv[csv.duplicated(keep=False)].sort_values(
            by=list(csv.columns)).head())
        csv.drop_duplicates(inplace=True)
    else:
        print("No duplicated entries found")
    return csv