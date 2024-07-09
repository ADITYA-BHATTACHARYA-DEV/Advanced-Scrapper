import json
import csv

# File paths
json_file_path = 'response.json'
csv_file_path = 'output.csv'

# Read the JSON data from the file
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# If data is a list, wrap it in a dictionary
if isinstance(data, list):
    data = {'tabs': data}

# Navigate to the product data
tabs = data.get('tabs', [])
products_list = []

# Extract product data from each tab
for tab in tabs:
    product_info = tab.get('product_info', {})
    products = product_info.get('products', [])
    for product in products:
        children = product.get('children', [])
        for child in children:
            products_list.append(child)

# Extract the fields you are interested in
fields = ['Title', 'Brand', 'Magnitude', 'Unit', 'Quantity', 'MRP', 'ean_code', 'TLC', 'MLC', 'LLC', 'Images']

# Open a CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()

    # Write the data rows
    for product in products_list:
        desc = product.get('desc', '')
        brand_name = product.get('brand', {}).get('name', '')
        magnitude = product.get('magnitude', '')
        quantity = product.get('w', '')
        unit = product.get('unit', '')
        title = f"{desc} {brand_name} [{magnitude}] {{{unit}}}"
        category = product.get('category', {})
        tlc_name = category.get('tlc_name', '')
        mlc_name = category.get('mlc_name', '')
        llc_name = category.get('llc_name', '')

        # Extract and join the image URLs from images > l
        images = ', '.join([image.get('l', '') for image in product.get('images', []) if 'l' in image])

        row = {
            'Title': title,
            'ean_code': str(product.get('ean_code', '')),
            'Magnitude': magnitude,
            'Quantity': quantity,
            'Brand': brand_name,
            'MRP': product.get('pricing', {}).get('discount', {}).get('mrp', ''),
            'Unit': unit,
            'TLC': tlc_name,
            'MLC': mlc_name,
            'LLC': llc_name,
            'Images': images
        }
        writer.writerow(row)

print(f"Data successfully written to {csv_file_path}")