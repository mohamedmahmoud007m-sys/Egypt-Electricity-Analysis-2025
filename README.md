# Egypt Electricity Demand Simulation (Synthetic Data)

A reproducible Python scenario generator for hourly electricity-demand patterns across Egypt's 27 governorates from 2023–2025.

> **Data notice:** every generated weather, demand, and generation value is synthetic. Governorate population and baseline inputs are illustrative assumptions in the script, not verified official figures. The output is not measured utility data, an official estimate, or a forecast.

## Model outline

- Hourly time grid from 2023-01-01 through 2025-12-31.
- 27 governorates and three customer segments: residential, commercial, and industrial.
- Seasonal and daily temperature patterns, weekend and time-of-day multipliers, and seeded random variation.
- NumPy and pandas are used to generate a reproducible CSV for downstream BI practice.

The full run produces 2,130,624 rows and can use substantial memory. Generated data is intentionally excluded from Git.

## Run

```powershell
python -m pip install -r requirements.txt
python src/generate_synthetic_demand.py
```

Output: `outputs/egypt_all_governorates_2023_2025_synthetic.csv`.

## Scope

This repository includes the generator only. Earlier generated exports and an HTML file were omitted because they are large, duplicated, or carry third-party tracking metadata. The scenarios are suitable for demonstration and BI prototyping, not policy, investment, or operational decisions.