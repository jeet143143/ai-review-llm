from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def summarize_reviews(reviews):
    joined_reviews = "\n".join(reviews)
    
    prompt = PromptTemplate(
        input_variables=["reviews"],
        template="""
        Summarize the following customer reviews into a short, clear summary that highlights key feedback:
        {reviews}
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run({"reviews":joined_reviews})
    return summary