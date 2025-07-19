from all_different import all_different

def main() -> None:

    if all_different (1,1,1):
        print(f'ERROR: all_different (1,1,1) should be False.')
    else:
        print(f'Correct: all_different (1,1,1) is False')

    if all_different (1,1,2):
        print(f'ERROR: all_different (1,1,2) should be False.')
    else:
        print(f'Correct: all_different (1,1,2) is False')

    if all_different (1,2,2):
        print(f'ERROR: all_different (1,2,2) should be False.')
    else:
        print(f'Correct: all_different (1,2,2) is False')

    if all_different (2,1,2):
        print(f'ERROR: all_different (2,1,2) should be False.')
    else:
        print(f'Correct: all_different (2,1,2) is False')

    if not all_different (1,2,3):
        print(f'ERROR: all_different (1,2,3) should be False.')
    else:
        print(f'Correct: all_different (1,2,3) is True')

    assert all_different(1,1,1) == False, f'all_different(1,1,1) expected False got: {all_different(1,1,1)}'
    assert all_different(1,1,2) == False, f'all_different(1,1,2) expected False got: {all_different(1,1,1)}'
    assert all_different(1,2,2) == False, f'all_different(1,2,2) expected False got: {all_different(1,2,2)}'
    assert all_different(1,1,1) == False, f'all_different(2,1,2) expected False got: {all_different(2,1,2)}'
    assert all_different(1,2,3) == True, f'all_different(1,2,3) expected False got: {all_different(1,2,2)}'


# @return different indicating if 3 variables are different
if __name__ == "__main__":
    main()
