# Import necessary libraries
from dataclasses import dataclass
import json


# Define user profile dataclass
@dataclass
class UserProfile:
    age: int
    gender: str
    weight: float
    height: float
    activity_level: str
    goal: str
    dietary_preference: str


def main_fun():
    user = UserProfile(
        age=0,
        gender="",
        weight=0,
        height=0,
        activity_level="",
        goal="",
        dietary_preference="",
    )


# Define function to calculate BMR (Basal Metabolic Rate)
def calculate_bmr(user: UserProfile) -> float:
    if user.gender == "male":
        bmr = (
            88.362 + (13.397 * user.weight) + (4.799 * user.height) - (5.677 * user.age)
        )
    else:
        bmr = (
            447.593 + (9.247 * user.weight) + (3.098 * user.height) - (4.330 * user.age)
        )
    return bmr


# Define function to calculate TDEE (Total Daily Energy Expenditure)
def calculate_tdee(user: UserProfile, bmr: float) -> float:
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9,
    }
    tdee = bmr * activity_multipliers[user.activity_level]
    return tdee


# Define function to adjust TDEE based on goal
def adjust_tdee_for_goal(user: UserProfile, tdee: float) -> float:
    if user.goal == "weight loss":
        return tdee - 500
    elif user.goal == "weight gain":
        return tdee + 500
    else:
        return tdee


# Define function to calculate macronutrient distribution
def calculate_macros(calories: float) -> dict:
    protein = calories * 0.25 / 4
    fat = calories * 0.30 / 9
    carbs = calories * 0.45 / 4
    return {"protein": protein, "fat": fat, "carbs": carbs}


# Define function to create a sample meal plan
def create_meal_plan(calories: float, macros: dict) -> dict:
    meal_plan = {
        "Breakfast": {
            "item": "Greek Yogurt Parfait with Berries and Honey",
            "calories": 300,
            "protein": 15,
            "fat": 8,
            "carbs": 40,
        },
        "Snack 1": {
            "item": "Apple with Almond Butter",
            "calories": 200,
            "protein": 4,
            "fat": 14,
            "carbs": 20,
        },
        "Lunch": {
            "item": "Quinoa Salad with Chickpeas, Cucumber, Tomato, and Feta",
            "calories": 450,
            "protein": 15,
            "fat": 18,
            "carbs": 55,
        },
        "Snack 2": {
            "item": "Carrot Sticks with Hummus",
            "calories": 150,
            "protein": 4,
            "fat": 8,
            "carbs": 16,
        },
        "Dinner": {
            "item": "Stir-fried Tofu with Broccoli and Brown Rice",
            "calories": 500,
            "protein": 20,
            "fat": 15,
            "carbs": 60,
        },
        "Snack 3": {
            "item": "Cottage Cheese with Pineapple",
            "calories": 200,
            "protein": 10,
            "fat": 5,
            "carbs": 25,
        },
    }
    return meal_plan


# Define function to create weekly and monthly meal plans
def create_extended_meal_plans(daily_plan: dict) -> dict:
    weekly_plan = {f"Day {i+1}": daily_plan for i in range(7)}
    monthly_plan = {f"Day {i+1}": daily_plan for i in range(30)}
    return {"weekly_plan": weekly_plan, "monthly_plan": monthly_plan}


# Define function to calculate calories burned
def calculate_calories_burned(user: UserProfile) -> float:
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9,
    }
    calories_burned = user.weight * activity_multipliers[user.activity_level] * 24
    return calories_burned


# Main function to generate personalized diet plan
def generate_diet_plan(user: UserProfile) -> dict:
    bmr = calculate_bmr(user)
    tdee = calculate_tdee(user, bmr)
    adjusted_calories = adjust_tdee_for_goal(user, tdee)
    macros = calculate_macros(adjusted_calories)
    daily_meal_plan = create_meal_plan(adjusted_calories, macros)
    extended_meal_plans = create_extended_meal_plans(daily_meal_plan)
    calories_burned = calculate_calories_burned(user)

    return {
        "user_profile": user,
        "calories": adjusted_calories,
        "macros": macros,
        "daily_meal_plan": daily_meal_plan,
        "weekly_meal_plan": extended_meal_plans["weekly_plan"],
        "monthly_meal_plan": extended_meal_plans["monthly_plan"],
        "calories_burned": calories_burned,
    }


# Example user profile
user = UserProfile(
    age=30,
    gender="female",
    weight=150,
    height=66,
    activity_level="moderate",
    goal="weight loss",
    dietary_preference="vegetarian",
)

# Generate diet plan
diet_plan = generate_diet_plan(user)

# Print the diet plan in a readable format
print(json.dumps(diet_plan, indent=4, default=str))
