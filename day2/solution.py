def get_reports(lines: list[str]) -> list[list[int]]:
    return []


def main():
    test = True
    file = "test_input.txt" if test else "real_input.txt"

    with open(file, "r") as f:
        lines = f.readlines()


if __name__ == "__main__":
    main()
