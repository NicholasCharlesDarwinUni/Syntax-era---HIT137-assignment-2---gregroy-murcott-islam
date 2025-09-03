import pandas as pd
import os
import glob

#fileList = ["stations_group_1986.csv",  "stations_group_1987.csv",  "stations_group_1988.csv",  "stations_group_1989.csv",  "stations_group_1990.csv",  "stations_group_1991.csv",  "stations_group_1992.csv",  "stations_group_1993.csv",  "stations_group_1994.csv",  "stations_group_1995.csv",  "stations_group_1996.csv",  "stations_group_1997.csv",  "stations_group_1998.csv",  "stations_group_1999.csv",  "stations_group_2000.csv",  "stations_group_2001.csv",  "stations_group_2002.csv",  "stations_group_2003.csv",  "stations_group_2004.csv",  "stations_group_2005.csv"]
path = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))

csvPath = os.path.join(script_dir, "weatherData", "*.csv")

csvFiles = glob.glob(csvPath)


print(csvFiles)

def deleteFile(file_path):
    if os.path.exists(file_path):
        os.remove("average_temp.txt")
    else:
        print("deletion failed")

for f in csvFiles:
    summerValues = pd.read_csv(f, usecols=['January', 'February', 'December'])
    autumnValues = pd.read_csv(f, usecols=['March', 'April', 'May'])
    winterValues = pd.read_csv(f, usecols=['June', 'July', 'August'])
    springValues = pd.read_csv(f, usecols=['September', 'October', 'November'])

    summerAverages = summerValues.mean()
    autumnAverages = autumnValues.mean()
    winterAverages = winterValues.mean()
    springAverages = springValues.mean()

    summerAve = str(round((sum(summerAverages) / 3), 1))
    autumnAve = str(round((sum(autumnAverages) / 3), 1))
    winterAve = str(round((sum(winterAverages) / 3), 1))
    springAve = str(round((sum(springAverages) / 3), 1))

deleteFile("average_temp.txt")
file = open("average_temp.txt", "a")
file.write("Average for summer:")
file.write(summerAve)
file.write("°C\n") 
file.write("Average for autumn:")
file.write(autumnAve)
file.write("°C\n")
file.write("Average for winter:")
file.write(winterAve)
file.write("°C\n")
file.write("Average for spring:")
file.write(springAve)
file.write("°C\n")
file.close()