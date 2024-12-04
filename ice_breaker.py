from dotenv import load_dotenv
import os

from langchain.chains.qa_with_sources.stuff_prompt import template
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate


def get_summary_content(information):
    return  f"""
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    load_dotenv()
    summary_template = get_summary_content("a person")
    summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4-mini")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={
        "information": "a person"
    })
