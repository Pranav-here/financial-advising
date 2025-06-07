# Load environment variables from .env file
# This is where your GROQ_API_KEY and OPENAI_API_KEY should be stored
from dotenv import load_dotenv
import os
load_dotenv()

# Import required classes from phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat

# This is to show flexibility that we can also do this with our code
# This piece lets the model resolve informal or human terms to stock symbols
# Example: "Pranav" → "AAPL", so you can customize aliasing or internal logic
def get_company_symbol(company: str) -> str:
    """
    Use this function to get the symbol of a company
    Args:
        company(str): The name of the company
    Returns:
        str: The symbol for the company
    """
    symbols={
        "Pranav": "AAPL",     # maps 'Pranav' to Apple stock
        "Tesla": "TSLA",      # Tesla remains Tesla
        "Google": "GOOGL"     # Maps to Alphabet
    }
    return symbols.get(company, "Unknown")  # Fallback is "Unknown" (agent is told to abort if this happens)

# Set up the agent using Groq's LLaMA model
# We're using 'llama-3.3-70b-versatile' here, which is a strong general-purpose model: works well for reasoning, Q&A, and basic analysis.
# 
# Alternative Groq models you can try:
# - 'llama3-70b-8192'      → newer, faster, more optimized version of LLaMA 3 — better for real-time performance and updated support.
# - 'mixtral-8x7b-32768'   → mixture-of-experts model — faster and very cost-efficient for high-throughput apps.
# - 'gemma-7b-it'          → smaller instruction-tuned model — good for lightweight tasks or tighter latency limits.
# 
# Why we’re using 'llama-3.3-70b-versatile' for now:
# - It’s widely supported, stable, and known to handle reasoning + finance prompts well.
# - We're just starting to build this system, so stability + flexibility > raw performance for now.
test_agent = Agent(
    model=Groq(        id="llama-3.3-70b-versatile"    ),
    
    # Optionally switch to OpenAI GPT-4o-mini for comparison/testing
    # model=OpenAIChat(
    #     id="gpt-4o-mini"
    # ),

    # Attach financial tools powered by yfinance
    # These allow the agent to actually pull real stock info like price, fundamentals, and analyst opinions
    tools=[
        YFinanceTools(
            stock_price=True,                   # Enables current stock price access
            analyst_recommendations=True,       # Enables analyst buy/sell/hold data
            stock_fundamentals=True             # Enables P/E, EPS, market cap, etc.
        ),
        get_company_symbol                      # Adds our custom symbol resolver as a callable tool
    ],

    show_tool_calls=True,   # Logs each time a tool is used, helpful to see which functions were triggered
    markdown=True,          # Enables clean formatting like tables and bold text in answers

    # Custom behavior instructions for the model
    # It must always create tables for comparison-type answers
    # And must fetch stock symbols only via our get_company_symbol function — if it can't find the symbol, it should abort
    instructions=[
        "Always create tables for comparisons. Always get symbols from the get_company_symbol too and only use that symbol for further analysis, if the symbol does not exist abort"
    ],
    
    debug_mode=True         # Turns on full logging of how the agent thinks, makes decisions, and picks tools — very useful for dev/debug
)

# Ask the agent to compare Apple (Pranav) and Tesla based on analyst recommendations
# With our symbol-mapping tool, it should resolve "Pranav" to "AAPL", then run yfinance queries on AAPL and TSLA
test_agent.print_response("Summarize and compare the analyst recommendations for the stocks of Pranav and Tesla")
