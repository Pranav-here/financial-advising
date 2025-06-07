from dotenv import load_dotenv
import os
load_dotenv()  # Force load environment variables from .env

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools


test_agent = Agent(
    model=Groq(
        id="llama-3.3-70b-versatile"
    ),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations = True,
        stock_fundamentals=True
    )],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always create tables for comparisions"],
    debug_mode=True
)

test_agent.print_response("Summarize and compare the analyst recommendations for the stocks of Apple and Tesla?")