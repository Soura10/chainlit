import os
#import python_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction

from dotenv import load_dotenv

load_dotenv()

#from google.colab import userdata
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

messages=[{"role": "system", "content": instruction}]

#def load_model():
def ask_bot(message):
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    response = llm.invoke(message)

    return response.content

if __name__=="__main__":
    print("Welcome to my chatbot")
    message = ask_bot("what is the meaning of large language models")
    print(message)
