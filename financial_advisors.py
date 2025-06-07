from dotenv import load_dotenv
import os
load_dotenv()

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat

# Financial Agent handles all finance-related queries using YFinance tools
financial_agent = Agent(
    name="Financial Analyst",                            # Optional identifier for the agent (used in team context)
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o-mini"),
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
        "Always create tables for comparisons."           # Ensures consistent tabular output for finance comparisons
    ]
)

# Web Researcher uses DuckDuckGo to answer general or current event questions from the web
web_researcher = Agent(
    name="Web Researcher",                                # Gives the agent a distinct role label
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],                                 # Enables internet search via DuckDuckGo
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include sources of the information that you gather."  # Forces inclusion of citations in output
    ]
)

# This composite agent coordinates between Financial Analyst and Web Researcher as a team
agents_team = Agent(
    team=[financial_agent, web_researcher],               # Allows routing of tasks to specific sub-agents based on skill
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include sources of the information that you gather.",  # Reinforces citation requirement at the team level
        "Always include sources of the information that you gather."   # Redundant on purpose, but can be deduped
    ],
    debug_mode=True                                       # Enables logging for how decisions are delegated within the team
)

# This query triggers both finance (analyst recommendations) and web search (latest news/info)
agents_team.print_response("Summarize the analyst recommendations and share the latest information about Google.")
