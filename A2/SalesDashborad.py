# Name: Jordyn Pendergrass
# Date: April 5, 2026

import time
import os

import pandas as pd
import numpy as np
import pyarrow


pd.set_option('display.max_columns', None) #show all columns in the output
df = pd.read_csv(r"C:\Users\XANA\Downloads\sales_data.csv")

def load_csv(filepath):
    print(f"Loading data from {filepath}...")
    start_time = time.time()
    try:
        df = pd.read_csv(filepath, engine='python')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"number of rows: {len(df)}")
        print(f"columns: {df.columns.tolist()}")
        # Convert order_date to datetime
        df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y', errors='coerce') # convert order_date to datetime, coerce errors to NaT
#        df.fillna(0, inplace=True) # fill any missing values with 0
        df['sales'] = df['quantity'] * df['unit_price'] # create a new column for sales

        required_columns = ['quantity', 'unit_price', 'order_date']
        # Check if all required columns are present
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")
        else:
            print("All required columns are present.")

        return df
    
    except Exception as e:
     print(f"Error loading CSV file: {e}")
    return None


def check_columns(df, needed_columns):
    missing = [col for col in needed_columns if col not in df.columns]
    if missing:
        print(f"Cannot complete this task. Missing columns: {missing}")
        return False
    return True

# Export to Excel file
def export_to_excel(result_df):
    choice = input("\nDo you want to export these results to Excel? (y/n): ").strip().lower()

    if choice != 'y':
        return

    filename = input("Enter the Excel filename (without extension): ").strip()

    if filename == "":
        print("Invalid filename. Export cancelled.")
        return

    try:
        result_df.to_excel(f"{filename}.xlsx")
        print(f"Results exported successfully to {filename}.xlsx")
    except Exception as e:
        print(f"Error exporting to Excel: {e}")

# Data Summary
def display_data_summary(df):
    print("\n--- Sales Data Summary ---")

    print(f"Total orders: {len(df)}")

    if 'employee_id' in df.columns:
        print(f"Number of employees: {df['employee_id'].nunique()}")
    else:
        print("Number of employees: Not available")

    if 'sales_region' in df.columns:
        print(f"Sales regions: {df['sales_region'].nunique()}")
    else:
        print("Sales regions: Not available")

    if 'order_date' in df.columns:
        valid_dates = pd.to_datetime(df['order_date'], errors='coerce').dropna()
        if len(valid_dates) > 0:
            print(f"Dates range of orders: {valid_dates.min().date()} to {valid_dates.max().date()}")
        else:
            print("Dates range of orders: Not available")
    else:
        print("Dates range of orders: Not available")

    if 'customer_name' in df.columns:
        print(f"Number of unique customers: {df['customer_name'].nunique()}")
    else:
        print("Number of unique customers: Not available")

    if 'product_category' in df.columns:
        print(f"Product categories: {df['product_category'].nunique()}")
    else:
        print("Product categories: Not available")

    if 'customer_state' in df.columns:
        print(f"Unique states: {df['customer_state'].nunique()}")
    else:
        print("Unique states: Not available")

    if 'sales' in df.columns:
        print(f"Total sales amount: {df['sales'].sum():.2f}")
    else:
        print("Total sales amount: Not available")

    if 'quantity' in df.columns:
        print(f"Total quantities of products sold: {df['quantity'].sum()}")
    else:
        print("Total quantities of products sold: Not available")

# Menu Options
def show_first_n_rows(df):
    total_rows = len(df)
    print("\nShow the first n rows of sales data")
    print("Enter rows to display:")
    print(f"- Enter a number 1 to {total_rows}")
    print("- To see all rows, enter 'all'")
    print("- To skip preview, press Enter")

    choice = input("Your choice: ").strip().lower()
    if choice == "":
        print("No rows displayed.")
        return
    if choice == "all":
        print(df)
        export_to_excel
        return
    if choice.isdigit():
        n = int(choice)
        if 1 <= n <= total_rows:
            print(df.head(n))
            export_to_excel
        else:
            print(f"Invalid input. Please enter a number from 1 to {total_rows}.")
    else:
        print("Invalid input. Please enter a number, 'all', or press Enter.")

def total_sales_by_region_and_order_type(df):
    pivot = pd.pivot_table(
        df,
        index='sales_region',
        columns='order_type',
        values='sales',
        aggfunc='sum',
        fill_value=0
    )
    print("\nTotal sales by region and order_type:")
    print(pivot)
    export_to_excel(pivot)


def average_sales_by_region_state_sale_type(df):
    pivot = pd.pivot_table(
        df,
        index='sales_region',
        columns='customer_state',
        values='sales',
        aggfunc='mean',
        fill_value=0
    )
    print("\nAverage sales by region with average sales by state:")
    print(pivot)
    export_to_excel(pivot)


def sales_by_customer_type_order_type_state(df):
    pivot = pd.pivot_table(
        df,
        index=['customer_state', 'customer_type', 'order_type'],
        values='sales',
        aggfunc='sum',
        fill_value=0
    )
    print("\nSales by customer type and order type by state:")
    print(pivot)
    export_to_excel(pivot)


