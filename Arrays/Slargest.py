def find_second_largest(nums):
    """Return the second largest number in the list (one-pass optimal solution)."""
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    for i in range(n):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]

    return s_largest


def find_second_largest_two_pass(nums):
    """Return the second largest using two passes (for learning)."""
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    for i in range(n):
        largest = max(largest, nums[i])

    for i in range(n):
        if nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]

    return s_largest


def main():
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter the numbers (space-separated): ").split()))

    if len(nums) != n:
        print(f"Warning: expected {n} numbers, got {len(nums)}. Using what you entered.")

    if len(nums) < 2:
        print("Need at least 2 numbers to find second largest!")
        return

    result = find_second_largest(nums)

    if result == float("-inf"):
        print("Second largest does not exist (all elements may be the same).")
        return

    print("Second largest number is:", int(result))


if __name__ == "__main__":
    main()
