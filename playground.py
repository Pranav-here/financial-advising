from dotenv import load_dotenv
import os
load_dotenv()

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app

financial_agent = Agent(
    name="Financial Analyst",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
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

agents_team = Agent(
    team=[financial_agent, web_researcher],
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources of the information that you gather.", "Always include sources of the information that you gather."],
    debug_mode=True
)

app = Playground(agents=[financial_agent, web_researcher]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)

# Use phi euth to start and then run this file