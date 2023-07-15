from matplotlib import dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from stockData import raw

def resampling(df,period):  #resample the data based on a given period
    return(df
           .resample(f'{period}')
           .Close
           .mean()
           )


def volatility(df): #give back 2 type of 30 day volatility based on the original database
    return (df
            .assign(close_vol=df.rolling(30).Close.std(),
                    per_vol=df.Close.pct_change().rolling(30).std())
            .iloc[:, -2:]  # pick the last two colum
            )


def moving_avg(df,period): #calculate the moving averaga on a given period and give back the movingavg data
    return (df
            .assign(ma=df.Close.rolling(period).mean(),
                    )
            ['ma']
            )


def calc_obv(df, close_col='Close', vol_col='Volume'): #calculate on balance volume
    close = df[close_col]
    vol = df[vol_col]
    close_shift = close.shift(1)
    return (df
            .assign(vol=np.select([close > close_shift,
                                   close == close_shift,
                                   close < close_shift],
                                   [vol, 0, -vol]),
                    obv=lambda df_:df_.vol.fillna(0).cumsum()
                   )
            ['obv']
           )





# *** RSI ***, the rsi calculation based on the different function, the second one is the final suliton


def avg(df, col, window_size=14):
    results=[]
    window = []
    for i, val in enumerate(df[col]):
        window.append(val)
        if i < (window_size):
            results.append(np.nan)
        elif i == (window_size):
            window.pop(0)
            results.append(sum(window)/window_size)
        else:
            results.append((results[-1]*(window_size-1)+val) / window_size)
    return pd.Series(results, index=df.index)


def get_rsi(df):
    return(raw[['Close']]
           .assign(change=lambda df:df['Close'].diff(),
                   gain=lambda df:df.change.clip(lower=0),
                   loss=lambda df:df.change.clip(upper=0),
                   avg_gain=lambda df:avg(df, col='gain'),
                   avg_loss=lambda df:-avg(df, col='loss'),
                   rs = lambda df:df.avg_gain/df.avg_loss,
                   rsi=lambda df:np.select([df.avg_loss == 0], [100],
                                           (100-(100/(1+df.rs))))
                   )
    ['rsi']
            )



def get_index(df):  # i needed a function wich transform the Date index column into a str type, because Google API cant accept TimeStamp datatype
    index_list = df.index
    return [[str(item)] for item in index_list]



def get_df(df):  #this is the function which create the final Panda DF, which will send to the Google Spreadsheet
    return (df
            .assign(close_vol=df.rolling(30).Close.std(),
                    final_rsi=lambda df:get_rsi(df),
                    movavg=lambda df:moving_avg(df, 50),
                    movavg2=lambda df:moving_avg(df, 200),
                    obv =lambda df:calc_obv(df)
                     )
            )

final_table = get_df(raw).fillna('').values.tolist() # transform the final DF into a 2d list and fill all the 'nan' values with ''. ( because google api cant accept nan values)
new_index = get_index(raw) #get the index data

