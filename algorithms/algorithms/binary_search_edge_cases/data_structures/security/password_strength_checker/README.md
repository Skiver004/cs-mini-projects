## Password Strength Checker

### Problem
Weak passwords are a common security vulnerability.  
Checking password strength programmatically helps users create stronger passwords.

### Approach
- Validate passwords based on length, uppercase, lowercase, numeric, and special characters  
- Test multiple edge cases to ensure checks are accurate

### Edge Cases Tested
- Too short passwords  
- Missing uppercase letters  
- Missing lowercase letters  
- Missing numbers  
- Missing special characters  
- Strong password (all conditions met)

### Observations
- Most passwords fail one or more conditions  
- Edge-case testing ensures that validation is reliable

### Lesson Learned
Security requires anticipating **user mistakes** and **testing edge cases**, not just implementing rules.
