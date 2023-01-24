#!/usr/bin//env python3

# Created by: maliksalem1
# Created on: October 2022
# This program compares two numbers


def main():
    pairs = []

    for i in range(10, 50):
        for j in range(i + 1, 51):
            if i + j == 60 and abs(i - j) == 14:
                pairs.append((i, j))

    print(pairs)
    print("\nDone.")


if __name__ == "__main__":
    main()
