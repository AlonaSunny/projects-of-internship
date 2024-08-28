
def strongPassword(password: str) -> int:
    missing_type = 3
    if any('a' <= c <= 'z' for c in password):
        missing_type -= 1
    if any('A' <= c <= 'Z' for c in password):
        missing_type -= 1
    if any(c.isdigit() for c in password):
        missing_type -= 1

    if len(password) < 6:
        return max(missing_type, 6 - len(password))
    elif len(password) > 20:
        return len(password) - 20 + missing_type
    else:
        repeat = 0
        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                repeat += 1
        return max(missing_type, repeat)
        
        
print(strongPassword("a")) # Output: 5
print(strongPassword("aA1")) # Output: 3
print(strongPassword("1337C0d3")) # Output: 0
print(strongPassword("aaa111")) # Output: 2
print(strongPassword("abcdef")) # Output: 2
print(strongPassword("ABABABAB")) # Output: 2
print(strongPassword("abcABC123")) # Output: 0
print(strongPassword("abcABC123!")) # Output: 0
print(strongPassword("abcABC123.!")) # Output: 0
print(strongPassword("abcABC123.!a")) # Output: 0
print(strongPassword("abcABC123.!aA")) # Output: 0
print(strongPassword("abcABC123.!aA1"))
