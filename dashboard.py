import csv

days = []
sales = []

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        days.append(row["day"])
        sales.append(int(row["sales"]))

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)

best_day = days[sales.index(highest_sale)]
worst_day = days[sales.index(lowest_sale)]

print("=== Mini Sales Dashboard ===")
print("Total Sales:", total_sales)
print("Average Sale:", round(average_sales, 2))
print("Highest Sale:", highest_sale, "on", best_day)
print("Lowest Sale:", lowest_sale, "on", worst_day)
