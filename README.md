## Formatting

join()
```python
#string.join(iterable)
print(".".join(["abc", "def", "ghi"]))
# >> abc.def.ghi
```
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

## Cryptography

### Sha256
```python
import hashlib
sha256_string = hashlib.sha256(s.encode('utf-8')).hexdigest()
```