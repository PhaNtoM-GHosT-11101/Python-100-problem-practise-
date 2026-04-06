"""
Problem 60: dataclasses Module
--------------------------------
Create a Student dataclass with:
  name: str
  roll: int
  cgpa: float = 0.0
  courses: list = field(default_factory=list)

  - Add a method grade() that returns letter grade based on cgpa
  - Use __post_init__ to validate cgpa is between 0 and 10
  - Create a list of 3 students and sort by cgpa descending
"""

# Write your solution below:


