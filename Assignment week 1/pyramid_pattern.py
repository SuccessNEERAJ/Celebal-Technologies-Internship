def pyramid(n):
    print("Pyramid Pattern:")
    for row in range(n):
        print(" " * (n - row - 1), end="")  
        print("* " * (row + 1))             
rows = 5
pyramid(rows)