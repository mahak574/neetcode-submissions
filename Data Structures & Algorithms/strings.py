# Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    window = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# Test cases
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))      # 1
print(length_of_longest_substring("pwwkew"))     # 3
print(length_of_longest_substring(""))           # 0

# Complexity
# Time: O(n) — the string is traversed only once.
# Space: O(min(n, m)) — where m is the size of the character set