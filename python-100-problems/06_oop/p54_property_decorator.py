"""
Problem 54: @property and Encapsulation
-----------------------------------------
Create a Temperature class:
  - Store temperature in Celsius internally
  - @property celsius: getter and setter (reject < -273.15)
  - @property fahrenheit: read-only, computed from celsius
  - @property kelvin: read-only

t = Temperature(25)
print(t.fahrenheit)  → 77.0
print(t.kelvin)      → 298.15
t.celsius = -300     → raises ValueError
"""

# Write your solution below:


