"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Sales: "))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.15
    total_bonus = sales * bonus_rate
    print(f"Bonus: ${total_bonus:.2f}")
    sales = float(input("Sales: "))
