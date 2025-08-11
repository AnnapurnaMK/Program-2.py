def generate_odd_series(count):
    """
    Generates the first 'count' odd numbers starting from 1.

    Parameters:
    count (int): The number of odd numbers to generate.

    Returns:
    list: A list of odd numbers.
    """
    return [2 * i + 1 for i in range(count)]


def main():
    try:
        # Take input from the user
        a = int(input("Enter a positive integer: "))

        # Validate the input
        if a <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        # Generate and display the series
        odd_series = generate_odd_series(a)
        print("Output:", ', '.join(map(str, odd_series)))

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()

