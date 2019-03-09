# duodecimal
try it out now [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fschmnn/duodecimal/master)

Python converter/calculator for the duodecimal numeral system (1,2,3,4,5,6,7,8,9,X,E)

## How to use
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
g = duo('X.31')
g.dec()
```
## Why base12?
We use base10 because of the number of fingers we have and not because it is easy to use. While it might be handy for counting, it has serious disadvantages for arithmic operations. This is because 12 has more divisors and hence most sequences in the multiplication table are shorter

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | X | E | 10|
|--|---|---|---|---|---|---|---|---|---|---|---|---|
|1 |1  |2 |3 |4 |5 |6 |7 |8 |9 |X |E |10|
|2 |2  |4 |6 |8 |X |10 |12 |14 |16 |18 |1X |20|
|3 |3  |6 |9 |10 |13 |16 |19 |20 |23 |26 |29 |30|
|4 |4  |8 |10 |14 |18 |20 |24 |28 |30 |34 |38 |40|
|5 |5  |X |13 |18 |21 |26 |2E |34 |39 |42 |47 |50|
|6 |6  |10 |16 |20 |26 |30 |36 |40 |46 |50 |56 |60|
|7 |7  |12 |19 |24 |2E |36 |41 |48 |53 |5X |65 |70|
|8 |8  |14 |20 |28 |34 |40 |48 |54 |60 |68 |74 |80|
|9 |9  |16 |23 |30 |39 |46 |53 |60 |69 |76 |83 |90|
|X |X  |18 |26 |34 |42 |50 |5X |68 |76 |84 |92 |X0|
|E |E  |1X |29 |38 |47 |56 |65 |74 |83 |92 |X1 |E0|
|10|10 |20 |30 |40 |50 |60 |70 |80 |90 |X0 |E0 |100|

another advantage is that more fractions have nice representations. 

|     | base10 | base 12|
|-----|:------:|:------:|
| 1/2 |  0.5   |  0.6   |
| 1/3 | 0.3333 |  0.4   |
| 1/4 |  0.25  |  0.3   |
| 1/5 | 0.2    |  0.2497 |
| 1/6 |  0.1666|  0.2   |
| 1/7 | 0.1429 |  0.186E |
| 1/8 |  0.125   |  0.16 |
| 1/9 | 0.1111 |  0.14  |
| 1/10| 0.1    |  0.1250 |
| 1/11| 0.0999 |  0.1111 |
| 1/12| 0.0833 |  0.1   |

For more information visit [Dozenal Society of America](http://www.dozenal.org/)
