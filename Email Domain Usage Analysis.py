# Email list
emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]

# Step 1: Count domains
domain_count = {}

for email in emails:
    domain = email.split("@")[1]   # extract domain
    
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

# Step 2: Calculate percentage usage
total_users = len(emails)

print("Email Domain Usage:")
for domain, count in domain_count.items():
    percentage = (count / total_users) * 100
    print(f"{domain}: {percentage:.0f}%")
