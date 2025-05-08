# Osmosis-MCP-4B

## Prerequisites

*   Python 3.x
*   Access to a Qwen model server (e.g., running locally via vLLM/SGLang)
*   API Keys for:
    *   Brave Search
    *   Google Maps
    *   AccuWeather

## Setup & Installation

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone https://github.com/Gulp-AI/Osmosis-MCP-4B-demo
    # cd Osmosis-MCP-4B-demo
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file would need to be created. Based on `main.py`, it should include at least `python-dotenv` and `qwen-agent`.)*

3.  **Set up Environment Variables:**
    Create a `.env` file in the root of the project directory and add your API keys and model server configuration:
    ```env
    BRAVE_API_KEY="your_brave_api_key"
    GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ACCUWEATHER_API_KEY="your_accuweather_api_key"

    # Optional: If your model server requires an API key
    # OPENAI_API_KEY="your_model_server_api_key"
    ```
    The `main.py` script currently configures the model server URL directly. Ensure `http://localhost:1234/v1` is the correct endpoint for your Qwen model server (this is what lm studio uses).

## Environment Variables

The application uses the following environment variables (loaded from a `.env` file):

*   `BRAVE_API_KEY`: Your API key for Brave Search.
*   `GOOGLE_MAPS_API_KEY`: Your API key for Google Maps.
*   `ACCUWEATHER_API_KEY`: Your API key for AccuWeather.

## Available Tools (MCP Servers)

The agent is configured to use the following tools via MCP:

*   **Time:** Provides current time information.
    *   Command: `uvx mcp-server-time --local-timezone=America/New_York`
*   **Brave Search:** Enables web search capabilities.
    *   Command: `npx -y @modelcontextprotocol/server-brave-search`
    *   Requires: `BRAVE_API_KEY`
*   **Fetch:** Fetches content from URLs.
    *   Command: `uvx mcp-server-fetch`
*   **Google Maps:** Provides location-based services.
    *   Command: `npx -y @modelcontextprotocol/server-google-maps`
    *   Requires: `GOOGLE_MAPS_API_KEY`
*   **Weather:** Provides weather forecasts.
    *   Command: `uvx --from git+https://github.com/adhikasp/mcp-weather.git mcp-weather`
    *   Requires: `ACCUWEATHER_API_KEY`
*   **Code Interpreter:** A built-in tool for executing Python code snippets.

These servers need to be running and accessible for the agent to utilize their respective functionalities. The `main.py` script provides the commands to start these MCP servers.

## How to Run

The `main.py` script provides three ways to run the agent:

1.  **Test Mode:**
    This mode runs a predefined query or a custom one if modified in the `test()` function.
    ```bash
    python main.py
    ```
    (You'll need to uncomment `test()` and comment out `app_tui()` and `app_gui()` in the `if __name__ == '__main__':` block of `main.py`)

2.  **Terminal User Interface (TUI):**
    This mode allows you to chat with the agent directly in your terminal.
    ```bash
    python main.py
    ```
    (You'll need to uncomment `app_tui()` and comment out `test()` and `app_gui()` in the `if __name__ == '__main__':` block of `main.py`)

3.  **Graphical User Interface (GUI):**
    This mode launches a web-based interface for interacting with the agent. This is the default mode.
    ```bash
    python main.py
    ```
    (Ensure `app_gui()` is the uncommented function in the `if __name__ == '__main__':` block of `main.py`)

    The web UI will be accessible at the address provided by the `WebUI` component upon startup (usually `http://localhost:7860` or similar).

---

This README provides a basic structure. You might want to add more details, such as:
*   Specific versions for dependencies in `requirements.txt`.
*   More detailed instructions for setting up the Qwen model server.
*   Troubleshooting tips.
*   Examples of interactions with the agent. 