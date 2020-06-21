offset = ord('A') - 1
nums = [8, 5, '{', 20, 8, 5, '_', 2, 1, 19, 9, 3,
        '_', 14, 21, 13, 2, 5, 18, '_', 7, 1, 13, 5, '}']
for num in nums:
    if num == '{' or num == '}' or num == '_':
        print(num, end='')
    else:
        print(chr(num + offset), end='')
