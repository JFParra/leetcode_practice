# https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


def is_palindrome(s: str) -> bool:
    if len(s) == 1:
        return True

    if s:
        parsed = ""

        for c in s:
            if c.isalnum():
                parsed += c.lower()

        if len(parsed) == 1:
            return True

        first = 0
        last = len(parsed) - 1

        while first < last:
            if parsed[first] != parsed[last]:
                return False

            first += 1
            last -= 1

        return True

    return False


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("0P"))
    print(is_palindrome("a."))
    print(is_palindrome(" "))
    print(is_palindrome(""))
