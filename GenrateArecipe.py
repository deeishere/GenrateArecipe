

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
# Pick one of the Azure OpenAI models from the GitHub Models service
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

while True:
    user_input = input("Enter ingredients (comma-separated): ")
    ingredients = [item.strip() for item in user_input.split(',') if item.strip()]
    answer = input("Do you want to edit ingredients? Yes or No\n")
    if answer.lower() == "no":
        break

# Formulate the prompt
prompt_content = (
    "Please create a recipe using the following ingredients: "
    f"{', '.join(ingredients)}. "
    "The approximate time to do it 'Approximate Time:'"
    "Include a creative name with 'Recipe Title:', "
    "an introduction with 'Introduction:', "
    "ingredients with 'Ingredients:', and "
    "cooking steps with 'Cooking Steps:'."
)

# Make API request
try:
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert chef."},
            {"role": "user", "content": prompt_content},
        ],
        temperature=1.0,
        max_tokens=1000,
        model=model_name,
    )
except Exception as e:
    print(f"An error occurred: {e}")

print(response.choices[0].message.content)
    
generated_text = response.choices[0].message.content.strip()


