import pandas as pd
df = pd.read_csv("test_done1.csv")
result_df = df.groupby('Label')['Values'].std()
print(result_df)
result_df.to_csv("standard_deviation_orange.csv", index=False)
