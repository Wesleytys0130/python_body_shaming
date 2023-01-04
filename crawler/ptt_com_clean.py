import pandas as pd


data = pd.read_csv('/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_data/MuscleBeach/MB_com.csv', index_col=[0])
df=data.drop_duplicates()
df.reset_index(drop=True, inplace=True)
(pd.DataFrame.from_dict(data=df)
     .to_csv('/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_data/MuscleBeach/MB_com.csv', mode='w'))