def total_sales_quantity_price_by_region_product(df):
    pivot = pd.pivot_table(
        df,
        index=['sales_region', 'produce_name'],
        values=['quantity', 'sales'],
        aggfunc='sum',
        fill_value=0
    )
    print("\nTotal sales quantity and price by region and product:")
    print(pivot)
    export_to_excel(pivot)


def total_sales_quantity_price_by_customer_type(df):
    pivot = pd.pivot_table(
        df,
        index=['order_type', 'customer_type'],
        values=['quantity', 'sales'],
        aggfunc='sum',
        fill_value=0
    )
    print("\nTotal sales quantity and price by order type and customer type:")
    print(pivot)
    export_to_excel(pivot)


def max_min_sales_price_by_category(df):
    pivot = pd.pivot_table(
        df,
        index='product_category',
        values='sales',
        aggfunc=['max', 'min'],
        fill_value=0
    )
    print("\nMax and min sales price of sales by category:")
    print(pivot)
    export_to_excel(pivot)


def unique_employees_by_region(df):
    pivot = pd.pivot_table(
        df,
        index='sales_region',
        values='employee_id',
        aggfunc=pd.Series.nunique,
        fill_value=0
    )
    pivot.rename(columns={'employee_id': 'unique_employees'}, inplace=True)

    print("\nNumber of unique employees by region:")
    print(pivot)
    export_to_excel(pivot)

def create_custom_pivot_table(df):
    print("\n--- Pivot Table Generator ---")

    row_options = {
        "1": "employee_name",
        "2": "sales_region",
        "3": "product_category"
    }

    column_options = {
        "1": "order_type",
        "2": "customer_type"
    }

    value_options = {
        "1": "quantity",
        "2": "unit_price"
    }

    agg_options = {
        "1": "sum",
        "2": "mean",
        "3": "count"
    }

    def parse_choices(user_input, options_dict, allow_blank=False):
        user_input = user_input.strip()

        if allow_blank and user_input == "":
            return []

        choices = [choice.strip() for choice in user_input.split(",")]
        selected = []

        for choice in choices:
            if choice not in options_dict:
                return None
            selected.append(options_dict[choice])

        return selected

    print("\nSelect rows:")
    print("1. employee_name")
    print("2. sales_region")
    print("3. product_category")
    row_input = input("Enter the number(s) of your choice(s), separated by commas: ")
    rows = parse_choices(row_input, row_options)

    if rows is None or len(rows) == 0:
        print("Invalid row selection.")
        return

    print("\nSelect columns (optional):")
    print("1. order_type")
    print("2. customer_type")
    col_input = input("Enter the number(s) of your choice(s), separated by commas (enter for no grouping): ")
    columns = parse_choices(col_input, column_options, allow_blank=True)

    if columns is None:
        print("Invalid column selection.")
        return

    print("\nSelect values:")
    print("1. quantity")
    print("2. unit_price")
    value_input = input("Enter the number(s) of your choice(s), separated by commas: ")
    values = parse_choices(value_input, value_options)

    if values is None or len(values) == 0:
        print("Invalid value selection.")
        return

    print("\nSelect aggregation function:")
    print("1. sum")
    print("2. mean")
    print("3. count")
    agg_input = input("Enter the number of your choice: ").strip()

    if agg_input not in agg_options:
        print("Invalid aggregation function selection.")
        return

    aggfunc = agg_options[agg_input]

    needed_columns = rows + columns + values
    missing = [col for col in needed_columns if col not in df.columns]

    if missing:
        print(f"Cannot create pivot table. Missing columns: {missing}")
        return

    pivot = pd.pivot_table(
        df,
        index=rows,
        columns=columns if len(columns) > 0 else None,
        values=values,
        aggfunc=aggfunc,
        fill_value=0
    )
    print("\nGenerated Pivot Table:")
    print(pivot)
    export_to_excel(pivot)
    
# Menu Display
def display_menu(dataframe):
    menu_options = (
        ("Show the first n rows of sales data", show_first_n_rows),
        ("Total sales by region and order_type", total_sales_by_region_and_order_type),
        ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_sale_type),
        ("Sales by customer type and order type by state", sales_by_customer_type_order_type_state),
        ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
        ("Total sales quantity and price customer type", total_sales_quantity_price_by_customer_type),
        ("Max and min sales price of sales by category", max_min_sales_price_by_category),
        ("Number of unique employees by region", unique_employees_by_region),
        ("Create a custom pivot table", create_custom_pivot_table),
        ("Exit", None)
    )

    while True:
        print("\n--- Sales Data Dashboard ---")
        for i, (description, _) in enumerate(menu_options, start=1):
            print(f"{i}. {description}")

        choice = input(f"Enter your choice (1-{len(menu_options)}): ").strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(menu_options):
            print("Invalid choice. Please try again.")
            continue

        description, action = menu_options[choice - 1]

        if action is None:
            print("Exiting dashboard. Goodbye!")
            break

        action(dataframe)


# Call load_csv to load the data amd print the first 10 rows
filename = 'sales_data.csv'
sales_data = load_csv(filename)

# Run the main processing loop
def main():
    if sales_data is None:
        print("Sales data could not be loaded.")
        return

    display_data_summary(sales_data)
    display_menu(sales_data)

# Check if this is the main moduel being run
if __name__ == "__main__":
    main()