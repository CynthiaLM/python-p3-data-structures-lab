spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
spicy_food = {
    "name": "Biryani",
    "cuisine": "Swahili",
    "heat_level": 4,
}

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        heat_emojis = "🌶" * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food 

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return round(average) 

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    
    return new_spicy_foods