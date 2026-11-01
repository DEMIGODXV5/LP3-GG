"""
The Greedy Method is an algorithm design technique that builds a solution step by step by selecting the best possible choice at the current stage.It makes a locally optimal choice at every step, hoping to achieve a globally optimal solution.

Job Sequencing is a scheduling problem in which each job has:
1. Job ID.
2. Deadline.
3. Profit.
Each job requires one unit of time, and only one job can be performed at a time.

"""

def job_sequencing(jobs):

    # Sort jobs according to profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Initialize time slots
    slots = [None] * max_deadline

    total_profit = 0

    # Schedule jobs
    for job in jobs:
        job_id, deadline, profit = job

        # Find latest available slot
        for j in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    # Display scheduled jobs
    print("\nScheduled Jobs:")

    for i in range(max_deadline):
        if slots[i] is not None:
            print(f"Time Slot {i + 1}: {slots[i]}")

    print("\nTotal Profit:", total_profit)


# Main Program
print("===== Job Sequencing with Deadlines =====")

n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    print(f"\nEnter details for Job {i + 1}:")

    job_id = input("Job ID: ")
    deadline = int(input("Deadline: "))
    profit = int(input("Profit: "))

    jobs.append((job_id, deadline, profit))

job_sequencing(jobs)