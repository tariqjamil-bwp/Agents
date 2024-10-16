import os
from phi.assistant import Assistant
#from phi.llm.openai import OpenAIChat
from phi.llm.groq import Groq
from phi.tools.yfinance import YFinanceTools

assistant = Assistant(
    #llm=OpenAIChat(model="gpt-4o"),
    llm=Groq(api_key=os.environ.get("GROQ_API_KEY")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("What is the stock price of NVDA")
assistant.print_response("Write a comparison between NVDA and AMD, use all tools available.")