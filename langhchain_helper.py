from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.6)

def generate_attraction_in_capital(country):

    prompt_template_capital = PromptTemplate(
    input_variables=["country"],
    template="What is the capital of {country}? Just give me capital name"
    )

    capital_chain = LLMChain(llm=llm, prompt=prompt_template_capital, output_key="city")

    prompt_template_places = PromptTemplate(
        input_variables=["city"],
        template="What are the major attractions in this {city}? Write top 5 in comma seprated values"
    )
    places_chain = LLMChain(llm=llm, prompt=prompt_template_places, output_key="places")

    chain=SequentialChain(chains=[capital_chain, places_chain], input_variables=["country"], output_variables = ["city", "places"])

    response = chain({"country": country})

    return response