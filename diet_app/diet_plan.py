import random
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Example user profile
user_profile = {
    "age": 30,
    "gender": "female",
    "weight_kg": 65,
    "height_cm": 165,
    "goal": "weight_loss",
    "dietary_preferences": ["vegetarian"],
    "allergies": ["shellfish"],
}

# Example nutritional database (simplified)
nutritional_database = {
    "oatmeal": {"calories": 150, "protein_g": 5, "fat_g": 3, "carbs_g": 25},
    "fruits": {"calories": 50, "protein_g": 1, "fat_g": 0, "carbs_g": 12},
    "lentil_soup": {"calories": 250, "protein_g": 15, "fat_g": 5, "carbs_g": 30},
    "whole_grain_bread": {"calories": 100, "protein_g": 4, "fat_g": 2, "carbs_g": 18},
    "tofu": {"calories": 200, "protein_g": 20, "fat_g": 10, "carbs_g": 5},
    "vegetables": {"calories": 30, "protein_g": 2, "fat_g": 0, "carbs_g": 5},
    "greek_yogurt": {"calories": 120, "protein_g": 15, "fat_g": 2, "carbs_g": 10},
    "nuts": {"calories": 180, "protein_g": 5, "fat_g": 15, "carbs_g": 5},
}

# Synthetic training data for the decision tree (for illustration)
train_profiles = [
    {
        "age": 25,
        "gender": "male",
        "weight_kg": 70,
        "height_cm": 175,
        "goal": "muscle_gain",
        "dietary_preferences": ["omnivore"],
        "allergies": [],
    },
    {
        "age": 35,
        "gender": "female",
        "weight_kg": 60,
        "height_cm": 160,
        "goal": "weight_loss",
        "dietary_preferences": ["vegetarian"],
        "allergies": ["shellfish"],
    },
    {
        "age": 40,
        "gender": "male",
        "weight_kg": 85,
        "height_cm": 180,
        "goal": "weight_maintenance",
        "dietary_preferences": ["omnivore"],
        "allergies": ["nuts"],
    },
    {
        "age": 22,
        "gender": "female",
        "weight_kg": 55,
        "height_cm": 165,
        "goal": "weight_loss",
        "dietary_preferences": ["vegan"],
        "allergies": [],
    },
    {
        "age": 50,
        "gender": "male",
        "weight_kg": 90,
        "height_cm": 170,
        "goal": "weight_maintenance",
        "dietary_preferences": ["omnivore"],
        "allergies": ["gluten"],
    },
    {
        "age": 30,
        "gender": "female",
        "weight_kg": 68,
        "height_cm": 160,
        "goal": "muscle_gain",
        "dietary_preferences": ["vegetarian"],
        "allergies": [],
    },
    {
        "age": 28,
        "gender": "male",
        "weight_kg": 75,
        "height_cm": 180,
        "goal": "weight_loss",
        "dietary_preferences": ["omnivore"],
        "allergies": ["dairy"],
    },
    {
        "age": 32,
        "gender": "female",
        "weight_kg": 62,
        "height_cm": 168,
        "goal": "weight_maintenance",
        "dietary_preferences": ["vegetarian"],
        "allergies": ["peanuts"],
    },
    {
        "age": 45,
        "gender": "male",
        "weight_kg": 80,
        "height_cm": 178,
        "goal": "muscle_gain",
        "dietary_preferences": ["omnivore"],
        "allergies": [],
    },
    {
        "age": 29,
        "gender": "female",
        "weight_kg": 58,
        "height_cm": 162,
        "goal": "weight_loss",
        "dietary_preferences": ["vegan"],
        "allergies": ["nuts"],
    },
    {
        "age": 34,
        "gender": "male",
        "weight_kg": 72,
        "height_cm": 175,
        "goal": "weight_maintenance",
        "dietary_preferences": ["omnivore"],
        "allergies": ["gluten"],
    },
    {
        "age": 27,
        "gender": "female",
        "weight_kg": 65,
        "height_cm": 170,
        "goal": "muscle_gain",
        "dietary_preferences": ["vegetarian"],
        "allergies": [],
    },
    {
        "age": 36,
        "gender": "male",
        "weight_kg": 78,
        "height_cm": 180,
        "goal": "weight_loss",
        "dietary_preferences": ["omnivore"],
        "allergies": ["dairy"],
    },
    {
        "age": 42,
        "gender": "female",
        "weight_kg": 70,
        "height_cm": 165,
        "goal": "weight_maintenance",
        "dietary_preferences": ["vegan"],
        "allergies": ["peanuts"],
    },
    {
        "age": 38,
        "gender": "male",
        "weight_kg": 90,
        "height_cm": 182,
        "goal": "muscle_gain",
        "dietary_preferences": ["omnivore"],
        "allergies": [],
    },
    {
        "age": 31,
        "gender": "female",
        "weight_kg": 60,
        "height_cm": 168,
        "goal": "weight_loss",
        "dietary_preferences": ["vegetarian"],
        "allergies": ["shellfish"],
    },
    {
        "age": 39,
        "gender": "male",
        "weight_kg": 85,
        "height_cm": 175,
        "goal": "weight_maintenance",
        "dietary_preferences": ["omnivore"],
        "allergies": ["nuts"],
    },
    {
        "age": 26,
        "gender": "female",
        "weight_kg": 55,
        "height_cm": 160,
        "goal": "weight_loss",
        "dietary_preferences": ["vegan"],
        "allergies": [],
    },
]

