"""Tool 7: Grant Opportunity Matcher - Find relevant grants."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a grant writing and funding expert."""

def run():
    console.print("[bold cyan]💰 Grant Opportunity Matcher[/bold cyan]\n")
    
    console.print("[yellow]Describe your research project:[/yellow]")
    research = get_multiline_input("Enter description (type 'END' when done):")
    
    researcher_type = Prompt.ask("[green]Researcher type[/green]",
                                choices=["student", "early-career", "established"],
                                default="student")
    
    prompt = f"""Match grant opportunities:

Research: {research}
Researcher: {researcher_type}

1. 🎯 FUNDING TYPES
   - Federal grants
   - Private foundations
   - University grants
   - Industry funding

2. 💰 GRANT CATEGORIES
   - Research grants
   - Travel grants
   - Equipment grants
   - Fellowship opportunities

3. 📋 APPLICATION TIPS
   - Timeline planning
   - Key components

4. 💡 SEARCH STRATEGIES
   - Where to look
   - Keywords to use"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("💰 Grant Matching", result, "green")

if __name__ == "__main__":
    run()
