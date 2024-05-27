from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import os
import dotenv
dotenv.load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY,
                             model="gemini-1.5-pro", temperature=0.6)

prompt_template_name = PromptTemplate(
    input_variables=["country"],
  template="""I want to open a restaurant for {country} food, suggest me a fancy name for the restaurant. Your output should be a single line containing  the name of the restaurant in bold.""",
)

name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

prompt_template_menu = PromptTemplate(
    input_variables=["restaurant_name"],
  template="""suggest me menu items for the restaurant {restaurant_name}. Your output should be a comma seprated list.""",
)

menu_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="menu_items")

sequential_chain = SequentialChain(
    chains=[name_chain, menu_chain],
    input_variables=["country"],
    output_variables=["restaurant_name", "menu_items"],
)

def generate_restaurant(country):
    res = sequential_chain({'country': f"{country}"})

    return f"{res['restaurant_name']}", "\n".join(["- " + item for item in list(res["menu_items"].strip().split(','))])