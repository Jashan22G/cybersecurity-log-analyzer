logs = [
    "Login successful",
    "Login failed",
    "Login failed",
    "Login successful",
    "Login failed"
]

failed = logs.count("Login failed")

print("Total login attempts:", len(logs))
print("Failed attempts:", failed)

if failed >= 3:
    print("Warning: Multiple failed login attempts!")
else:
    print("No suspicious activity detected.")
