# Task 1

for num in range(1,20):
    if num % 2 == 0 and num % 7 == 0:
        print(" -> CRITICAL: Blocked by Safety Guard")
    elif num % 2 == 0:
        print(" -> Safe Content")
    elif num % 7 == 0:
        print(" -> Flagged: System Warning")
    else:
        print(" -> Standard Token")


#Task 2

requests = [15, 30, 45, 10, 25, 50]
total_tokens = 0

for req in requests:
    total_tokens = total_tokens + req
    if total_tokens > 100:
        print(f"Budget Exceeded! Stopping stream at { total_tokens } tokens.")
        break
    else:
        print(f"Processed request. Current total: { total_tokens } tokens.")


