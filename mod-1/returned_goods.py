"""Returned Goods."""


# @TODO: Define a new function called process_claims
def process_claims(claims):
    total_claims = sum(claims)
    total_payout = total_claims * .30
    return total_payout
    # Inside of the function:
# Create a variable called `total_claims`, that is the sum of all claims
# Calculate a total payout, which is 30% of total_claims:
# Return only the total_payout amount


# @TODO Paste the list of weekly claims:
weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]
print(sum(weekly_claims))
print(process_claims(weekly_claims))

# What's the total insurance payout?
# Use the print() statement to print the returned value from the function.
# @TODO: Call the function using `weekly_claims` as the function argument
# YOUR CODE HERE!
principle = 103208.56
interest_rates = [.103, .067, .099, .10]
total_interest = 0.0
for rate in interest_rates:
    interest = rate * principle
    total_interest = total_interest + interest
    print("Your interest will be: ", interest)
print("The total interest is: ", total_interest)