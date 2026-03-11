

def calculate_total_basket_cost(shopping_list):
  shopping_list_value = shopping_list.values()
  result = 0
  for value in shopping_list_value:
    result+=value
  return result

shopping_list = {"eggs": 1.85, "bread": 1.50, "peppers": 0.90}
print(calculate_total_basket_cost(shopping_list))