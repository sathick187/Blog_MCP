import chainlit as cl
from mcp_agent import main as agent_main
import asyncio

# ── Starter suggestions shown on empty chat ────────────────────────────────
STARTERS = [
    cl.Starter(
        label="📰 Latest articles",
        message="Show me the latest articles on Dev.to",
        icon="/public/icons/news.svg",
    ),
    cl.Starter(
        label="🔥 Top trending",
        message="Show me the top trending articles right now",
        icon="/public/icons/fire.svg",
    ),
    cl.Starter(
        label="🐍 Python articles",
        message="Find articles about Python",
        icon="/public/icons/tag.svg",
    ),
    cl.Starter(
        label="🤖 AI articles",
        message="Find articles about artificial intelligence and AI agents",
        icon="/public/icons/robot.svg",
    ),
    cl.Starter(
        label="✍️ Search articles",
        message="Search for articles about machine learning",
        icon="/public/icons/search.svg",
    ),
    cl.Starter(
        label="🌟 Write an article",
        message="Create a new article about the latest trends in agentic AI. Be creative, write at least one page covering 5-6 key innovations. Use tags: AI, agents",
        icon="/public/icons/write.svg",
    ),
]


@cl.set_starters
async def set_starters():
    return STARTERS


@cl.on_chat_start
async def on_start():
    await cl.Message(
        content=(
            "### 👋 Hey there! I'm your **Dev.to Assistant** ✨\n\n"
            "I can help you discover and explore amazing content on Dev.to:\n\n"
            "- 📰 Browse **latest** & **trending** articles\n"
            "- 🏷️ Find articles by **tag** — Python, JavaScript, AI, and more\n"
            "- 🔍 **Search** by any keywords\n"
            "- 👤 Explore articles by a specific **author**\n"
            "- ✍️ Even **create** brand-new articles!\n\n"
            "Pick a suggestion below or just type anything 🚀"
        ),
        author="Dev.to Assistant 🌸",
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    # Show a thinking indicator
    thinking = cl.Message(content="", author="Dev.to Assistant 🌸")
    await thinking.send()

    async with cl.Step(name="🔍 Talking to Dev.to MCP…", show_input=False) as step:
        try:
            # Run async agent from async Chainlit context
            response = await agent_main(message.content)
            step.output = "Done ✅"
        except Exception as e:
            import traceback
            step.output = f"Error: {e}"
            response = f"❌ Something went wrong:\n```\n{traceback.format_exc()}\n```"

    # Update the placeholder message with real content
    thinking.content = response or "🤔 No response received."
    await thinking.update()