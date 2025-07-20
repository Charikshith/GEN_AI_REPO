# AI Coding Workflow

This guide shows a clear, step-by-step way to work with AI coding tools to build real software.  
It uses an example—creating a Supabase MCP server in Python—but you can apply the same approach to any coding project.

---

## 1. Simple Rules to Follow

### 📄 Use Markdown for Project Files  
- Keep project info in these files: `README.md`, `PLANNING.md`, and `TASK.md`.

### 🪓 Keep Files Small  
- Don’t let any file grow too big (limit: 500 lines).  
- Split big files into smaller parts (modules) when needed.

### 🔄 Start Fresh Conversations  
- If chats get too long, start a new one to keep answers clear.

### ✅ One Task at a Time  
- Ask the AI to do only **one task per message**. This keeps things simple.

### 🧪 Test Early, Test Often  
- Write tests as you build.  
- Every new function should have unit tests.

### 🎯 Be Clear  
- Give detailed and clear instructions.  
- Share examples when asking the AI for help.

### 📝 Write Documentation as You Go  
- Don’t wait until the end to write comments or docs.

### 🔑 Protect Secrets  
- Manage environment variables yourself.  
- **Never** share API keys with the AI.

### 🚀 Focus on Quality  
- Don’t rush. Write clean, well-organized code.

---

## 1.1 Easy Rules to Follow (Key–Value)

| Rule                   | What to Do                                           |
|------------------------|------------------------------------------------------|
| **Project Files**      | Use `README.md`, `PLANNING.md`, and `TASK.md`.       |
| **File Size Limit**    | Keep files under 500 lines. Split into modules if needed. |
| **Conversations**      | Start a new chat if the current one gets too long.   |
| **Tasks**              | Do one task per AI message.                          |
| **Testing**            | Write tests early. Every function needs unit tests.  |
| **Clarity**            | Give clear, detailed instructions. Use examples.     |
| **Documentation**      | Write comments and docs as you go.                   |
| **Secrets / API Keys** | Manage secrets yourself. Never share API keys.       |
| **Code Quality**       | Don’t rush. Write clean, well-organized code.        |

---

## 2. Planning & Task Management (Made Simple)

Before you start writing any code, talk with the AI to plan what you’re building and break it into smaller tasks.  
We will use two files to manage this:

- **PLANNING.md**  
- **TASK.md**

The AI assistant should keep updating these files as the project moves forward.

---

### 📋 PLANNING.md — Project Planning

**Purpose:**  
Write down the overall idea for the project. Include big decisions like architecture, tools, tech stack, and any limits or rules to follow.

**What to include:**  
- High-level vision of the project (`## Overview`)  
- Architecture (how things fit together)  
- Any important rules or constraints  
- Tech stack (Python, FastAPI, Supabase, etc.)  
- Tools you plan to use  

```markdown
# azure-pm-agent — Project Planning

## Overview

## Architecture

## Rules & Constraints

## Tech Stack

## Tools

## Important Features (including priority feature)

## Next Steps
```

Tip for Using AI:  
At the start of every new conversation, tell the AI:  
 👉 “Use the structure and decisions outlined in PLANNING.md.”



### ✅ TASK.md — Task Tracking  

**Purpose:**  
Keep track of the tasks you’re working on.

List what’s done, what’s in progress, and what’s coming up.


**What to include:**   
- Bullet points of active tasks
- Any milestones
- New things you discover while working


Tip for Using AI:  
After finishing something, tell the AI:  
 👉 “Update TASK.md to mark XYZ as done and add ABC as a new task.”


Extra:  
You can ask the AI to update this file automatically as part of your process.




## 3. AI Coding Rules for IDEs  

These rules help you and your AI coding assistant follow a consistent, clean process.  
 There are global rules (for all projects) and project-specific rules (for one project).  

All AI IDEs support.  
1. [Github Copilot Rules](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot)
2. [Cursor Rules](https://docs.cursor.com/context/rules-for-ai) 
3. [Windsurf Rules](https://docs.codeium.com/windsurf/memories#windsurfrules)
4. [Cline Rules](https://docs.cline.bot/improving-your-prompting-skills/prompting)



---


### 🔄 Project Awareness & Context
- Always read `PLANNING.md` at the start of a conversation to understand the **architecture, goals, and style**.  
- Check `TASK.md` before starting work.  
If the task isn’t listed, **add it with today’s date and a short note**.  
- Follow the **naming, file structure, and architecture patterns** written in `PLANNING.md`.


---


### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines**. Split it into smaller modules if needed.  
- Organize your code by **feature or responsibility**.  
- Use clear, consistent **relative imports**.


---


### 🧪 Testing & Reliability
- Always write **unit tests** (using Pytest) for new functions, classes, or routes.  
- After changing any logic, update tests if needed.  
- Keep all tests in a `/tests` folder that **matches your main code structure**.  
- For each feature, write:  
  - 1 test for normal use  
  - 1 test for edge cases  
  - 1 test for failures


---


### ✅ Task Completion
- Mark finished tasks as **done in `TASK.md`** right after completing them.  
- Add any **new subtasks or TODOs** you discover during work under a section called **"Discovered During Work"**.


---


### 📎 Style & Conventions
- Use **Python** as the main language.  
- Follow **PEP8**, use **type hints**, and format code with **black**.  
- Use **pydantic** for data validation.  
- Use **FastAPI** for APIs and **SQLAlchemy** or **SQLModel** for ORM.  
- Write clear **docstrings** for every function in **Google style**:


```python
def example():
    """
    Short summary.


    Args:
        param1 (type): Description.


    Returns:
        type: Description.
    """
```


### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.  
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.  
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.


### 🧠 AI Behavior Rules
- **Never guess the context. Always ask questions.**  
- **Never hallucinate libraries or functions** – only use known, verified Python packages.  
- **Always confirm file paths and module names** before writing code or tests.  
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.