import pandas as pd
ufo=pd.read_table("http://bit.ly/uforeports", sep=",")
print(ufo.head())
print(ufo["City"])
print(ufo["State"])