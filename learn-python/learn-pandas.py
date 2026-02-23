import pandas as pd

df = pd.DataFrame({
    "Hassan": [10, 20, 25],
    "Musa": [12, 19, 31]
})

df.to_csv("marks.csv",)