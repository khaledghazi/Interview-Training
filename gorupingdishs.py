def groupingdishs(dishes: list):

    ingredient2dish = {}
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient not in ingredient2dish:
                ingredient2dish[ingredient] = []
            ingredient2dish[ingredient].append(dish[0])
    result = [[ingredient] + sorted(dishes) for ingredient, dishes in ingredient2dish.items() if len(dishes) > 1]
    return sorted(result)
   

print(groupingdishs([["Salad","Tomato","Cucumber","Salad","Sauce"],
                     ["Pizza","Tomato","Sausage","Sauce","Dough"],
                     ["Quesadilla","Chicken","Cheese","Sauce"],
                     ["Sandwich","Salad","Bread","Tomato","Cheese"]]))
                     