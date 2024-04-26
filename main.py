import random
import tau_units
import pandas as pd

units_dict = tau_units.tau_units


def random_unit_select(tau_units):
    unit_name = random.choice(list(tau_units.keys()))
    unit_info = tau_units[unit_name]
    min_points = unit_info["Minimum"]
    max_points = unit_info["Maximum"]
    points = random.randint(min_points, max_points)
    return unit_name, points


total_points = 0
selected_units = []

# acquire how many units user would like, in points
points_goal = int(input("Please enter your desired army size as a number: "))

# Print the input value to verify
print("Desired army size:", points_goal, "points.")

UnitList = {'Selected Units': [selected_units], 'Total Points': [total_points]}
#TODO UnitList currently appends the full list to first cell, fix

while total_points < points_goal:
    selected_unit, points = random_unit_select(units_dict)
    UnitList['Selected Units'].append(selected_unit)
    UnitList['Total Points'].append(points)
    df = pd.DataFrame(UnitList)
    df.to_csv('Tau Units.csv', index=False)
    if total_points + points <= points_goal:
        selected_units.append(selected_unit)
        total_points += points
    else:
        break
print("Your army has been added to the file.")
