import re

def check_password_complexity(password):
    # Criteria definitions
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[\W_]', password) is not None,
    }

    # Evaluate criteria
    passed_criteria = sum(criteria.values())

    # Determine complexity level
    if passed_criteria == 5:
        complexity = 'Very Strong'
    elif passed_criteria == 4:
        complexity = 'Strong'
    elif passed_criteria == 3:
        complexity = 'Moderate'
    elif passed_criteria == 2:
        complexity = 'Weak'
    else:
        complexity = 'Very Weak'

    return complexity, criteria

# Example usage
password = input("Enter a password to check its complexity: ")
complexity, criteria = check_password_complexity(password)

print(f"Password Complexity: {complexity}")
print("Criteria Met:")
for criterion, met in criteria.items():
    print(f"  {criterion.capitalize()}: {'Yes' if met else 'No'}")
