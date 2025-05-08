# Osmosis-MCP-4B

## Prerequisites

*   Python 3.x
*   uvx
*   Access to a model server (e.g., running locally via vLLM/lm studio)
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
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**
    Create a `.env` file in the root of the project directory and add your API keys and model server configuration:
    ```env
    BRAVE_API_KEY="your_brave_api_key"
    GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ACCUWEATHER_API_KEY="your_accuweather_api_key"
    APP_STYLE="gui" # or "tui"
    ```
    if an api key is not provided, the tool will not be loaded.
    The `main.py` script currently configures the model server URL directly. Ensure `http://localhost:1234/v1` is the correct endpoint for your Qwen model server (this is what lm studio uses).

## Environment Variables

The application uses the following environment variables (loaded from a `.env` file):

*   `BRAVE_API_KEY`: Your API key for Brave Search.
*   `GOOGLE_MAPS_API_KEY`: Your API key for Google Maps.
*   `ACCUWEATHER_API_KEY`: Your API key for AccuWeather.
*   `APP_STYLE`: 'tui' or 'gui'
## Available Tools (MCP Servers)

The agent is configured to use the following tools via MCP:

*   **Time:** Provides current time information.
*   **Brave Search:** Enables web search capabilities.
    *   Requires: `BRAVE_API_KEY`
*   **Fetch:** Fetches content from URLs.
*   **Google Maps:** Provides location-based services.
    *   Requires: `GOOGLE_MAPS_API_KEY`
*   **Weather:** Provides weather forecasts.
    *   Requires: `ACCUWEATHER_API_KEY`
*   **Code Interpreter:** A built-in tool for executing Python code snippets.

These servers need to be running and accessible for the agent to utilize their respective functionalities. The `main.py` script provides the commands to start these MCP servers.

## How to Run Graphical User Interface (GUI):
    This mode launches a web-based interface for interacting with the agent. This is the default mode.
    ```bash
    python main.py
    ```

    The web UI will be accessible at the address provided by the `WebUI` component upon startup (on `http://localhost:7860`).

---
