# Osmosis-MCP-4B

## [Blog Post](https://osmosis.ai/blog/applying-rl-mcp)

## Prerequisites

*   Python 3.x
*   uvx
*   Access to a model server (e.g., running locally via vLLM/lm studio)
*   API Keys for:
    *   Brave Search
    *   Google Maps
    *   AccuWeather

## Setup & Installation

0. **Install LM studio [here](https://lmstudio.ai) and use it to run the model from a http endpoint**
   1. find and download model in discover    
   <img width="944" alt="image" src="https://github.com/user-attachments/assets/7a379cc3-fe3f-4e4c-bc0f-9f17f753c849" />
   2. select model to load and load an osmosis model
   <img width="430" alt="image" src="https://github.com/user-attachments/assets/3d32833d-dcae-4f91-bb3f-47dd23e0570c" />
   3. start the web server with model loaded
   <img width="1130" alt="image" src="https://github.com/user-attachments/assets/51d4fd79-75dc-4808-8dd7-3b9f8c43ff77" />


2.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/Gulp-AI/Osmosis-MCP-4B-demo
    cd Osmosis-MCP-4B-demo
    ```

3.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root of the project directory and add your API keys and model server configuration:
    ```env
    BRAVE_API_KEY="your_brave_api_key"
    GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ACCUWEATHER_API_KEY="your_accuweather_api_key"
    APP_STYLE="gui" # or "tui"
    ```
    if an api key is not provided, the tool will not be loaded.
    If `APP_STYLE` is omitted, the application defaults to GUI mode.
    The `main.py` script currently configures the model server URL directly. Ensure `http://localhost:1234/v1` is the correct endpoint for your Qwen model server (this is what lm studio uses).

5.  **Serve local model:**
    Use a tool like lm studio to provide a usable endpoint.

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
