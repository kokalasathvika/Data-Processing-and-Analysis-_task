# List of user IDs
user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]

# Step 1: Count frequency of each ID
id_count = {}

for uid in user_ids:
    if uid in id_count:
        id_count[uid] += 1
    else:
        id_count[uid] = 1

# Step 2: Display duplicates only
print("Duplicate User IDs:")

for uid, count in id_count.items():
    if count > 1:
        print(f"{uid} → {count} times")
