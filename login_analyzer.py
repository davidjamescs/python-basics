successful_logins = 8
failed_logins = 3

total_attempts = successful_logins + failed_logins

print("Total login attempts:", total_attempts)
print("Successful logins:", successful_logins)
print("Failed logins:", failed_logins)

if failed_logins >= 3:
    print("Warning: Multiple failed login attempts detected.")
else:
    print("Login activity appears normal.")
