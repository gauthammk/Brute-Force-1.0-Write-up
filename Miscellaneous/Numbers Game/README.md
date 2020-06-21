# Numbers Game

Points : 50

## Solution

We are given a picture with the words represented as numbers i.e, 1 = A,2 = B, 3 = C, and so on.
We can create a script to find the character representation of the given numbers and convert them manually.

```python
offset = ord('A') - 1
nums = [8, 5, '{', 20, 8, 5, '_', 2, 1, 19, 9, 3,
        '_', 14, 21, 13, 2, 5, 18, '_', 7, 1, 13, 5, '}']
for num in nums:
    if num == '{' or num == '}' or num == '_':
        print(num, end='')
    else:
        print(chr(num + offset), end='')
```

Flag : `HE{THE_BASIC_NUMBER_GAME}`
