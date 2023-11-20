# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip
# at most k 0's.


def longest_ones(nums: list[int], k: int) -> int:
    left_index = current = answer = zero_counter = 0

    for right_index, right_val in enumerate(nums):
        if right_val == 0:
            zero_counter += 1

        if zero_counter > k:
            if nums[left_index] == 0:
                zero_counter -= 1
            left_index += 1

        if zero_counter <= k:
            current += 1
            answer = max(answer, right_index - left_index + 1)

    return answer


if __name__ == "__main__":
    print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
