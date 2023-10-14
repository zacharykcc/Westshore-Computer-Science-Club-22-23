# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    # Read the number of categories and transactions
    num_categories, num_transactions = map(int, input().split())

    # Read initial balances and store them in a dictionary
    budget = {}
    for _ in range(num_categories):
        category, balance = input().split()
        budget[category] = int(balance)

    # Process transactions
    for _ in range(num_transactions):
        category, transaction_type, amount = input().split()
        amount = int(amount)
        if transaction_type == '+':
            budget[category] += amount
        else:
            if budget[category] >= amount:
                budget[category] -= amount

    # Output the final budget status
    for category, balance in budget.items():
        print(f'{category} {balance}')

    # Print a newline to separate test cases
    print()