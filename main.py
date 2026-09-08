from anthropic.types import TextBlock
from dotenv import load_dotenv
from anthropic import Anthropic
from pydantic import BaseModel
import json

load_dotenv()

client = Anthropic()

class MacroNutrition(BaseModel):
    type: str
    percentage: float
    quantity: float
    quantity_type: str

class MicroNutrition(BaseModel):
    type: str
    percentage: float
    quantity: float
    message: str

class FoodAndCalories(BaseModel):
    food_item: str
    quantity: float
    calories: float

class Nutrients(BaseModel):
    message: str
    note: str
    total_calories: int
    food_items: list[FoodAndCalories]
    macro_nutrition: list[MacroNutrition]
    micro_nutrition: list[MicroNutrition]

def add_mesaage(messages: list, content: str, role: str):
    message = {
        "role": role,
        "content": content,
    }
    messages.append(message)


def find_nutrition(content: str):
    messages = []
    system_message = """
    You are a food macro and micro nutrition analyzer. you'll provide the following nutrition values based on the food, ingredients and its quantity
    
    Example Input:
    chick-fill-a spicy chicken sandwich deluxe, french fries - medium, chick fill a lemonade - large, chick-fill-a ice cream cup - half, chicken strips - 1, ranch - 1, chick-fill-a sauce - 1, grilled chicken nuggets - 1
    
    Example Format of Output:
    
    {
        "message": "Nutrition analysis for Chick-fil-A meal: Spicy Chicken Sandwich Deluxe, Medium French Fries, Large Lemonade, Half Ice Cream Cup, 1 Chicken Strip, 1 Ranch, 1 Chick-fil-A Sauce, and 1 Grilled Chicken Nuggets",
        "note": "Values are approximate based on standard Chick-fil-A menu items as of current nutritional data. Actual values may vary slightly by location and preparation. Sauces and condiments included in calculations.",
        "total_calories": 1847,
        "food_items": [
            {
                "food_item": "Spicy Chicken Sandwich Deluxe",
                "quantity": 1,
                "calories": 520
            },
            {
                "food_item": "French Fries - Medium",
                "quantity": 1,
                "calories": 365
            },
            {
                "food_item": "Lemonade - Large",
                "quantity": 1,
                "calories": 280
            },
            {
                "food_item": "Ice Cream Cup - Half",
                "quantity": 0.5,
                "calories": 150
            },
            {
                "food_item": "Chicken Strip",
                "quantity": 1,
                "calories": 120
            },
            {
                "food_item": "Ranch Sauce",
                "quantity": 1,
                "calories": 140
            },
            {
                "food_item": "Chick-fil-A Sauce",
                "quantity": 1,
                "calories": 140
            },
            {
                "food_item": "Grilled Chicken Nuggets",
                "quantity": 1,
                "calories": 132
            }
        ],
        "macro_nutrition": [
            {
                "type": "Protein",
                "percentage": 28,
                "quantity": 130,
                "quantity_type": "grams"
            },
            {
                "type": "Fat",
                "percentage": 38,
                "quantity": 78,
                "quantity_type": "grams"
            },
            {
                "type": "Carbohydrates",
                "percentage": 32,
                "quantity": 148,
                "quantity_type": "grams"
            },
            {
                "type": "Fiber",
                "percentage": 2,
                "quantity": 5,
                "quantity_type": "grams"
            }
        ],
        "micro_nutrition": [
            {
                "type": "Sodium",
                "percentage": 115,
                "quantity": 2760,
                "message": "Significantly high - consider limiting additional salt intake for the day"
            },
            {
                "type": "Saturated Fat",
                "percentage": 58,
                "quantity": 29,
                "message": "High saturated fat content - aim to balance with unsaturated fats"
            },
            {
                "type": "Vitamin C",
                "percentage": 22,
                "quantity": 13,
                "message": "Supports immune function and collagen production"
            },
            {
                "type": "Calcium",
                "percentage": 15,
                "quantity": 180,
                "message": "Important for bone health and muscle function"
            },
            {
                "type": "Iron",
                "percentage": 18,
                "quantity": 3.2,
                "message": "Essential for oxygen transport in blood"
            },
            {
                "type": "Potassium",
                "percentage": 12,
                "quantity": 580,
                "message": "Helps regulate blood pressure and heart function"
            }
        ]
    }
      
    """
    add_mesaage(messages, content, "user")
    nutrition = client.messages.parse(
        messages = messages,
        max_tokens=1024,
        model="claude-sonnet-5",
        system=system_message,
        output_format=Nutrients
    )
    return nutrition




if __name__ == "__main__":
    print("Hello - I am a nutrition analyzer and provides detailed macro, micro nutrition details baded on the food intake. \nSo please provide the food and its quantity to analyze. \nExample: Chicken 200g, French fries medium\n")
    content = input("Please provide the food and its quantity: ")
    print("Processing nutrition...")
    res = find_nutrition(content)
    print(res.content)
    for block in res.content:
        if isinstance(block, TextBlock):
            print(json.dumps(json.loads(block.text),indent=4))