def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)
    for i in range(rows - 1, 0, -1):
        print("*" * i)


# Test the function
rows = int(input("Enter the number of rows: "))
print_star_pattern(rows)
