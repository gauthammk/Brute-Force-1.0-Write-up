# Grep

Points : 25

## Solution

We are given a file with a lot of strings and we need to find the flag. This can be done by using a simple script as follows :

```sh
strings UNIX | grep "HE{.*}"
```

Flag : `HE{ecfc468968534a32fe335bba396fa519}`
