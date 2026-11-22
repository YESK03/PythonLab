# Experiment 8: Regular Expressions for Email and Mobile Number Validation

## AIM

To validate an email address or a 10-digit mobile number using Python's built-in `re` module and regular-expression pattern matching.

## OBJECTIVES

1. Understand the use of regular expressions in Python.
2. Use the `re.fullmatch()` function to check whether the complete input matches a pattern.
3. Define separate patterns for email addresses and mobile numbers.
4. Display whether the entered value is a valid email ID, a valid mobile number, or invalid input.

## ALGORITHM

1. Import the `re` module.
2. Read an email address or mobile number from the user and store it in `data`.
3. Define an email pattern using the regular-expression syntax.
4. Define a mobile-number pattern that accepts exactly 10 digits.
5. Check whether `data` fully matches the email pattern using `re.fullmatch()`.
6. If it matches the email pattern, print `Valid Email ID`.
7. Otherwise, check whether `data` fully matches the mobile-number pattern using `re.fullmatch()`.
8. If it matches the mobile-number pattern, print `Valid mobile Number`.
9. Otherwise, print `Given value not valid`.

## Pseudocode

```text
START
IMPORT re

INPUT data

email_pattern ← regular expression for a valid email address
mobile_pattern ← regular expression for exactly 10 digits

IF re.fullmatch(email_pattern, data) THEN
    PRINT "Valid Email ID"
ELSE IF re.fullmatch(mobile_pattern, data) THEN
    PRINT "Valid mobile Number"
ELSE
    PRINT "Given value not valid"
END IF

END
```

## Example Input and Output

```text
Input: student123@gmail.com
Output: Valid Email ID

Input: 9876543210
Output: Valid mobile Number

Input: hello123
Output: Given value not valid
```

## LEARNING OUTCOMES

After completing this experiment, students will be able to:

- Import and use Python's `re` module.
- Define regular-expression patterns.
- Apply `re.fullmatch()` for complete-input validation.
- Validate email addresses and 10-digit mobile numbers.
- Use conditional statements to select and display the appropriate result.
