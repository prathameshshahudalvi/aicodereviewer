import subprocess 
from langchain_groq import ChatGroq
from rule import RuleBook
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import smtplib
from email.message import EmailMessage

model_name = "llama-3.3-70b-versatile"
msg_from = "prathameshdalvi2017@gmail.com"
msg_to = "prathameshdalvi2017@gmail.com"

class HTMLResponse(BaseModel):
    html: str = Field(description="Complete valid HTML document. Must start with <html> and end with </html>. No extra text.")

def send_mail(html_content):
    msg = EmailMessage()
    msg['Subject'] = 'Code Review Feedback'
    msg['From'] = msg_from
    msg['To'] = msg_to
    msg.set_content("Please find the code review feedback below")
    msg.add_alternative(html_content, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(msg_from, os.getenv("MAIL_APP_PASSWORD"))
        smtp.send_message(msg)
    return "Email sent successfully"

def main():
    load_dotenv()
    diff = subprocess.check_output(["git","show"], text=True)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(model_name = model_name, api_key=GROQ_API_KEY)
    response = llm.with_structured_output(HTMLResponse).invoke(f"""Review the following code
    changes and provide feedback, according to these rules:{RuleBook.rule} \n\n Diff:{diff}""")
    send_mail(response.html)

if __name__ == "__main__":
    main()
