# @copyright Deborah Kitchin

def main() -> None:

    a = 45.75
    b = 0.18
    c = 0.08
    d = 4
    x = a * b
    y = a * c
    z = a + x + y

    print("Subtotal:", a)
    print("Thing 1:", x)
    print("Thing 2:", y)
    print("Final amount:", z)

    # More confusing calculations
    temp = z / d
    data = temp * 2
    result = data - 5

    print(f"Per person after weird math: {result:.2f}")

if __name__ == "__main__":
    main()