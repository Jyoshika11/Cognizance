import pandas as pd
ser = pd.Series([input("Enter the Sentence : ")])
for i in range(len(ser)):
    print(ser[i].title(),end=' ')




