# Name: Jordyn Pendergrass
# Date: Feb 3, 2026

url = input("Enter a full URL: ")

cleaned_url = url.replace("https://", "")
print("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".")

domain = parts[1]
print("Domain:", domain)

TLD = parts[2]
TLD_cleaned = TLD.strip("/")
print("Top Level Domain:", TLD_cleaned)