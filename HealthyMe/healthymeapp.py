import pandas as pd
import itertools

file_path = "allfoodstest.csv"
data = pd.read_csv(file_path)

# Replace 'g' character and convert the amino acid columns to numeric
amino_acid_columns = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'valine']
data[amino_acid_columns] = data[amino_acid_columns].replace('g', '', regex=True).astype(float)

# Calculate ratios for each food item
rdi_values = {
    'histidine': 0.706,
    'isoleucine': 1.39,
    'leucine': 2.70,
    'lysine': 2.08,
    'methionine': 0.723,
    'phenylalanine': 0.870,
    'threonine': 1.04,
    'valine': 1.82
}

for amino_acid, rdi_value in rdi_values.items():
    column_name = f'{amino_acid}_ratio'
    data[column_name] = data[amino_acid] / rdi_value

def calculate_total_rdi(food_names):
    total_grams = {acid: 0.0 for acid in rdi_values.keys()}
    
    for food_name in food_names:
        food_row = data[data['name'] == food_name]
        food_grams = food_row[amino_acid_columns].values[0]
        
        for i, acid in enumerate(rdi_values.keys()):
            total_grams[acid] += food_grams[i]
    
    total_rdi = {acid: total_grams[acid] / rdi_values[acid] for acid in rdi_values.keys()}
    
    return total_rdi

def find_combination_with_rdi(food_name, num_additional_foods=1, min_rdi=0.8, max_rdi=1.5):
    input_food = data[data['name'] == food_name]
    other_foods = data[data['name'] != food_name]
    combinations = itertools.combinations(other_foods['name'], num_additional_foods)

    best_combination = None
    best_rdi = None

    for combo in combinations:
        food_combination = [food_name] + list(combo)
        total_rdi = calculate_total_rdi(food_combination)

        # Check if all RDIs are within the desired range
        if all(min_rdi <= rdi <= max_rdi for rdi in total_rdi.values()):
            if best_rdi is None or sum(total_rdi.values()) > sum(best_rdi.values()):
                best_rdi = total_rdi
                best_combination = combo

    if best_combination:
        food_combination = [food_name] + list(best_combination)
        total_rdi = calculate_total_rdi(food_combination)
        return total_rdi, best_combination
    else:
        return None, None

# Finding the food combos, in this example instead of an input which will be the final product i use "Nuts, pecan"
input_food_name = 'Nuts pecans'
result_rdi, food_combination = find_combination_with_rdi(input_food_name, num_additional_foods=3)

if result_rdi and food_combination:
    print(f"Combining '{input_food_name}' with {food_combination} gives you an optimal amino acid distribution.")
    
    print("\nTotal RDI for each amino acid in the combination:")
    for acid, rdi in result_rdi.items():
        print(f"{acid.capitalize()}: {rdi * 100:.2f}% RDI")
else:
    print("No combination found within the specified tolerance.")