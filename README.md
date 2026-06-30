# 🚀 Dev.to AI Agent using MCP & OpenAI Agents SDK

An intelligent Dev.to assistant powered by the OpenAI Agents SDK, Model Context Protocol (MCP), Chainlit, and OpenRouter LLMs.

This project demonstrates how AI Agents can dynamically discover and execute tools exposed through a custom MCP Server, enabling natural language interactions with Dev.to. Users can search articles, explore trending content, retrieve author-specific posts, and even generate and publish new blog articles—all through a conversational interface.

---

## 📖 Overview

The Dev.to AI Agent acts as an intelligent bridge between users and the Dev.to platform.

Instead of hardcoding API calls directly into the application, all Dev.to operations are exposed as MCP tools through a custom MCP Server. The AI Agent analyzes user intent, discovers available tools, selects the appropriate tool, executes it, and returns a summarized response.

### Example Use Cases

* Browse latest Dev.to articles
* Discover trending content
* Search articles by keyword
* Find articles by tag
* Explore articles by author
* Retrieve article details
* Generate and publish new blog posts

---

## ✨ Features

* 🤖 AI-powered Dev.to assistant
* 🔌 MCP-based tool architecture
* 📰 Browse latest Dev.to articles
* 🔥 Discover trending articles
* 🏷️ Search articles by tags
* 🔍 Keyword-based article search
* 👤 Find articles by author
* ✍️ AI-generated article creation
* ⚡ Fully asynchronous architecture
* 💬 Modern conversational UI with Chainlit
* 🧠 Intelligent tool selection using OpenAI Agents SDK
* 🚀 Easily extensible MCP tool ecosystem

---

## 🏗️ Architecture

```text
┌──────────────────────────┐
│      Chainlit UI         │
│       (app.py)           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   OpenAI Agents SDK      │
│     (mcp_agent.py)       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Dev.to AI Agent       │
│  Instruction Driven      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   MCP Server (STDIO)     │
│      (server.py)         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      MCP Tools           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Dev.to APIs         │
└──────────────────────────┘
```

---

## 🔄 End-to-End Flow

```text
User
 │
 ▼
Chainlit Chat Interface
 │
 ▼
OpenAI Agent SDK
 │
 ▼
Dev.to AI Agent
 │
 ▼
MCP Tool Discovery
 │
 ▼
Tool Selection
 │
 ▼
MCP Tool Execution
 │
 ▼
Dev.to API
 │
 ▼
Agent Summarization
 │
 ▼
Response Displayed in UI
```

---

## 💬 User Experience

The application uses Chainlit to provide a modern conversational interface.

### Starter Prompts

Users can quickly explore the agent using built-in starter suggestions:

* 📰 Latest Articles
* 🔥 Top Trending Articles
* 🐍 Python Articles
* 🤖 AI Articles
* 🔍 Search Articles
* ✍️ Generate New Article

These prompts help users immediately understand the capabilities of the agent.

---

## ⚙️ Agent Execution Lifecycle

Every request follows the same execution workflow:

```text
1. User sends a message

2. Chainlit receives the request

3. Thinking indicator is displayed

4. AI Agent is invoked

5. MCP Server starts

6. Agent discovers available tools

7. Agent selects the appropriate tool

8. MCP Tool executes

9. Dev.to API returns data

10. Agent summarizes results

11. Response is displayed to the user
```

---

## 🛠️ Technology Stack

| Technology                   | Purpose                              |
| ---------------------------- | ------------------------------------ |
| Python                       | Core programming language            |
| Chainlit                     | Conversational AI interface          |
| OpenAI Agents SDK            | Agent orchestration and tool calling |
| MCP (Model Context Protocol) | Tool discovery and execution         |
| OpenRouter                   | LLM provider                         |
| Qwen 3 235B                  | Foundation language model            |
| AsyncIO                      | Asynchronous execution               |
| MCPServerStdio               | MCP communication layer              |
| dotenv                       | Environment variable management      |

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── mcp_agent.py
├── server.py
├── .env
├── requirements.txt
└── README.md
```

---

# 📄 File Breakdown

## app.py

This file contains the Chainlit user interface and handles all user interactions.

### Responsibilities

* Displays the chat interface
* Registers starter prompts
* Receives user messages
* Displays agent progress
* Shows final responses

---

### set_starters()

Registers predefined starter prompts displayed on an empty chat screen.

#### Purpose

* Improve user onboarding
* Demonstrate available capabilities
* Provide quick actions

---

### on_chat_start()

Triggered whenever a new conversation begins.

#### Responsibilities

* Displays welcome message
* Introduces the assistant
* Explains supported actions

---

### on_message()

Main message processing function.

#### Responsibilities

* Receives user input
* Displays thinking indicator
* Invokes AI agent
* Displays final response

#### Flow

```text
User Message
      │
      ▼
