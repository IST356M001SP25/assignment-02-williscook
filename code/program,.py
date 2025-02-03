'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code
def parse_packaging(packaging_data: str) -> list[dict]:
    package = []
    for data in packaging_data.split('/'):
        item = data.split(" in ")[0]
        quantity = int(item.split()[0])
        item = item.split()[1].strip()
        package.append({item: quantity})
    
    # get the last one
    item = data.split(" in ")[-1]
    quantity = int(item.split()[0])
    item = item.split()[1].strip()
    package.append({item: quantity})

    return package

def calc_total_units(package: list[dict]) -> int:
    total = 1
    for item in package:
        for key, value in item.items():
         total += value
    return total

def get_unit(package: list[dict]) -> str:
        return list(package[0].keys())[0]

if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")


