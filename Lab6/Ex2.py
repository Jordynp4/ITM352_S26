# Create a list with different types of values (one example)
my_list = [42, "hello", 3.14, True, "python", 99]

# Test cases: list of lists covering each length condition
test_cases = [
    [],                      # length 0 -> fewer than 5
    [42],                    # length 1 -> fewer than 5
    [1, 2, 3, 4],            # length 4 -> fewer than 5
    [1, 2, 3, 4, 5],         # length 5 -> between 5 and 10
    list(range(6)),         # length 6 -> between 5 and 10
    list(range(10)),        # length 10 -> between 5 and 10
    list(range(11)),        # length 11 -> more than 10
    my_list                 # example original list (length 6)
]


for idx, lst in enumerate(test_cases, start=1):
    length = len(lst)
    print(f"Test case {idx}: length={length} -> {lst}")
    if length < 5:
        print("The list has fewer than 5 elements.")
    elif 5 <= length <= 10:
        print("The list has between 5 and 10 elements.")
    else:
        print("The list has more than 10 elements.")
    print()