on_message()
      │
      ▼
agent_main()
      │
      ▼
Agent Execution
      │
      ▼
Tool Execution
      │
      ▼
Response Returned
      │
      ▼
UI Updated
```

---

## mcp_agent.py

This file contains the AI Agent orchestration logic.

It acts as the bridge between:

* User Queries
* Language Model
* MCP Server
* MCP Tools

---

### setup_dev_agent()

Creates and configures the Dev.to Agent.

#### Responsibilities

* Defines agent instructions
* Connects MCP Server
* Attaches language model
* Configures tool usage behavior

The agent receives detailed instructions describing:

* Which tool should be used
* When it should be used
* How results should be formatted

This improves tool-calling reliability and response quality.

---

### main()

Primary execution entry point for all requests.

#### Responsibilities

* Starts MCP Server
* Creates agent instance
* Executes agent workflow
* Returns final output

#### Flow

```text
User Query
    │
    ▼
Start MCP Server
    │
    ▼
Create Agent
    │
    ▼
Run Agent
    │
    ▼
Tool Execution
    │
    ▼
Final Response
```

---

## server.py

This file contains the MCP Server implementation.

The server exposes Dev.to functionality as MCP-compatible tools that can be dynamically discovered and used by the AI Agent.

---

## 🔌 MCP Tools

The MCP Server exposes multiple tools to the agent.

### get_latest_articles()

Returns the latest articles from Dev.to.

---

### get_top_articles()

Returns trending or top-performing articles.

---

### get_articles_by_tag(tag)

Retrieves articles belonging to a specific tag.

#### Example

```text
Python
JavaScript
AI
MachineLearning
Agents
```

---

### search_articles(query)

Performs keyword-based article search.

#### Example

```text
LangChain
Agentic AI
OpenAI
MCP
```

---

### get_articles_by_username(username)

Returns articles published by a specific author.

---

### get_article_details(article_id)

Retrieves detailed information for a specific article.

---

### create_article()

Creates and publishes a new Dev.to article.

#### Parameters

```python
title
body_markdown
tags
published
```

---

## 🤖 Intelligent Tool Selection

The AI Agent uses instruction-based reasoning to select the correct MCP tool.

### Example 1

User:

```text
Show me the latest articles
```

Agent:

```text
Calls get_latest_articles()
```

---

### Example 2

User:

```text
Search for Agentic AI
```

Agent:

```text
Calls search_articles("Agentic AI")
```

---

### Example 3

User:

```text
Show articles by ThePracticalDev
```

Agent:

```text
Calls get_articles_by_username()
```

---

### Example 4

User:

```text
Create an article about MCP Servers
```

Agent:

```text
Generates content
      ↓
Calls create_article()
```

---

## 🔌 Why MCP?

This project intentionally uses Model Context Protocol (MCP) rather than directly integrating APIs into the agent.

### Benefits

* Standardized tool interface
* Dynamic tool discovery
* Decoupled architecture
* Easier maintenance
* Reusable integrations
* Future multi-agent compatibility
* Scalable tool ecosystem

New tools can be added to the MCP Server without changing the core agent implementation.

---

## 📸 Screenshots

### Home Screen

```md
Add screenshot here
```

### Agent Execution

```md
Add screenshot here
```

### Article Generation

```md
Add screenshot here
```

---

## 🚀 Example Queries

```text
Show me the latest Dev.to articles
```

```text
Show me the top trending articles
```

```text
Find articles about Python
```

```text
Find articles about AI agents
```

```text
Search for machine learning articles
```

```text
Show articles by ThePracticalDev
```

```text
Create a blog about the latest advancements in Agentic AI
```

---

## 🔮 Future Enhancements

* Multi-agent workflows
* Medium integration
* Hashnode integration
* Memory-enabled agents
* Blog review agent
* SEO optimization agent
* Research assistant agent
* Content planning agent
* Analytics dashboard
* Streaming responses
* Human approval workflows

---

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* OpenAI Agents SDK
* MCP (Model Context Protocol)
* Tool Calling Agents
* Agent Instructions Engineering
* Async Python Development
* OpenRouter Integration
* Chainlit Applications
* AI-Powered Content Automation
* Agentic AI Workflows

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/Dharshini195/Blog-MCP.git
cd Blog-MCP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

### Run the Application

```bash
chainlit run app.py
```

Open the provided local URL and start chatting with the Dev.to Assistant.

---

## 📜 License

This project is intended for educational, experimentation, and learning purposes. Feel free to fork, modify, and extend it for your own MCP and Agent Engineering projects.
