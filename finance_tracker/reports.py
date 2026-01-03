from collections import defaultdict
def monthly(expenses):
    result = defaultdict(float)
    for e in expenses:
        key = e.date.strftime("%Y-%m")
        result[key] += e.amount
    return result
def category(expenses):
    result = defaultdict(float)
    for e in expenses:
        result[e.category] += e.amount
    return result
def stats(expenses):
    amounts = [e.amount for e in expenses]
    if not amounts:
        return {}
    return {
        "Total": sum(amounts),
        "Highest": max(amounts),
        "Lowest": min(amounts),
        "Average": sum(amounts) / len(amounts)
    }
