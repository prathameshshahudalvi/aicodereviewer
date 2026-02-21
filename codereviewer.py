import subprocess 
from langchain_groq import ChatGroq
from rule import RuleBook
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

model_name = "llama-3.3-70b-versatile"

class HTMLResponse(BaseModel):
    html: str = Field(description="Valid HTML content")

def main():
    load_dotenv()
    diff = subprocess.check_output(["git","show"], text=True)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(model_name = model_name)
    response = llm.with_structured_output(HTMLResponse).invoke(f"""
    Summarize the following diff according to these rules:{RuleBook.rule}
    Diff:{diff}""")
    print(response)

if __name__ == "__main__":
    main()
