# Recipe Generator Using OpenAI API

## Overview
This Python script allows users to generate creative recipes using the OpenAI API (hosted on Azure). Users can input a list of ingredients, review them, and receive a custom recipe including the title, introduction, ingredients, and cooking steps.

## Features
- Accepts user-input ingredients
- Provides an option to edit the ingredients before processing
- Generates a detailed recipe using OpenAI's `gpt-4o-mini` model
- Includes a creative recipe title, introduction, ingredient list, and cooking instructions

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenAI Python package (`openai`)
- Environment variable setup for `GITHUB_TOKEN`

## Setup & Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/recipe-generator.git
   cd recipe-generator
   ```
2. Install dependencies:
   ```bash
   pip install openai
   ```
3. Set up the API token:
   - Replace `os.getenv("GITHUB_TOKEN")` with your actual GitHub token or set it as an environment variable:
     ```bash
     export GITHUB_TOKEN="your_api_key"
     ```
4. Run the script:
   ```bash
   python script.py
   ```

## Usage
1. The script will prompt you to enter a list of ingredients (comma-separated).
2. You will have the option to edit the ingredients before proceeding.
3. The script sends the request to OpenAI's API and returns a complete recipe.
4. The generated recipe is displayed in the console.

## Example Output
```
Enter ingredients (comma-separated): eggs, flour, milk, sugar
Do you want to edit ingredients? Yes or No
No

Recipe Title: Sweet Pancake Delight
Approximate Time: 20 minutes
Introduction: A delightful, fluffy pancake recipe perfect for breakfast or snacks.
Ingredients:
- 2 eggs
- 1 cup flour
- 1 cup milk
- 2 tbsp sugar
Cooking Steps:
1. Mix all ingredients in a bowl.
2. Heat a pan and pour batter to form pancakes.
3. Cook until golden brown on both sides.
4. Serve with syrup or toppings of choice.
```

## Error Handling
- If the API request fails, an error message will be displayed.
- If the AI does not return a valid recipe, a retry suggestion is given.


## Author
[Doaa] - GitHub: [deeishere]

