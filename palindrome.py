def reverse_string(s):
    temp = ''
    for char in s:
        temp = char + temp
    return temp


def is_palindrome(s):
    return reverse_string(s) == s


def is_palindrome_v2(s):
    n = len(s)
    return s[:n // 2] == reverse_string(s[n - (n // 2):])


def is_palindrome_v3(s):
    i = 0  # hold the first character
    j = len(s) - 1  # represents the last charcter

    while i < j and s[i] == s[j]:
        i += 1  # we increment i by 1 and decrement j by 1
        j -= 1
    return j <= i
