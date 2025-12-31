"""Tool 4: Conference Abstract Generator - Create compelling conference abstracts."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in academic writing and conference presentations."""

def run():
    console.print("[bold cyan]📋 Conference Abstract Generator[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["generate", "improve", "structure-guide"],
                     default="generate")
    
    if mode == "generate":
        console.print("\n[yellow]Describe your research:[/yellow]")
        research = get_multiline_input("Enter research (type 'END' when done):")
        
        word_limit = Prompt.ask("[green]Word limit[/green]", default="300")
        
        prompt = f"""Generate conference abstract:

Research: {research}
Limit: {word_limit} words

1. 📝 ABSTRACT
   [Structured abstract within limit]

2. 🎯 KEY ELEMENTS
   - Background
   - Objective
   - Methods
   - Results
   - Conclusions

3. 💡 TITLE OPTIONS
   - 3 compelling titles"""

    elif mode == "improve":
        console.print("\n[yellow]Paste your abstract:[/yellow]")
        abstract = get_multiline_input("Enter abstract (type 'END' when done):")
        
        prompt = f"""Improve abstract:

{abstract}

1. ✅ STRENGTHS
2. ⚠️ WEAKNESSES
3. ✨ IMPROVED VERSION
4. 📝 CHANGES MADE"""

    else:
        prompt = """Abstract structure guide:

1. 📚 BACKGROUND (1-2 sentences)
2. 🎯 OBJECTIVE (1 sentence)
3. 🔬 METHODS (2-3 sentences)
4. 📊 RESULTS (2-3 sentences)
5. 💡 CONCLUSIONS (1-2 sentences)

Plus: Tips for each section"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📋 Abstract", result, "cyan")

if __name__ == "__main__":
    run()
