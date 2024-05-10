import random
import pandas as pd
import tau_units
import tau_upgrades

units_dict = tau_units.tau_units
unit_upgrades = tau_upgrades.tau_weapon_upgrades


def random_unit_select(tau_units):
    unit_name = random.choice(list(tau_units.keys()))
    unit_info = tau_units[unit_name]
    min_points = unit_info["Minimum"]
    max_points = unit_info["Maximum"]
    points = random.randint(min_points, max_points)
    return unit_name, points


def upgrade_select(tau_weapon_upgrades):
    random_upgrade_name = random.choice(list(tau_weapon_upgrades.keys()))
    upgrade_cost = tau_weapon_upgrades[random_upgrade_name]
    return random_upgrade_name, upgrade_cost


total_points = 0
selected_units = []

# Acquire how many units user would like, in points
points_goal = int(input("Please enter your desired army size as a number: "))
print("Desired army size:", points_goal, "points.")

UnitList = {'Selected Units': [], 'Total Points': []}

while total_points < points_goal:
    selected_unit, unit_points = random_unit_select(units_dict)
    random_upgrade_name, upgrade_cost = upgrade_select(unit_upgrades)

    if total_points + unit_points + upgrade_cost <= points_goal:
        selected_units.append([selected_unit, unit_points, random_upgrade_name, upgrade_cost])
        total_points += unit_points + upgrade_cost
    else:
        break

df = pd.DataFrame(selected_units, columns=['Unit', 'Unit Points', 'Upgrade', 'Upgrade Points'])
df['Total Points'] = df['Unit Points'] + df['Upgrade Points']
df.to_csv('Tau Units.csv', index=False)

print("Your army has been added to the file.")
