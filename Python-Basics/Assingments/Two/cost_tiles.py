def find_cost_of_tiles(width, length, cost):
    result = width * length * cost
    return result

def main():
    width = float(input("Width of floor: "))
    length = float(input("Length of floor: "))
    cost = float(input("Cost of Tile: "))
    cost_of_tiles = find_cost_of_tiles(width, length, cost)
    print(cost_of_tiles)

if __name__ == "__main__":
    main()