from dotenv import load_dotenv
import os
load_dotenv()  # Force load environment variables from .env

from phi.agent import Agent
from phi.model.groq import Groq

test_agent = Agent(
    model=Groq(
        id="llama-3.3-70b-versatile"
    )
)

test_agent.print_response("What is your knowledge cutoff date?")