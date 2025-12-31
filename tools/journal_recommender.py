"""Tool 3: Research Journal Recommender - Find suitable journals for publication."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an academic publishing expert helping researchers find suitable journals."""

def run():
    console.print("[bold cyan]📰 Research Journal Recommender[/bold cyan]\n")
    
    console.print("[yellow]Describe your research:[/yellow]")
    research = get_multiline_input("Enter description (type 'END' when done):")
    
    field = Prompt.ask("[green]Academic field[/green]")
    
    prompt = f"""Recommend journals for publication:

Research: {research}
Field: {field}

1. 🎯 TOP RECOMMENDATIONS
   For each journal:
   - Name and scope
   - Impact factor range
   - Acceptance rate
   - Time to publication
   - Fit with your research

2. 📊 JOURNAL TIERS
   - Top tier options
   - Mid tier options
   - Accessible options

3. 💡 SUBMISSION TIPS
   - Formatting requirements
   - Cover letter advice

4. ⚠️ JOURNALS TO AVOID
   - Predatory journal warning signs"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📰 Journal Recommendations", result, "yellow")

if __name__ == "__main__":
    run()
