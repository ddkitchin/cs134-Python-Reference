# @ copyright Deborah Kitchin
def main():
    print(factorial(int(input("Enter an integer "))))


def factorial(n):
    answer = 1
    for i in range(0, n):
        answer = answer * (n - i)
        print("Line  9 answer=%d" % answer)
    print("Line 10 n=%d answer=%d" % (n, answer))
    return answer


if __name__ == "__main__":
    main()