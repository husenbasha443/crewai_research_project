# Research Blog – CrewAI Project

This project is a **CrewAI-based agentic application** designed to research topics and generate structured blog-style outputs using multiple AI agents and tasks.

The repository follows a clean, production-friendly layout that separates configuration, tools, agents, and execution logic.

---

## 📂 Project Structure

```
research_blog/
│
├── .venv/                  # Python virtual environment (local)
├── knowledge/              # Knowledge base / reference documents for agents
│
├── src/
│   └── research_blog/
│       ├── config/
│       │   ├── agents.yaml # Agent definitions (roles, goals, LLM config)
│       │   └── tasks.yaml  # Task definitions and agent-task mapping
│       │
│       ├── tools/          # Custom tools used by agents
│       │   └── __init__.py
│       │
│       ├── crew.py         # CrewAI crew setup (agents + tasks)
│       ├── main.py         # Application entry point
│       └── __init__.py
│
├── tests/                  # Unit / integration tests
│
├── .env                    # Environment variables (API keys, configs)
├── .gitignore
├── demo.ipynb              # Jupyter notebook for experimentation
├── pyproject.toml          # Project metadata and tooling config
├── requirements.txt        # Python dependencies
├── uv.lock                 # Dependency lock file (uv)
└── README.md               # Project documentation
```

---

## 🚀 Features

* Multi-agent orchestration using **CrewAI**
* YAML-based configuration for agents and tasks
* Extensible tool system for agent capabilities
* Clean separation of logic and configuration
* Easy to switch LLM providers (Groq, OpenAI, Ollama, etc.)

---

## 🔧 Prerequisites

* Python **3.10+**
* Virtual environment tool (`venv` or `uv`)
* API key for your chosen LLM provider (e.g., Groq, OpenAI)

---

## 📦 Installation



### 2️⃣ Create and activate virtual environment

**Windows (PowerShell)**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

or if using **uv**:

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

> Only include the API key for the provider you are using.

---

## 🧠 Agents & Tasks Configuration

### `config/agents.yaml`

Defines:

* Agent role
* Goal
* Backstory
* LLM model
* Tools used by the agent

### `config/tasks.yaml`

Defines:

* Task description
* Expected output
* Assigned agent
* Execution order

This design allows **non-code changes** to agent behavior.

---

## ▶️ Running the Project

From the project root:

```bash
python -m src.research_blog.main
```

This will:

1. Load agents from `agents.yaml`
2. Load tasks from `tasks.yaml`
3. Create a Crew
4. Execute tasks sequentially or hierarchically

---

## 🛠 Custom Tools

Add custom tools inside:

```
src/research_blog/tools/
```

Each tool should:

* Be a Python function or class
* Follow CrewAI tool conventions
* Be imported and assigned to agents in `agents.yaml`

---

## 🧪 Testing

Run tests using:

```bash
pytest
```

---

## 📓 Jupyter Notebook

`demo.ipynb` can be used to:

* Experiment with agents
* Debug tasks
* Test prompts interactively

---

## 🔄 Extending the Project

You can easily:

* Add new agents in `agents.yaml`
* Add new tasks in `tasks.yaml`
* Plug in new LLMs (Groq, Ollama, OpenAI)
* Add RAG using the `knowledge/` directory

---

## 🧩 Common Use Cases

* Automated research blogging
* Content generation pipelines
* Agentic AI learning projects
* CrewAI production templates

---

## 📜 License

This project is for educational and experimental purposes.

---

## 🙌 Author

**Husen Basha**

If you are learning CrewAI or Agentic AI, this project is a solid foundation to build upon.

Happy building 🚀
