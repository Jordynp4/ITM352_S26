import importlib.util

packages = ["scipy", "statsmodels", "matplotlib"]

for package in packages:
    spec = importlib.util.find_spec(package)
    if spec is not None:
        print(f"{package} is installed")
    else:
        print(f"{package} is NOT installed")