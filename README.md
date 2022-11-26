## Formatting

join()
```python
#string.join(iterable)
print(".".join(["abc", "def", "ghi"]))
# >> abc.def.ghi
```

*Unicode Character*
```python
ord("a") # > 97 is the unicode for a
chr(97) # > "a" is the character of unicode 97
```

*Case*
"APPLE".lower() = "apple"
"apple".upper() = "APPLE"

# Math

*Exponents*
```python
v = pow(3,2) # > 3^2 = 9
v = 3**2  # > 3^2 = 9
```
*with Modulus*
```python
# (3^2)%4
v = pow(3,2, 4) # > 9 % 4 = 1
v = (3**2)%4 # > 9 % 4 = 1
```

*To receive a Float*
```python
import math
math.pow(2,5) # >> 25.0
```

*Convert to Hex*
```python
hex_val = hex(15) # >> 0xf
hex_val = hex(15)[:2] # >> f (remove the '0x')
```
## Sorting

*sorted(iterable, key=key, reverse=reverse)*
```python
sorted_numbers = sorted([3, 2, 1]) # > [1,2,3]
reverse_sorted_numbers = sorted([3, 4, 1, 4]) # > [3,2,1]
```

## Cryptography

### Sha256
```python
import hashlib
sha256_string = hashlib.sha256(s.encode('utf-8')).hexdigest()
```

## Arrays

### Arrays
*Shortest string in an array of strings*
```python
shortest_str = min(["a", "bc", "def"], key=len) # >> returns "a" 
```