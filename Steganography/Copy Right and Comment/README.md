# Copy Right and Comment

Points : 75

## Solution

Simply running strings on the image gives us the flag. Here is the script to retrieve the flag :

```sh
strings key.jpg | grep "HE{.*}"
```

Flag : `HE{7e69c214546a931d52312bb92da9d87d}`
