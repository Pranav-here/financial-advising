from dotenv import load_dotenv
import os
load_dotenv()

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat

test_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        ),
        get_company_symbol
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always create tables for comparisons."
    ],
    debug_mode=True
)

test_agent.print_response("Summarize and compare the analyst recommendations for the stocks of Pranav and Tesla")
