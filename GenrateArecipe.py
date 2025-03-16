import os
from openai import OpenAI


endpoint = "https://models.inference.ai.azure.com"
token = os.getenv("GITHUB_TOKEN")



# Pick one of the Azure OpenAI models from the GitHub Models service
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

while True:
    user_input = input("Enter ingredients (comma-separated): ") # to take the input
    ingredients = [item.strip() for item in user_input.split(',') if item.strip()] # to split it by the comma
    answer= input("Do you want to edit ingredients? Yes or No\n")#validation 
    if answer == "No":
        break



# Formulate the prompt
prompt_content = (
    "Please create a recipe for a children using the following ingredients: "
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
            {"role": "system", "content": "You are a  expert chef."}, # tells the system what his role
            {"role": "user", "content": prompt_content}, #tells the system what to promot by the user
        ],
        temperature=1.0,
        max_tokens=1000,  
        model=model_name,
    )


except Exception as e:
    print(f"An error occurred: {e}")


generated_text = response.choices[0].message.content.strip() 
if not generated_text:
    print("The AI did not return a valid recipe. Please try again.")
else:
    print(generated_text)




  