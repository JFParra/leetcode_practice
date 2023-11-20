# https://leetcode.com/problems/is-subsequence/description/
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).
def is_subsequence(s: str, t: str) -> bool:
    """
    :param s: string that may or may not be subsequence of t
    :param t: string used to compare with s
    :return: true if s is a subsequence of t, or false otherwise.
    """

    s_tracker = 0

    if s:
        for c in t:
            if s_tracker == len(s):
                break

            elif s[s_tracker] == c:
                s_tracker += 1

    return True if s_tracker == len(s) else False


if __name__ == "__main__":
    # Input: s = "abc", t = "ahbgdc"
    print(is_subsequence("abc", "ahbgdc"))
    # Input: s = "", t = "ahbgdc"
    print(is_subsequence("", "ahbgdc"))
    # Input: s = "x", t = "ahbgdc"
    print(is_subsequence("x", "ahbgdc"))
