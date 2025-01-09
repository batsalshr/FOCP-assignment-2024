import re
from collections import defaultdict
# Load drivers information from the file
drivers_data = []
with open("f1_drivers.txt") as f:
    for line in f:
        parts = line.strip().split(",")
        drivers_data.append({
            "Driver Number": parts[0],    # Store driver number
            "Short Name": parts[1],       # Store driver's short name
            "Driver Name": parts[2],      # Store full driver name
            "Team Name": parts[3]         # Store team name
        })

# Create a dictionary for quick lookup of driver details by short name
drivers_lookup = {driver["Short Name"]: driver for driver in drivers_data}

# Load number of podiums from the file
podiums_data = {}
with open("podium.txt") as f:
    for line in f:
        short_name, podiums = line.strip().split(",")
        podiums_data[short_name] = int(podiums)  # Convert to integer for calculations

# Load lap times from multiple files
lap_times_files = ["lap_times_1.txt", "lap_times_2.txt", "lap_times_3.txt"]
lap_times_data = []

# Extract lap times from files using regex
for file in lap_times_files:
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                match = re.match(r"([A-Za-z]+)(\d+\.\d+)", line)
                if match:
                    short_name, time = match.groups()
                    lap_times_data.append({
                        "Short Name": short_name,  # Store driver short name
                        "Lap Time": float(time)   # Convert lap time to float
                    })

# Group lap times by driver short name
lap_times_grouped = defaultdict(list)
for lap in lap_times_data:
    lap_times_grouped[lap["Short Name"]].append(lap["Lap Time"])

# Calculate average and fastest lap times for each driver
results = []
for short_name, lap_times in lap_times_grouped.items():
    if short_name in drivers_lookup:
        driver_info = drivers_lookup[short_name]
        avg_lap_time = sum(lap_times) / len(lap_times)  # Calculate average lap time
        fastest_lap_time = min(lap_times)               # Get fastest lap time
        podiums = podiums_data.get(short_name, 0)      # Look up podium count
        results.append({
            "Driver Number": driver_info["Driver Number"],  # Driver number
            "Short Name": short_name,                      # Driver short name
            "Driver Name": driver_info["Driver Name"],     # Full driver name
            "Team Name": driver_info["Team Name"],         # Team name
            "Average Lap Time": avg_lap_time,              # Calculated average lap time
            "Fastest Lap Time": fastest_lap_time,          # Recorded fastest lap time
            "Podiums": podiums                             # Number of podiums
        })
        
# Sort results by the fastest lap time in ascending order
results.sort(key=lambda x: x["Fastest Lap Time"])

# Prepare table headers and format the results
headers = ["Driver Number", "Short Name", "Driver Name", "Team Name", 
           "Average Lap Time", "Fastest Lap Time", "Podiums"]
table = [headers] + [[
    res["Driver Number"],                              # Driver number
    res["Short Name"],                                 # Driver short name
    res["Driver Name"],                                # Driver name
    res["Team Name"],                                  # Team name
    f"{res['Average Lap Time']:.3f}",                 # Formatted average lap time
    f"{res['Fastest Lap Time']:.3f}",                 # Formatted fastest lap time
    res["Podiums"]                                     # Number of podiums
] for res in results]

# Function to format and print the table with centered content
def print_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]  # Find max width for each column
    print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")            # Print top border

    for row in data:
        print("| " + " | ".join(f"{str(item).center(w)}" for item, w in zip(row, col_widths)) + " |")  # Print centered row
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")        # Print row border

# Display the results table
print_table(table)

# Calculate the overall average lap time of all drivers
total_lap_time = sum(res['Average Lap Time'] for res in results)  # Total average lap time of all drivers
overall_avg_lap_time = total_lap_time / len(results)              # Calculate overall average
print(f"\nOverall Average Lap Time of All Drivers: {overall_avg_lap_time:.3f}")
