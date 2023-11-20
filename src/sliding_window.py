# Example 1:
# Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum
# is less than or equal to k.


def longest_sum_subarray(nums: list[int], k: int) -> int:
    left_index = curr = answer = 0

    # Slide window right
    for right_index, val in enumerate(nums):
        curr += val

        # Slide window left
        while curr > k:
            curr -= nums[left_index]
            left_index += 1

        # Length is right_index - left_index and +1 due to 0 based index
        answer = max(answer, right_index - left_index + 1)

    return answer


# Example 2:
# You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and
# flip it to a "1". What is the length of the longest substring achievable that contains only "1"?


# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes
# 1111100111.


def longest_substring(s: str) -> int:
    # curr is the current number of zeros in the window
    left_index = curr = answer = 0

    for right_index, val in enumerate(s):
        if val == "0":
            curr += 1

        while curr > 1:
            if s[left_index] == "0":
                curr -= 1
            left_index += 1

        answer = max(answer, right_index - left_index + 1)

    return answer


# Example 3:
# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all
# the elements in the subarray is strictly less than k.


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    if k == 0 or k == 1:
        return 0

    left_index = 0
    curr = 1
    answer = 0

    for right_index, right_val in enumerate(nums):
        curr *= right_val
        while curr >= k:
            curr //= nums[left_index]
            left_index += 1

        answer += right_index - left_index + 1
        print(answer)

    return answer


# Example 4:
# Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.


def sum_of_longest_subarray(nums: list[int], k: int) -> int:
    left_index = curr = answer = 0

    for right_index, right_val in enumerate(nums):
        curr += right_val
        length = right_index - left_index + 1

        while length > k:
            curr -= nums[left_index]
            left_index += 1
            length = right_index - left_index + 1

        answer = max(answer, curr)

    return answer


if __name__ == "__main__":
    # print(longest_sum_subarray([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
    # print(longest_substring("1101100111"))
    # print(num_subarray_product_less_than_k([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
    # print(num_subarray_product_less_than_k([10, 5, 2, 6], 100))

    print(sum_of_longest_subarray([3, -1, 4, 12, -8, 5, 6], 4))
