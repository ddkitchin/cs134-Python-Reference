def main() -> None:
    total_hours = 0

    class_hours = int(input("Enter class hours "))

    while total_hours + class_hours <= 16:
        total_hours = total_hours + class_hours
        #print(f'In Loop total_hours = {total_hours}')
        class_hours = int(input("Enter class hours "))

    print(f'total_hours = {total_hours}')


if __name__ == "__main__":
    main()