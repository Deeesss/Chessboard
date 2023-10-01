def print_chessboard(size):
    for i in range(size):
        for j in range(size):
            
                print("█", end="")
            
            else:
                print(" ", end="")
        print()  # Nový riadok po každom rriadku šachovnice

# Velikosť šachového pole (počet riadkov a stlpcou)
velikost = 8

# Vytlačí šachovnicu
print_chessboard(velikost)
