import sys

MIRROR_MAP = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8'}

def is_palindrome(s):
    return s == s[::-1]

def is_mirrored(s):
    mirrored_chars = []
    for char in s:
        if char in MIRROR_MAP:
            mirrored_chars.append(MIRROR_MAP[char])
        else:
            return False
    
    mirrored_str = "".join(mirrored_chars)
    return mirrored_str[::-1] == s

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
        
    p = is_palindrome(s)
    m = is_mirrored(s)
    
    if p and m:
        print(f"{s} -- is a mirrored palindrome.")
    elif p and not m:
        print(f"{s} -- is a regular palindrome.")
    elif not p and m:
        print(f"{s} -- is a mirrored string.")
    else:
        print(f"{s} -- is not a palindrome.")
        
    print()