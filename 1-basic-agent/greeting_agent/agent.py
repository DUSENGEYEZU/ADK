from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from datetime import datetime
# my own custmmer tool
## geting current time
def get_current_time() -> dict:
    """Get the current time in format yyyy-mm-dd hh:mm:ss"""
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

root_agent = Agent(
    name="greeting_agent",
    # Local Ollama model via LiteLLM (no external API calls)
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    -get_current_time
    """,
    tools=[get_current_time],
)
