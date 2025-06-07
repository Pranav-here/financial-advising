from dotenv import load_dotenv
import os
load_dotenv()

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app   # Importing the web UI for interactive testing

# Financial Analyst now uses OpenAI's GPT-4o-mini instead of Groq
financial_agent = Agent(
    name="Financial Analyst",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),                     # Switched to OpenAI model for flexibility or cost-saving
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        ),
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always create tables for comparisons."
    ]
)

# Web Researcher also uses OpenAI GPT-4o-mini
web_researcher = Agent(
    name="Web Researcher",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include sources of the information that you gather."
    ]
)

# Team agent wraps the two specialized agents and routes queries appropriately
agents_team = Agent(
    team=[financial_agent, web_researcher],
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include sources of the information that you gather.",  # Repeated for reinforcement
        "Always include sources of the information that you gather."
    ],
    debug_mode=True
)

# Create a Streamlit-like playground UI that allows testing both agents in browser
app = Playground(agents=[financial_agent, web_researcher]).get_app()

# Entry point for running the playground server
if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)     # Runs the playground with live reload enabled

# Use `phi euth` to start the environment, then run this script to launch the playground
