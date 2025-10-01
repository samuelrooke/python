# Python Control Structures: While and For Loops

## While Loops

### Basic Syntax
```python
while condition:
    # code block
    # remember to update condition variable!
```

### Example: Countdown
```python
laskuri = 10 
while laskuri > 0:
    print(laskuri) 
    laskuri = laskuri - 1  # Fixed: was .1, should be -1
print('Liftoff!')
```

## For Loops

### Basic Syntax
```python
for variable in iterable:
    # code block
```

### Examples
```python
# Loop through range
for i in range(5):
    print(i)

# Loop through list
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
```

## Print Function Tips

### End Parameter
Use `end` parameter to control line endings:
```python
print("Hello", end=' ')  # Prints on same line
print("World")           # Output: "Hello World"
```

### Formatting
```python
name = "Python"
version = 3.11
print(f"Language: {name}, Version: {version}")
```

## References
- Chapter 15, 16, 17 in course material
- Decimal module: `decimal.ROUND_CEILING` for rounding operations
