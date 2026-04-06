"""
Problem 69: Retry Decorator
-----------------------------
Write a @retry(max_attempts=3, delay=1) decorator that:
  - Retries a function if it raises an exception
  - Waits `delay` seconds between retries (use time.sleep)
  - Raises the last exception if all attempts fail
  - Logs each attempt

Test it on a function that randomly fails 70% of the time.
"""

# Write your solution below:


