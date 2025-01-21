from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

#Web Search Agent
web_search_agent = Agent(
    name = 'web_search_agent',
    role = 'search the web for the information',
    model = Groq(id='llama-3.3-70b-versatile'),
    tools = [DuckDuckGo()],
    instructions= ["Always include sources"],
    show_tools_call = True,
    markdown = True
)

#Financial Agent

financial_agent = Agent(
    name = 'financial_agent',
    role = 'analyze financial data',
    model = Groq(id='llama-3.3-70b-versatile'),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions= ["Use table to display the data"],
    show_tools_call = True,
    markdown = True
)

multi_ai_agent = Agent(
    model = Groq(id='llama-3.3-70b-versatile'),
    team = [web_search_agent, financial_agent],
    instructions=['Always include sources', 'Use table to display the data'],
    show_tool_calls=True,
    markdown=True

)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)
