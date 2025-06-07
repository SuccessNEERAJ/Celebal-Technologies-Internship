def lower_triangular(n):
    print("Lower Triangular Pattern:")
    for row in range(n):
        for col in range(row + 1):
            print("*", end=" ")
        print()
rows = 5
lower_triangular(rows)