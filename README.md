# duodecimal
Python converter/calculator for the duodecimal numeral system

```python
from duodecimal import duo
```
A duodecimal number can be initialized by passing a duodecimal number as a string or a decimal number as an int/float
```python
a = duo('1X.23')  # initialize with duodecimal value
b = duo(3.14)     # initialize with decimal value
```
All basic math operations are supported. The first part must be an instance of the duo class. The second one can be another instance or any valid input for the duo class
```python
c = a + b
d = a - 2
e = b * duo(1/2)
f = duo(20) / 'X'
```
The decimal representation can be accessed via
```python
g = duo('X.31)
g.dec()
```
