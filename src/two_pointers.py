def palidrome_check(input_str: str) -> bool:
    first = 0
    last = len(input_str) - 1

    while first < last:
        if input_str[first] != input_str[last]:
            return False

        first += 1
        last -= 1

    return True


def sorted_two_sums(nums: list[int], target: int) -> bool:
    f = 0
    l = len(nums) - 1

    while f < l:
        if nums[f] + nums[l] == target:
            return True
        elif nums[f] + nums[l] > target:
            l -= 1
        else:
            f += 1

    return False


def merge_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    index = 0
    final: list[int] = []

    largest_list = a if len(a) > len(b) else b

    while index < len(largest_list) - 1:
        if len(a) - 1 > index and len(b) - 1 > index:
            if a[index] < b[index]:
                final.append()


if __name__ == "__main__":
    print(sorted_two_sums([1, 2, 4, 6, 8, 9, 14, 15], 13))
    print(palidrome_check("abcdcba"))

    print(merge_sorted_lists([1, 4, 7, 20], [3, 5, 6]))
