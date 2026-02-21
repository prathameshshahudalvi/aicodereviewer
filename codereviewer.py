import subprocess 
from langchain_groq import ChatGroq
from rule import RuleBook
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

model_name = "llama-3.3-70b-versatile"

class HTMLResponse(BaseModel):
    html: str = Field(description="Complete valid HTML document. Must start with <html> and end with </html>. No extra text.")

def main():
    load_dotenv()
    diff = subprocess.check_output(["git","show"], text=True)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(model_name = model_name, api_key=GROQ_API_KEY)
    response = llm.with_structured_output(HTMLResponse,method="json_schema").invoke(f"""Review the following code
    changes and provide feedback, according to these rules:{RuleBook.rule} \n\n Diff:{diff}""")
    print(response)

if __name__ == "__main__":
    main()
