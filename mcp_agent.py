from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os
from agents.mcp import MCPServerStdio
from pathlib import Path

load_dotenv()

set_tracing_disabled(True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

UV_PATH = r"C:\Users\dhars\.local\bin\uv.exe"
CURRENT_DIRECTORY = str(Path(__file__).parent.absolute())

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    model="qwen/qwen3-235b-a22b-2507",
    openai_client=client
)

async def setup_dev_agent(mcp_server : MCPServerStdio):
    instructions = """You are a Dev.to assistant that helps users discover and explore content from Dev.to.

IMPORTANT GUIDELINES:
1. ALWAYS check available tools and resource before responding.
2. When retrieving article information, do not make repeated calls for the same data.
3. Focus on providing a clear, concise summary when presenting article information.
4. Limit your response to the top 3-5 most relevant results.
5. If it asks for a list of articles, in the response show it as a list of titles and authors.
5. When the task is complete, summarize the results and end your response.


FUNCTION SELECTION MAPPING:

IF the user wants latest articles:
- THEN use tool 'get_latest_articles with no parameters

IF the user wants trending or top articles:
- THEN use tool 'get_top_articles with no parameters

IF the user wants articles about a specific topic or tag:
- THEN use tool get articles_by_tag' with the tag name as parameter.

IF the user wants to search by keywords:
- THEN use tool 'search articles with query parameter

IF the user wants articles by a specific author:
-THEN use tool 'get articles_by_username with username parameter

IF the user wants details for a specific article:
- THEN use tool get_article_details' with article id parameter

IF the user wants to create a new article:
- THEN use tool 'create_article' with title, body_markdown, tags, published parameters

SPECIFIC QUERY HANDLING:
- For "Find the latest articles on Dev.to You MUST use tool 'get_latest_articles()'
- For "Show me top articles" You MUST use tool 'get_top_articles()
- For "Articles about javascript" You MUST use tool 'get_articles_by_tag("javascript")"
- For "Search for Python" You MUST use tool 'search_articles("Python")"
"""
    agent = Agent(
        name="Dev.to Blogging Agent",
        mcp_servers=[mcp_server],
        model=model,
        instructions=instructions,    
    )
    return agent

async def main(query : str):
    try:
        print("\n Starting MCP Server..") 
        custom_params = {
            "command": UV_PATH,
            "args" :[
                "--directory",
                CURRENT_DIRECTORY,
                "run",
                "server.py"
            ]

        }
        async with MCPServerStdio(
            cache_tools_list=False,
            params=custom_params
        ) as mcp_server:
            print("\n Initiating Server..")
            dev_agent = await setup_dev_agent(mcp_server)

            result = await Runner.run(
                starting_agent=dev_agent,
                input=query
            )
            return result.final_output
    
    except:
        import traceback
        print("\n Error in Agent : \n")
        print(traceback.format_exc())


# if __name__ == "__main__":
#     query = """Create an new article. Be creative in writing this blog. Topic should be about latest advancements in agentic ai world.
#     Write atleast a one pager blog containing 5-6 points covering most recent inovations in agentic ai. Choose a relevent title for this article.
#     Use tags as AI, agents"""
#     asyncio.run(main(query))
