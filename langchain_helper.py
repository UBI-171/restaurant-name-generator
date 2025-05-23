from secret_key import openapi_key
import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


def generate_restaurant_name_and_menu(cuisine):
    os.environ["OPENAI_API_KEY"] = openapi_key
    llm = OpenAI(temperature = 0.6)
    restaurant_name_prompt_template = PromptTemplate(
    input_variables = ["cuisine"],
    template = "I want to open a restaurant for {cuisine} food.Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm = llm, prompt = restaurant_name_prompt_template, output_key="restaurant_name")

    restaurant_menu_prompt_template = PromptTemplate(
    input_variables = ["restaurant_name"],
    template = "Suggest some menu items for {restaurant_name}.Return it as a comma seperated list."
    )

    menu_chain = LLMChain(llm = llm, prompt = restaurant_menu_prompt_template, output_key="menu_items")

    chain = SequentialChain(
    chains = [name_chain, menu_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items']
    )

    response : dict = chain({'cuisine' : cuisine})

    return response

    