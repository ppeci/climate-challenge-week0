import pandas as pd

def load_data():
    countries = ["ethiopia","kenya","nigeria","sudan","tanzania"]
    dfs = []

    for c in countries:
        df = pd.read_csv(f"data/{c}_clean.csv")
        df["Country"] = c.capitalize()
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)