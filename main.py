"""An agent implemented by assistant with qwen3"""
import os  # noqa
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI
from qwen_agent.utils.output_beautify import typewriter_print

BRAVE_API_KEY = os.getenv('BRAVE_API_KEY')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
ACCUWEATHER_API_KEY = os.getenv('ACCUWEATHER_API_KEY')
MODEL_SERVER_URL = os.getenv('MODEL_SERVER_URL')
MODEL_SERVER_API_KEY = os.getenv('MODEL_SERVER_API_KEY')
APP_STYLE = os.getenv('APP_STYLE') # 'tui' or 'gui'

def init_agent_service():
    llm_cfg = {
        # Use your own model service compatible with OpenAI API by vLLM/SGLang:
        'model': 'osmosis-ai/osmosis-mcp-4b',
        'model_server': MODEL_SERVER_URL,  # api_base
        'api_key': MODEL_SERVER_API_KEY,
    
        'generate_cfg': {},
    }

    mcp_servers_config = {
        'time': {
            'command': 'uvx',
            'args': ['mcp-server-time', '--local-timezone=America/New_York']
        },
        'fetch': {
            'command': 'uvx',
            'args': ['mcp-server-fetch']
        }
    }

    if BRAVE_API_KEY:
        print("BRAVE_API_KEY found")
        mcp_servers_config["brave-search"] = {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-brave-search"
            ],
            "env": {
                "BRAVE_API_KEY": BRAVE_API_KEY
            }
        }

    if GOOGLE_MAPS_API_KEY:
        print("GOOGLE_MAPS_API_KEY found")
        mcp_servers_config["google-maps"] = {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-google-maps"],
            "env": {
                "GOOGLE_MAPS_API_KEY": GOOGLE_MAPS_API_KEY
            }
        }

    if ACCUWEATHER_API_KEY:
        print("ACCUWEATHER_API_KEY found")
        mcp_servers_config["weather"] = {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/adhikasp/mcp-weather.git", "mcp-weather"],
            "env": {
                "ACCUWEATHER_API_KEY": ACCUWEATHER_API_KEY
            }
        }

    tools = [
        {
            'mcpServers': mcp_servers_config
        },
        'code_interpreter',  # Built-in tools
    ]
    bot = Assistant(llm=llm_cfg,
                    function_list=tools,
                    name='Osmosis-MCP-4B',
                    description="An Open Source SLM Trained for MCP")

    return bot

def app_tui():
    # Define the agent
    bot = init_agent_service()

    # Chat
    messages = []
    while True:
        query = input('user question: ')
        messages.append({'role': 'user', 'content': query})
        response = []
        response_plain_text = ''
        for response in bot.run(messages=messages):
            response_plain_text = typewriter_print(response, response_plain_text)
        messages.extend(response)


def app_gui():
    # Define the agent
    bot = init_agent_service()

    chatbot_config = {
        'prompt.suggestions': [
            'What is the weather in New York City tomorrow? Use the weather tool or brave search to get the forecast.',
            'I usually bike to work from Bushwick to Times Square at 7am. What\'s the best way to get there given tomorrow\'s weather and traffic?',
            'https://github.com/orgs/QwenLM/repositories Extract markdown content of this page, then provide a list of the top 5 repositories with stars, forks, and issues.',
            'I am allergic to peanuts. What are peanut-free restaurants near me in Roxbury, MA?',
            'I\'m planning a day trip from my current location, along market street in San Francisco. Find me 3 interesting destinations within a 1-hour drive, check their weather forecasts for tomorrow, recommend the best option based on weather and top-rated attractions, then create an optimized itinerary with driving directions a forecast at the top of the itinerary.',
        ],
        'agent.avatar': "https://avatars.githubusercontent.com/u/190666434?s=48&v=4",
        'agent.name': 'Agent',
        'agent.description': "An Open Source SLM Trained for MCP",
        'user.avatar': "https://avatars.githubusercontent.com/u/190666434?s=48&v=4",
        'verbose': True,
        'input.placeholder': 'Ask me anything...',
    }
    WebUI(
        bot,
        chatbot_config=chatbot_config,
    ).run()


if __name__ == '__main__':
    if APP_STYLE == 'gui':
        app_gui()
    else:
        app_tui()
