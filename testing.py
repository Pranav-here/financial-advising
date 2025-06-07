# Load environment variables from .env file
# This is where your GROQ_API_KEY should be stored
from dotenv import load_dotenv
import os
load_dotenv()

# Import required classes from phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

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
    model=Groq(
        id="llama-3.3-70b-versatile"
    ),
    
    # Attach financial tools powered by yfinance
    # These allow the agent to actually pull real stock info like price, fundamentals, and analyst opinions
    tools=[
        YFinanceTools(
            stock_price=True,                   # Enables current stock price access
            analyst_recommendations=True,       # Enables analyst buy/sell/hold data
            stock_fundamentals=True             # Enables P/E, EPS, market cap, etc.
        )
    ],

    show_tool_calls=True,   # Shows which tools are being used behind the scenes (you’ll see what it's fetching from yfinance)
    markdown=True,          # Formats response output using markdown (tables, bold, etc. where needed)
    
    # Add behavior instructions to guide how the model replies
    # In this case, it will always use tables when comparing stuff
    instructions=["Always create tables for comparisons"],
    
    debug_mode=True         # Full transparency mode — logs every action the agent takes (tool calls, reasoning, etc.)
)

# Ask the agent to compare Apple and Tesla based on analyst recommendations
# With the above setup, it should fetch data live using yfinance, then show a table comparing the two
test_agent.print_response("Summarize and compare the analyst recommendations for the stocks of Apple and Tesla?")
