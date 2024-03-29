import random
import tau_units
import pandas as pd

units_dict = tau_units.tau_units


def random_unit_select(tau_units):
    unit_name = random.choice(list(tau_units.keys()))
    points = tau_units[unit_name]
    return unit_name, points


total_points = 0
selected_units = []

# acquire how many units user would like, in points
points_goal = int(input("Please enter your desired army size as a number: "))

# Print the input value to verify
print("Desired army size:", points_goal, "points.")

UnitList = {'Selected Units': [selected_units], 'Total Points': [total_points]}

# Loop until the total points exceed or reach the desired goal
while total_points < points_goal:
    selected_unit, points = random_unit_select(units_dict)
    print("Selected unit:", selected_unit, "- points of selected unit:", points)
    UnitList['Selected Units'].append(selected_unit)
    UnitList['Total Points'].append(points)
    df = pd.DataFrame(UnitList)
    df.to_csv('Tau Units.csv', index=False)
    if total_points + points <= points_goal:
        selected_units.append(selected_unit)
        total_points += points
    else:
        break

# Print the selected units and total points
print("Selected units:", selected_units)
print("Total points:", total_points)
