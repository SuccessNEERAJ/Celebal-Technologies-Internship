def upper_triangular(n):
    print("Upper Triangular Pattern:")
    for row in range(n):
        for col in range(row):
            print(" ", end=" ")  
        for star in range(n - row):
            print("*", end=" ") 
        print()
rows = 5
upper_triangular(rows)