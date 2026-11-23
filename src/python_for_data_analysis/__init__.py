def main() -> None:
    print("Hello from python-for-data-analysis!")
    random_list_data = [1, 2, 3, 4, 5]
    random_list_data.append(6)
    print(random_list_data)


def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


if __name__ == "__main__":
    main()
    add_numbers(1, 2)
