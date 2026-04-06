# Name: Jordyn Pendergrass
# Date: April 5, 2026

import time

import pandas as pd
import numpy as np
import pyarrow


pd.set_option('display.max_columns', None) #show all columns in the output


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
        df.fillna(0, inplace=True) # fill any missing values with 0
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


# Menu Options
def show_first_n_rows(df):
    try:
        n = int(input("Enter the number of rows to display: "))
        print(df.head(n))
    except ValueError:
        print("Please enter a valid number.")


def total_sales_by_region_and_order_type(df):
    needed = ['region', 'order_type', 'sales']
    if not check_columns(df, needed):
        return

    result = df.groupby(['region', 'order_type'])['sales'].sum().reset_index()
    print("\nTotal Sales by Region and Order Type:")
    print(result)


def average_sales_by_region_state_sale_type(df):
    needed = ['region', 'state', 'sale_type', 'sales']
    if not check_columns(df, needed):
        return

    result = df.groupby(['region', 'state', 'sale_type'])['sales'].mean().reset_index()
    print("\nAverage Sales by Region, State, and Sale Type:")
    print(result)


def sales_by_customer_type_order_type_state(df):
    needed = ['customer_type', 'order_type', 'state', 'sales']
    if not check_columns(df, needed):
        return

    result = df.groupby(['customer_type', 'order_type', 'state'])['sales'].sum().reset_index()
    print("\nSales by Customer Type, Order Type, and State:")
    print(result)


def total_sales_quantity_price_by_region_product(df):
    needed = ['region', 'product', 'quantity', 'unit_price', 'sales']
    if not check_columns(df, needed):
        return

    result = df.groupby(['region', 'product']).agg(
        total_quantity=('quantity', 'sum'),
        total_unit_price=('unit_price', 'sum'),
        total_sales=('sales', 'sum')
    ).reset_index()

    print("\nTotal Sales Quantity and Price by Region and Product:")
    print(result)


def total_sales_quantity_price_by_customer_type(df):
    needed = ['customer_type', 'quantity', 'unit_price', 'sales']
    if not check_columns(df, needed):
        return

    result = df.groupby('customer_type').agg(
        total_quantity=('quantity', 'sum'),
        total_unit_price=('unit_price', 'sum'),
        total_sales=('sales', 'sum')
    ).reset_index()

    print("\nTotal Sales Quantity and Price by Customer Type:")
    print(result)


def max_min_sales_price_by_category(df):
    needed = ['category', 'sales']
    if not check_columns(df, needed):
        return

    result = df.groupby('category')['sales'].agg(['max', 'min']).reset_index()
    print("\nMax and Min Sales by Category:")
    print(result)


def unique_employees_by_region(df):
    needed = ['region', 'employee_id']
    if not check_columns(df, needed):
        return

    result = df.groupby('region')['employee_id'].nunique().reset_index()
    result.rename(columns={'employee_id': 'unique_employees'}, inplace=True)

    print("\nNumber of Unique Employees by Region:")
    print(result)


def create_custom_pivot_table(df):
    print("\nCreate a Custom Pivot Table")
    print("Available columns:")
    print(df.columns.tolist())

    try:
        index_col = input("Enter column for rows (index): ").strip()
        columns_col = input("Enter column for columns: ").strip()
        values_col = input("Enter column for values: ").strip()
        agg_func = input("Enter aggregation function (sum, mean, count, max, min): ").strip()

        if index_col not in df.columns or columns_col not in df.columns or values_col not in df.columns:
            print("One or more column names are invalid.")
            return

        if agg_func not in ['sum', 'mean', 'count', 'max', 'min']:
            print("Invalid aggregation function.")
            return

        pivot = pd.pivot_table(
            df,
            index=index_col,
            columns=columns_col,
            values=values_col,
            aggfunc=agg_func,
            fill_value=0
        )

        print("\nCustom Pivot Table:")
        print(pivot)

    except Exception as e:
        print(f"Error creating pivot table: {e}")

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

    print("Available options:")
    for i, (description, _) in enumerate(menu_options, start=1):
        print(f"{i}. {description}")

    try:
        menu_len = len(menu_options)
        choice = int(input(f"Enter your choice (1-{menu_len}): "))
        if 1 <= choice <= menu_len:
            action = menu_options[choice - 1][1]
            action(dataframe)
        if action == "Exit":
            print("Exiting dashboard. Goodbye!")
        else:
            print("Invalid choice. Please enter a number corresponding to the options.")

    except ValueError:
        print("Invalid input. Please enter a number corresponding to the options.")




# Call load_csv to load the data amd print the first 10 rows
filename = 'sales_data.csv'
sales_data = load_csv(filename)

# Run the main processing loop
def main():
    while True:
        print("Sales Data Dashboard")
        display_menu(sales_data)

# Check if this is the main moduel being run
if __name__ == "__main__":
    main()