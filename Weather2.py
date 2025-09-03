import pandas as pd
import os
import glob

#fileList = ["stations_group_1986.csv",  "stations_group_1987.csv",  "stations_group_1988.csv",  "stations_group_1989.csv",  "stations_group_1990.csv",  "stations_group_1991.csv",  "stations_group_1992.csv",  "stations_group_1993.csv",  "stations_group_1994.csv",  "stations_group_1995.csv",  "stations_group_1996.csv",  "stations_group_1997.csv",  "stations_group_1998.csv",  "stations_group_1999.csv",  "stations_group_2000.csv",  "stations_group_2001.csv",  "stations_group_2002.csv",  "stations_group_2003.csv",  "stations_group_2004.csv",  "stations_group_2005.csv"]
path = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))

csvPath = os.path.join(script_dir, "weatherData", "*.csv")

csvFiles = glob.glob(csvPath)

def deleteFile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("deletion failed")
def findAvgTemp():
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
        file1 = open("average_temp.txt", "a")
        file1.write("Average for summer:")
        file1.write(summerAve)
        file1.write("°C\n") 
        file1.write("Average for autumn:")
        file1.write(autumnAve)
        file1.write("°C\n")
        file1.write("Average for winter:")
        file1.write(winterAve)
        file1.write("°C\n")
        file1.write("Average for spring:")
        file1.write(springAve)
        file1.write("°C\n")
        file1.close()
    print("average_temp.txt written")

def findTempVariation():
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    all_data = []
    for f in csvFiles:
        try:
            df = pd.read_csv(f)

            if not all(col in df.columns for col in ['STATION_NAME'] + months):
                print(f"Skipping {os.path.basename(f)}: Missing required columns.")
                continue

            all_data.append(df[['STATION_NAME'] + months])

        except Exception as e:
            print(f"Error processing {f}: {e}")

    if not all_data:
        print("No data")
        return

    combined_df = pd.concat(all_data)

    long_df = combined_df.melt(
        id_vars='STATION_NAME',
        value_vars=months,
        var_name='Month',
        value_name='Temperature'
    )

    long_df = long_df.dropna()

    stats_df = long_df.groupby('STATION_NAME')['Temperature'].std().round(1).reset_index()
    stats_df = stats_df.rename(columns={'Temperature': 'StdDev'})

    max_std = stats_df['StdDev'].max()
    min_std = stats_df['StdDev'].min()

    most_variable = stats_df[stats_df['StdDev'] == max_std]
    least_variable = stats_df[stats_df['StdDev'] == min_std]

    deleteFile("temperature_stability_stations.txt")
    file2 = open("temperature_stability_stations.txt", "a")

    file2.write(f"Most Variable Station(s): (Std Dev {max_std}°C):")
    for _, row in most_variable.iterrows():
        file2.write("\n")        
        file2.write(f"{row['STATION_NAME']}")
    
    file2.write("\n")

    file2.write(f"Least Variable Station(s): (Std Dev {min_std}°C):")
    for _, row in least_variable.iterrows():
        file2.write("\n")
        file2.write(f"{row['STATION_NAME']}, ")
    
    file2.close()
    print("temperature_stability_stations.txt written")
    
def findTempRange():
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    all_data = []
    for f in csvFiles:
        try:
            df = pd.read_csv(f)

            if not all(col in df.columns for col in ['STATION_NAME'] + months):
                print(f"⚠️ Skipping {os.path.basename(f)}: Missing required columns.")
                continue

            all_data.append(df[['STATION_NAME'] + months])

        except Exception as e:
            print(f"❌ Error processing {f}: {e}")

    if not all_data:
        print("❌ No valid data loaded.")
        return

    combined_df = pd.concat(all_data)

    combined_df['MaxTemp'] = combined_df[months].max(axis=1)
    combined_df['MinTemp'] = combined_df[months].min(axis=1)
    combined_df['TempRange'] = combined_df['MaxTemp'] - combined_df['MinTemp']

    grouped = combined_df.groupby('STATION_NAME').agg({
        'TempRange': 'max',
        'MaxTemp': 'max',
        'MinTemp': 'min'
    }).round(1).reset_index()

    max_range = grouped['TempRange'].max()
    highest_range_stations = grouped[grouped['TempRange'] == max_range]
    
    deleteFile("largest_temp_range_station.txt")
    file3 = open("largest_temp_range_station.txt", "a")

    
    for _, row in highest_range_stations.iterrows():
        file3.write(f"{row['STATION_NAME']}: ")
        file3.write(f"Range {max_range}°C")
        file3.write(f"(Max: {row['MaxTemp']}°C, ")
        file3.write(f"Min: {row['MinTemp']}°C)")
    print("largest_temp_range_station.txt written")

findAvgTemp()
findTempVariation()
findTempRange()