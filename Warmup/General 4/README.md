# General 4

Points : 20

## Solution

We are asked to rotate the following string to get the flag : `NK{Xuzgzk_Sk_ZU_Mkz_Vuotzy}`. Since we know the flag format i.e, `HE{}`, we can employ the following script to find the offset:

```python
print('Offset = ', ord('N') - ord('H'))
```

Flag : `HE{Rotate_Me_TO_Get_Points}`
