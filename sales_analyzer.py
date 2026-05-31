with open("sales.csv", "r") as file:

    data = file.readlines()

    product_sales = {}
    total_sales = 0

    for line in data[1:]:

        product, quantity, price = line.strip().split(",")

        quantity = int(quantity)
        price = int(price)

        sale_amount = quantity * price

        total_sales += sale_amount

        if product in product_sales:
            product_sales[product] += sale_amount
        else:
            product_sales[product] = sale_amount


top_product = max(product_sales, key=product_sales.get)
lowest_product = min(product_sales, key=product_sales.get)


print("\nTOTAL SALES REPORT")
print("===================")
print("Total Sales:", total_sales)

print("\nPRODUCT WISE SALES")
print("===================")

for product, sales in product_sales.items():
    print(f"{product:<12} : ₹{sales:,}")


print("\nTOP & LOWEST PRODUCTS")
print("=====================")
print("Top Product   :", top_product, "₹", f"{product_sales[top_product]:,}")
print("Lowest Product:", lowest_product, "₹", f"{product_sales[lowest_product]:,}")


with open("report.txt", "w", encoding="utf-8") as report:

    report.write("SALES REPORT\n")
    report.write("====================\n\n")

    report.write(f"Total Sales: ₹{total_sales:,}\n\n")

    report.write("Product Wise Sales:\n")

    for product, sales in product_sales.items():
        report.write(f"{product}: ₹{sales:,}\n")

    report.write("\n")
    report.write(f"Top Product: {top_product} (₹{product_sales[top_product]:,})\n")
    report.write(f"Lowest Product: {lowest_product} (₹{product_sales[lowest_product]:,})\n")
