import ssl
from turtle import pd
import urllib.request

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL: " + url)
web_page = urllib.request.urlopen(url)
data_frame = pd.read_html(web_page)


one_month_rate = data_frame[0].loc[0, "1 Mo"]


for index, row in data_frame[0].iterrows():
    if row["Date"] == "2026-03-01":
        one_month_rate = row["1 Mo"]
        print(f"1 month interest rate on 2026-03-01: {one_month_rate}")
        break