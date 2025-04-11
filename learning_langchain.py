from secret_key import openapi_key
import os
os.environ["OPENAI_API_KEY"] = openapi_key

from langchain_community.llms import OpenAI
llm = OpenAI(temperature = 0.6)
# restaurant_name = llm("I want to open a restaurant for Indian food. Suggest a fancy name for this.")

# Restaurant Name Chain and Prompt Below :

from langchain.prompts import PromptTemplate

restaurant_name_prompt_template = PromptTemplate(
    input_variables = ["cuisine"],
    template = "I want to open a restaurant for {cuisine} food.Suggest a fancy name for this."
)

# restaurant_name_prompt_template.format(cuisine = "Italian")

from langchain.chains import LLMChain

name_chain = LLMChain(llm = llm, prompt = restaurant_name_prompt_template, output_key="restaurant_name")

# Restaurant Menu Chain and Prompt Below :

restaurant_menu_prompt_template = PromptTemplate(
    input_variables = ["restaurant_name"],
    template = "Suggest some menu items for {restaurant_name}.Return it as a comma seperated list."
)

menu_chain = LLMChain(llm = llm, prompt = restaurant_menu_prompt_template, output_key="menu_items")

# Simple Sequential Chain to make use of Restaurant Name to generate menu items.

# from langchain.chains import SimpleSequentialChain

# chain = SimpleSequentialChain(chains = [name_chain, menu_chain])
# response = chain.run("Mughlai")

# print(response)

""" 
Fixing lost Restaurant Name by using Sequential Chains
"""

from langchain.chains import SequentialChain

chain = SequentialChain(
    chains = [name_chain, menu_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items']
    )

response : dict = chain({'cuisine':'Chinese'})
print(response["restaurant_name"], response["menu_items"])
chain = LLMChain(llm = llm, prompt = restaurant_name_prompt_template)
print(chain.run("Italian"))

