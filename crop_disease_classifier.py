def classify_leaf(color, spots, texture):
    if spots > 5 or color == "yellow":
        return "Diseased"
    else:
        return "Healthy"

def main():
    print("Welcome to AI-based Agriculture Learning Portal")
    color = input("Enter leaf color (green/yellow): ").lower()
    spots = int(input("Enter number of spots on leaf: "))
    texture = input("Enter leaf texture (smooth/rough): ").lower()

    result = classify_leaf(color, spots, texture)
    print(f"The leaf is classified as: {result}")

if __name__ == "__main__":
    main()