# Corresponding meal choices for training data (for illustration)
train_meals = [
    ["oatmeal", "whole_grain_bread", "nuts"],
    ["fruits", "lentil_soup", "tofu"],
    ["vegetables", "greek_yogurt", "fruits"],
    ["vegetables", "lentil_soup", "fruits"],
    ["fruits", "oatmeal", "nuts"],
    ["greek_yogurt", "tofu", "whole_grain_bread"],
    ["lentil_soup", "vegetables", "nuts"],
    ["oatmeal", "tofu", "fruits"],
    ["greek_yogurt", "vegetables", "fruits"],
    ["fruits", "tofu", "whole_grain_bread"],
    ["oatmeal", "nuts", "greek_yogurt"],
    ["vegetables", "lentil_soup", "fruits"],
    ["whole_grain_bread", "tofu", "fruits"],
    ["fruits", "vegetables", "oatmeal"],
    ["greek_yogurt", "nuts", "whole_grain_bread"],
    ["lentil_soup", "fruits", "vegetables"],
    ["tofu", "oatmeal", "nuts"],
    ["fruits", "vegetables", "greek_yogurt"],
]


# Function to encode user profile
def encode_user_profile(profile):
    le_gender = LabelEncoder()
    le_goal = LabelEncoder()
    le_preferences = LabelEncoder()
    le_allergies = LabelEncoder()

    le_gender.fit(["male", "female"])
    le_goal.fit(["weight_loss", "muscle_gain", "weight_maintenance"])
    le_preferences.fit(["omnivore", "vegetarian", "vegan"])
    le_allergies.fit(["shellfish", "nuts", "gluten", "dairy", "peanuts"])

    encoded_profile = [
        profile["age"],
        le_gender.transform([profile["gender"]])[0],
        profile["weight_kg"],
        profile["height_cm"],
        le_goal.transform([profile["goal"]])[0],
        (
            le_preferences.transform(profile["dietary_preferences"])[0]
            if profile["dietary_preferences"]
            else 0
        ),
        le_allergies.transform(profile["allergies"])[0] if profile["allergies"] else 0,
    ]
    return np.array(encoded_profile)


# Encode training data
X_train = np.array([encode_user_profile(profile) for profile in train_profiles])
y_train = np.array(train_meals)

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)


# Function to generate a personalized meal plan using ML with randomness
def generate_meal_plan_ml(user_profile, nutritional_database, clf, days=7):
    encoded_profile = encode_user_profile(user_profile)
    meal_plan = {}

    for day in range(1, days + 1):
        meal_indices = clf.predict([encoded_profile]).flatten()  # Predict meals
        random.shuffle(meal_indices)  # Shuffle to introduce randomness
        meal_plan[f"Day {day}"] = meal_indices.tolist()

    return meal_plan


# Example NLP function to extract dietary preferences
def extract_dietary_preferences(text):
    tokens = word_tokenize(text.lower())
    dietary_preferences = []
    # Example: Detect vegetarian preferences
    if "vegetarian" in tokens or "vegan" in tokens:
        dietary_preferences.append("vegetarian")
    # Add more rules based on specific dietary preferences

    return dietary_preferences


# Example usage:
# Example user input for dietary preferences
user_input = "I prefer vegetarian meals with low carbs"
extracted_preferences = extract_dietary_preferences(user_input)
print("Extracted Dietary Preferences:", extracted_preferences)

# Generate a personalized weekly meal plan using ML
weekly_meal_plan_ml = generate_meal_plan_ml(
    user_profile, nutritional_database, clf, days=7
)
monthly_meal_plan_ml = generate_meal_plan_ml(
    user_profile, nutritional_database, clf, days=30
)

# Print the generated weekly meal plan
print("\nGenerated Weekly Meal Plan (ML):")
for day, meals in weekly_meal_plan_ml.items():
    print(f"{day}: {', '.join(meals)}")

    # Print the generated monthly meal plan
print("\nGenerated Monthly Meal Plan (ML):")
for day, meals in monthly_meal_plan_ml.items():
    print(f"{day}: {', '.join(meals)}")
