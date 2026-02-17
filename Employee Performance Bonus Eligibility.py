# Employee performance data
employees = {
    "Ravi": 92,
    "Anita": 88,
    "Kiran": 92,
    "Suresh": 85
}

# Step 1: Find the highest performance score
highest_score = max(employees.values())

# Step 2: Find all employees who have this highest score
top_performers = []

for name, score in employees.items():
    if score == highest_score:
        top_performers.append(name)

# Step 3: Convert list to comma-separated string
top_performers_str = ", ".join(top_performers)

# Step 4: Display result
print(f"Top Performers Eligible for Bonus: {top_performers_str} (Score: {highest_score})")
