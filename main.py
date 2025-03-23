import os
from dotenv import load_dotenv
from agents import Agent, Runner , AsyncOpenAI , OpenAIChatCompletionsModel
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)
model= OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

agent = Agent(
   name = "Greeting Agent",
   instructions= "You are a Greeting Agent. Your task is to greet users with a friendly message. - If a user says hi or any similar greeting, respond with Salam! Hope you're having a great day!  - If a user says bye or any farewell phrase, respond with Allah Hafiz! Take care!  - If a user asks anything other than a greeting, politely inform them that you are only designed for greetings and cannot answer other queries.  Your responses should always be warm and welcoming.",
   model=model
)

user_question = input("Please enter your question:").strip().lower()

result = Runner.run_sync(agent, user_question)
print(result.final_output)