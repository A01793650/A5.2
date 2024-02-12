"""Module providing a function printing python version."""
import sys
import json
import time


def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except (IOError, ValueError) as e:
        print(f"Error loading JSON file '{file_path}': {e}")
        return None


def compute_total_cost(price_catalog, sales_record):
    """Compute the total cost for all sales."""
    total_cost = 0

    for sale in sales_record:
        product_id = sale.get('Product')
        quantity = sale.get('Quantity')

        if product_id is not None and quantity is not None:
            for price in price_catalog:
                product = price.get('title')
                if product_id == product:
                    product_price = price.get("price")
                    if product_price is not None:
                        total_cost += quantity * product_price
                    else:
                        print(f"Error: Product ID {product_id} not found")
    return total_cost


def save_results_to_file(file_path, total_cost, elapsed_time):
    """Save results to a file."""
    with open(file_path, 'w', encoding="utf-8") as result_file:
        result_file.write(f"Total Cost of Sales: ${total_cost}\n")
        result_file.write(f"Elapsed Time: {elapsed_time:.4f} seconds")


def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: python compute_sales priceCatalogue salesRecord")
        sys.exit(1)

    price_catalog_file = sys.argv[1]
    sales_record_file = sys.argv[2]
    start_time = time.time()

    price_catalog = load_json(price_catalog_file)
    sales_record = load_json(sales_record_file)

    if price_catalog is not None and sales_record is not None:
        total_cost = compute_total_cost(price_catalog, sales_record)
        elapsed_time = time.time() - start_time
        save_results_to_file("SalesResults.txt", total_cost, elapsed_time)

        print(f"Total Cost of Sales: ${total_cost}")


if __name__ == "__main__":
    main()
    # End-of-file
