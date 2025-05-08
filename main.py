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

def init_agent_service():
    llm_cfg = {
        # Use your own model service compatible with OpenAI API by vLLM/SGLang:
        'model': 'Qwen/Qwen3-4B',
        'model_server': 'http://localhost:1234/v1',  # api_base
        # 'api_key': 'EMPTY',
    
        'generate_cfg': {},
    }
    tools = [
        {
            'mcpServers': {  # You can specify the MCP configuration file
                'time': {
                    'command': 'uvx',
                    'args': ['mcp-server-time', '--local-timezone=America/New_York']
                },
                "brave-search": {
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-brave-search"
                    ],
                    "env": {
                        "BRAVE_API_KEY": BRAVE_API_KEY
                    }
                },
                'fetch': {
                    'command': 'uvx',
                    'args': ['mcp-server-fetch']
                },
                "google-maps": {
                    "command": "npx",
                    "args": ["-y", "@modelcontextprotocol/server-google-maps"],
                    "env": {
                        "GOOGLE_MAPS_API_KEY": GOOGLE_MAPS_API_KEY
                    }
                },
                "weather": {
                    "command": "uvx",
                    "args": ["--from", "git+https://github.com/adhikasp/mcp-weather.git", "mcp-weather"],
                    "env": {
                        "ACCUWEATHER_API_KEY": ACCUWEATHER_API_KEY
                    }
                }
            }
        },
        'code_interpreter',  # Built-in tools
    ]
    bot = Assistant(llm=llm_cfg,
                    function_list=tools,
                    name='Osmosis-MCP-4B demo',
                    description="An Open Source SLM Trained for MCP")

    return bot


def test(query: str = 'I usually bike to work from Bushwick to Times Square at 7am. What\'s the best way to get there given tomorrow\'s weather and traffic?'):
    # Define the agent
    bot = init_agent_service()

    # Chat
    messages = [{'role': 'user', 'content': query}]
    response_plain_text = ''
    for response in bot.run(messages=messages):
        response_plain_text = typewriter_print(response, response_plain_text)


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
            'I usually bike to work from Bushwick to Times Square at 7am. What\'s the best way to get there given tomorrow\'s weather and traffic?',
            'https://github.com/orgs/QwenLM/repositories Extract markdown content of this page, then draw a bar chart to display the number of stars.',
        ],
        # base64 "O" logo
        'agent.avatar': "https://avatars.githubusercontent.com/u/190666434?s=48&v=4",
        'agent.name': 'Osmosis-MCP-4B demo',
        'agent.description': "An Open Source SLM Trained for MCP",
        'user.avatar': "https://avatars.githubusercontent.com/u/190666434?s=48&v=4",
        'user.name': 'User',
        'language': 'en',
    }
    WebUI(
        bot,
        chatbot_config=chatbot_config,
    ).run()


if __name__ == '__main__':
    app_gui()