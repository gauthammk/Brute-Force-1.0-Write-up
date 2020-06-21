# General 3

Points : 20

## Solution

We are asked to reverse this particular string : `10947f32df25eb4ce3de359176b20271`. We can do this witha simple script as follows:

```python
String = `10947f32df25eb4ce3de359176b20271`
flag = 'HE{' + String[::-1] + '}'
print(flag)
```

Flag : `HE{17202b671953ed3ec4be52fd23f74901}`
