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
   git clone https://github.com/deeishere/GenrateArecipe.git
   cd GenrateArecipe
   ```
2. Install dependencies:
   ```bash
   pip install openai or pip3 install openai
   ```
3. Set up the API token:
   - Replace `os.getenv("GITHUB_TOKEN")` with your actual GitHub token or set it as an environment variable:
     ```bash
     export GITHUB_TOKEN="your_api_key"
     ```
4. Run the script:
   ```bash
   python GenrateArecipe.py or python3 GenrateArecipe.py
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
**Recipe Title: Whimsical Eggy Pancakes**

**Introduction:**
Get ready for a fun and delicious cooking adventure! These Whimsical Eggy Pancakes are fluffy, sweet, and perfect for little hands to help with. With just a few simple ingredients—eggs, flour, milk, and sugar—this easy recipe will whip up a stack of delightful pancakes that will make breakfast or snack time extra special. Let’s put on our aprons and get cooking!

**Approximate Time:** 30 minutes 

**Ingredients:**
- 2 large eggs
- 1 cup all-purpose flour
- 1 cup milk
- 2 tablespoons sugar
- 1 teaspoon baking powder (optional for fluffiness)
- A pinch of salt
- Butter or oil (for cooking)

**Cooking Steps:**

1. **Mix the Dry Ingredients:** In a large mixing bowl, whisk together the flour, sugar, baking powder (if using), and salt until well combined.

2. **Whisk the Wet Ingredients:** In another bowl, crack the eggs and whisk them until frothy. Then, add the milk and mix until everything is blended smoothly.

3. **Combine the Mixtures:** Pour the egg and milk mixture into the bowl with the dry ingredients. Stir gently until just combined. Be careful not to overmix—some small lumps are okay! 

4. **Heat the Pan:** Place a non-stick skillet or griddle on medium heat and add a small amount of butter or oil to coat the surface.

5. **Cook the Pancakes:** Once the pan is hot, ladle about 1/4 cup of batter onto the skillet for each pancake. Let the pancakes cook for about 2-3 minutes, or until small bubbles form on the surface. 

6. **Flip and Finish:** Carefully flip the pancakes using a spatula and cook for another 1-2 minutes until golden brown on both sides. 

7. **Serve and Enjoy:** Stack your delicious pancakes on a plate. They can be enjoyed plain or with toppings like fresh fruit, syrup, or a sprinkle of powdered sugar. 

Get creative! You can even have fun adding chocolate chips or colorful sprinkles to the batter. Enjoy your Whimsical Eggy Pancakes!
```

## Error Handling
- If the API request fails, an error message will be displayed.
- If the AI does not return a valid recipe, a retry suggestion is given.


## Author
[Doaa] - GitHub: [deeishere]

