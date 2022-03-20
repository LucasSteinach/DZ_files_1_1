def recipes_dict(file_name: str, encoding: str):
	dict_recipes = {}

	with open(file_name, encoding=encoding) as file:
		data = file.readlines()
		data_copy = [[]]
		i = 0

		for one_line in data:
			data_copy[i] += [one_line[:-1]]
			if one_line == '\n':
				i += 1
				data_copy.append([])

		for dish in data_copy:
			key = dish[0]
			for i in range(2, int(dish[1]) + 2):
				ingredient_dict = {}
				ingredient_list = dish[i].split(' | ')
				ingredient_dict.update({'ingredient_name': ingredient_list[0], 'quantity': int(ingredient_list[1]),
										'measure': ingredient_list[2]})
				if dish[0] not in dict_recipes:
					dict_recipes.update({key: [ingredient_dict]})
				else:
					dict_recipes[key].append(ingredient_dict)

	return dict_recipes


def order(list_of_dishes: list, persons: int):
	if len(list_of_dishes) == len(set(list_of_dishes)):
		cook_book = recipes_dict('recipes.txt', 'utf-8')
		dict_ingredients = {}
		for dish in list_of_dishes:
			if dish not in cook_book:
				return f'There is no such dish ("{dish}") in cook book'
			else:
				for ingredient in cook_book[dish]:
					if ingredient['ingredient_name'] not in dict_ingredients:
						dict_ingredients.update({ingredient['ingredient_name']: {'measure': ingredient['measure'],
																				 'quantity': ingredient['quantity']
																				 }
												 }
												)
					else:
						dict_ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
		for ingredient in dict_ingredients.values():
			ingredient['quantity'] *= persons
		return dict_ingredients
	else:
		return 'В списке присутствуют дубликаты блюд'


print(recipes_dict('recipes.txt', 'utf-8'))
print("-----------")
print(order(['Омлет', 'Фахитос'], 2))
