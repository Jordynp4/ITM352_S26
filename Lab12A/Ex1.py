


import urllib.request
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

print("Opening URL: " + url)
web_page = urllib.request.urlopen(url)


for line in web_page:
    line = line.decode("utf-8")
    if "<title>" in line:
        print(line.strip())