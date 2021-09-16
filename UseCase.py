import pandas as pd

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Book.csv")

print(df)
TotalMarks=0
OutOff=0
for i in df.index:
    TotalMarks+=df["MARKS"][i]
    OutOff+=df["OUT OF"][i]
print(str(TotalMarks)+"/"+str(OutOff))
print(str((TotalMarks*100)/OutOff) +"%")