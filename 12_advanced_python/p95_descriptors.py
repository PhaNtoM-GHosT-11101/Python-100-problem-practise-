"""
Problem 95: Descriptors
------------------------
Create descriptor classes for validated attributes:
  - Positive: value must be > 0
  - StringLength(min, max): string length in range
  - TypeChecked(type): enforces type

Use them in a Product class:
  name: StringLength(2, 50)
  price: Positive + TypeChecked(float)
  quantity: Positive + TypeChecked(int)
"""

# Write your solution below:


