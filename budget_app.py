class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    total_spent = sum(-item["amount"]
                      for cat in categories for item in cat.ledger if item["amount"] < 0)
    spent_per_category = [
        sum(-item["amount"] for item in cat.ledger if item["amount"] < 0) for cat in categories]

    percentages = [(spend / total_spent * 100) // 10 *
                   10 for spend in spent_per_category]

    chart = "Percentage spent by category\n"
    for percent in range(100, -1, -10):
        chart += f"{percent:>3}| " + \
            "  ".join("o" if p >= percent else " " for p in percentages) + "  \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_length) for cat in categories]

    for i in range(max_length):
        chart += "     " + "  ".join(name[i] for name in names) + "  \n"

    return chart.rstrip("\n")


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(250, "car repair")

print(food)
print()
print(create_spend_chart([food, clothing, auto]))
