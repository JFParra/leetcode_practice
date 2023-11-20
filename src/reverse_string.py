# https://leetcode.com/problems/reverse-string/description/
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


def reverse_string(s: list[str]) -> None:
    """
    :param s: list of chars to be reversed

    Do not return anything, modify s in-place instead.
    """

    first = 0
    last = len(s) - 1

    while first < last:
        a = s[first]
        b = s[last]

        s[first] = b
        s[last] = a


if __name__ == "__main__":
    print(reverse_string(["h", "e", "l", "l", "o"]))
    print(reverse_string(["H", "a", "n", "n", "a", "h"]))
