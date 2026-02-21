import subprocess 
from langchain_groq import ChatGroq
from rule import RuleBook
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import smtplib
from email.message import EmailMessage

model_name = "llama-3.3-70b-versatile"
msg_from = "Sender@gmail.com"
msg_to = "Receiver@gmail.com"

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

    try:
        diff = subprocess.check_output(["git", "show"], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        send_mail(e.output)
        return
    
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(model_name=model_name,api_key=GROQ_API_KEY,timeout=60)

    try:
        structured_llm = llm.with_structured_output(HTMLResponse)
        response = structured_llm.invoke(f"""
        You are a senior software engineer.
        Review the following git diff according to these rules.
        Rules:
        {RuleBook.rule}

        Git Diff:
        {diff}

        Return ONLY valid HTML.""")
    except Exception as e:
        send_mail(e.output)
        return
    
    send_mail(response.html)

if __name__ == "__main__":
    main()
