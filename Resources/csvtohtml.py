import pandas as pd
citydf = pd.read_csv('cities.csv')
citydf.to_html('cities.html')