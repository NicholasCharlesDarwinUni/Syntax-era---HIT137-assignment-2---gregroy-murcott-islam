import pandas as pd
import os
import glob

#fileList = ["stations_group_1986.csv",  "stations_group_1987.csv",  "stations_group_1988.csv",  "stations_group_1989.csv",  "stations_group_1990.csv",  "stations_group_1991.csv",  "stations_group_1992.csv",  "stations_group_1993.csv",  "stations_group_1994.csv",  "stations_group_1995.csv",  "stations_group_1996.csv",  "stations_group_1997.csv",  "stations_group_1998.csv",  "stations_group_1999.csv",  "stations_group_2000.csv",  "stations_group_2001.csv",  "stations_group_2002.csv",  "stations_group_2003.csv",  "stations_group_2004.csv",  "stations_group_2005.csv"]
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "C:/Users/John/Documents/Python/Assignment2/weatherData/*.csv"))

for f in csv_files:
    summerValues = pd.read_csv(f, usecols=['January', 'February', 'December'])
    autumnValues = pd.read_csv(f, usecols=['March', 'April', 'May'])
    winterValues = pd.read_csv(f, usecols=['June', 'July', 'August'])
    springValues = pd.read_csv(f, usecols=['September', 'October', 'November'])

    summerAverages = summerValues.mean()
    autumnAverages = autumnValues.mean()
    winterAverages = winterValues.mean()
    springAverages = springValues.mean()

    summerAve = round((sum(summerAverages) / 3), 1)
    autumnAve = round((sum(autumnAverages) / 3), 1)
    winterAve = round((sum(winterAverages) / 3), 1)
    springAve = round((sum(springAverages) / 3), 1)

print("Average for summer:",summerAve)

print("Average for autumn:",autumnAve)

print("Average for winter:",winterAve)

print("Average for spring:",springAve)
