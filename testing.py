from phi.agent import Agent
from phi.model.groq import Groq

test_agent = Agent(
    model=Groq(
        id='llama-3.3-70b-versatile'
    )
)

test_agent.print_response("What is your knowledge cutoff date?")