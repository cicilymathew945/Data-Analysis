Data Analysis for Order Data (2019-2021)

This project performs data analysis on order data from the years 2019, 2020, and 2021. The key functionalities include:

Data Wrangling: The code preprocesses the raw order data by cleaning and transforming it into a structured format, handling missing values, and ensuring consistency across data columns.

Handling Missing Data: Missing data rows are identified and saved to a separate file for further analysis, ensuring no data is lost during the processing.

Most Popular Product: The analysis identifies the most popular product(s) based on the frequency of orders, giving insights into product preferences over the years.

Average Monthly Revenue: The project calculates the average monthly revenue for each year, helping to track sales performance across the given period.

Product Price Binning: Products are categorized into price bins (e.g., low, medium, high) to analyze sales counts for different price ranges. This feature helps understand which product categories are performing best within specific price ranges.

Files Included
order_data_2019.csv: Raw order data for 2019, order_data_2020.csv: Raw order data for 2020, order_data_2021.csv: Raw order data for 2021.

missing_data.csv: A file containing all rows of data that had missing or invalid values.

Requirements
To run the analysis, you will need to install the following dependencies: pandas, numpy, matplotlib (for visualizations),seaborn (for additional visualizations)
