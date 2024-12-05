from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

information = """
Cao Cao courtesy name Mengde, was a Chinese statesman, warlord, and poet who rose to power during the end of the Han dynasty (c. 184–220), ultimately taking effective control of the Han central government. He laid the foundation for the state of Cao Wei (220–265), established by his son and successor Cao Pi, who ended the Eastern Han dynasty and inaugurated the Three Kingdoms period (220–280). Beginning in his own lifetime, a corpus of legends developed around Cao Cao which built upon his talent, his cruelty, and his perceived eccentricities.
"""


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    load_dotenv()

    summary_template = """

    given the information {information} about a person from I want you to create.:
    1. a short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

   # llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={
        "information": information
    })

    print(res)