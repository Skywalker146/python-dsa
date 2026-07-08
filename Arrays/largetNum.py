def find_largest(nums):
    """Return the largest number in the list."""
    largest = nums[0]
    n = len(nums)

    for i in range(n):
        largest = max(largest, nums[i])

    return largest


def main():
    # Take input: first line = size, second line = space-separated numbers
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter the numbers (space-separated): ").split()))

    if len(nums) != n:
        print(f"Warning: expected {n} numbers, got {len(nums)}. Using what you entered.")

    if not nums:
        print("Array is empty!")
        return

    result = find_largest(nums)
    print("Largest number is:", result)


if __name__ == "__main__":
    main()
