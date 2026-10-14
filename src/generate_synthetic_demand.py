'''Synthetic scenario generator only; output values are illustrative, not observed Egyptian utility data.'''

import numpy as np
import pandas as pd

np.random.seed(42)
print('Generating synthetic hourly scenarios for 27 governorates...')
sample_dates = pd.date_range(start='2023-01-01', end='2025-12-31 23:00:00', freq='h')
govs_data = {
    'Cairo': {'base': 2500, 'temp': 45, 'pop': 10200000, 'share': 18.0},
    'Giza': {'base': 2100, 'temp': 42, 'pop': 9300000, 'share': 15.0},
    'Alexandria': {'base': 1800, 'temp': 35, 'pop': 5600000, 'share': 11.0},
    'Dakahlia': {'base': 1100, 'temp': 38, 'pop': 7000000, 'share': 6.0},
    'Sharqia': {'base': 1150, 'temp': 39, 'pop': 7800000, 'share': 6.5},
    'Beheira': {'base': 950, 'temp': 37, 'pop': 6900000, 'share': 5.0},
    'Monufia': {'base': 850, 'temp': 38, 'pop': 4700000, 'share': 4.0},
    'Qalyubia': {'base': 1000, 'temp': 40, 'pop': 6000000, 'share': 5.5},
    ' Gharbia': {'base': 900, 'temp': 38, 'pop': 5400000, 'share': 4.5},
    'Port Said': {'base': 500, 'temp': 34, 'pop': 800000, 'share': 1.5},
    'Suez': {'base': 600, 'temp': 38, 'pop': 800000, 'share': 2.0},
    'Ismailia': {'base': 550, 'temp': 38, 'pop': 1400000, 'share': 1.8},
    'Damietta': {'base': 600, 'temp': 35, 'pop': 1600000, 'share': 2.0},
    'Kafr El Sheikh': {'base': 700, 'temp': 36, 'pop': 3600000, 'share': 3.0},
    'Fayoum': {'base': 650, 'temp': 43, 'pop': 4000000, 'share': 2.5},
    'Beni Suef': {'base': 600, 'temp': 44, 'pop': 3600000, 'share': 2.2},
    'Minya': {'base': 750, 'temp': 46, 'pop': 6200000, 'share': 3.5},
    'Asyut': {'base': 800, 'temp': 48, 'pop': 5000000, 'share': 4.0},
    'Sohag': {'base': 700, 'temp': 47, 'pop': 5600000, 'share': 3.2},
    'Qena': {'base': 600, 'temp': 47, 'pop': 3600000, 'share': 2.5},
    'Luxor': {'base': 450, 'temp': 48, 'pop': 1400000, 'share': 1.5},
    'Aswan': {'base': 550, 'temp': 49, 'pop': 1600000, 'share': 2.0},
    'Red Sea': {'base': 400, 'temp': 42, 'pop': 400000, 'share': 1.5},
    'New Valley': {'base': 200, 'temp': 45, 'pop': 300000, 'share': 0.8},
    'Matrouh': {'base': 350, 'temp': 33, 'pop': 500000, 'share': 1.2},
    'North Sinai': {'base': 250, 'temp': 40, 'pop': 500000, 'share': 0.9},
    'South Sinai': {'base': 300, 'temp': 41, 'pop': 100000, 'share': 1.0}
}

data = []
for dt in sample_dates:
    month = dt.month; hour = dt.hour; year = dt.year; day_of_week_str = dt.strftime('%A'); is_weekend_str = 'Yes' if dt.weekday() in [4, 5] else 'No'; day_number_in_month = dt.day
    base_temp = 22 + 13 * np.sin(2 * np.pi * (month - 3) / 12)
    daily_temp_var = 5 * np.sin(2 * np.pi * (hour - 6) / 24)
    year_variation = 0.5 if year == 2024 else (1.0 if year == 2025 else 0.0)
    
    for region, params in govs_data.items():
        temp = np.clip(base_temp + daily_temp_var + year_variation + np.random.normal(0, 1.5), 12, 48)
        humidity = np.clip(50 - 0.7 * (temp - 25) + np.random.normal(0, 5), 15, 95)
        for c_type in ['Residential', 'Commercial', 'Industrial']:
            ac_load = max(0, (temp - 28) * params['temp']) if temp > 28 else 0
            time_factor = 1.3 if 18 <= hour <= 23 else (0.8 if 0 <= hour <= 6 else 1.0)
            weekend_factor = 0.85 if is_weekend_str == 'Yes' and c_type != 'Residential' else 1.0
            type_multiplier = 1.0 if c_type == 'Residential' else (1.4 if c_type == 'Commercial' else 2.5)
            growth_factor = 1.0 if year == 2023 else (1.04 if year == 2024 else 1.08)
            
            consumption_kwh = max(30, ((params['base'] + ac_load) * time_factor * weekend_factor * type_multiplier / 15 + np.random.normal(0, 30)) * growth_factor)
            generation_gw = round(consumption_kwh / 1000, 6)
            generation_tw = round(generation_gw / 1000, 9)
            per_capita = round(consumption_kwh / params['pop'], 8)
            
            data.append({
                'Date': dt.strftime('%Y-%m-%d %H:%M:%S'),
                'Governorate': region.strip(),
                'Customer_Type': c_type,
                'Population': params['pop'],
                'Energy_Share_%': params['share'],
                'Total_Energy_Generation_TW': generation_tw,
                'Total_Energy_Generation_GW': generation_gw,
                'Consumption_per_Capita_kWh': per_capita,
                'Day_of_Week': day_of_week_str,
                'Weekend': is_weekend_str,
                'Day_Number_In_Month': day_number_in_month,
                'Area': 'Egypt',
                'ISO_code': 'EGY',
                'Area_type': 'Country or economy',
                'Electricity_source': 'All Sources',
                'Is_aggregated_source': True,
                'Continent': 'Africa',
                'Ember_region': 'Africa',
                'EU_member': 'FALSE',
                'OECD_member': 'FALSE',
                'G20_member': 'FALSE',
                'G7_member': 'FALSE',
                'ASEAN_member': 'FALSE',
                'Temperature_C': round(temp, 1),
                'Humidity_Pct': round(humidity, 1),
                'Year': year,
                'Month': month,
                'Hour': hour,
                'Electricity_Consumption_kWh': round(consumption_kwh, 2)
            })

df = pd.DataFrame(data)
monthly_total_gw = df.groupby(['Month', 'Governorate'])['Total_Energy_Generation_GW'].transform('sum')
monthly_avg_gw = df.groupby(['Month', 'Governorate'])['Total_Energy_Generation_GW'].transform('mean')
df['Monthly_Total_Generation_GW'] = round(monthly_total_gw, 2)
df['Monthly_Average_Generation_GW'] = round(monthly_avg_gw, 4)
df['Monthly_Total_Generation_TW'] = round(monthly_total_gw / 1000, 6)
df['Monthly_Average_Generation_TW'] = round(monthly_avg_gw / 1000, 9)

output_file = 'outputs/egypt_all_governorates_2023_2025_synthetic.csv'
df.to_csv(output_file, index=False)
print(f'Saved synthetic scenario data to {output_file} ({len(df):,} rows)')
