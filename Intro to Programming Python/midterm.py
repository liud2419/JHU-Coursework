def print_meals(meal_plan):
    for meal in meal_plan.keys():
        print(f"{meal}: {meal_plan[meal]}")

meal_plan = {}

lunch = {"sandwich": 2, "chips": 1, "drink": 1}
dinner = {"ribs": 6, "mac_cheese": 1, "roll": 1, "pie": 1}

meal_plan["lunch"] = lunch
meal_plan["dinner"] = dinner

print_meals(meal_plan)