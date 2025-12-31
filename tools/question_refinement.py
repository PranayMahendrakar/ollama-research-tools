"""Tool 8: Research Question Refinement Tool - Refine research questions."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a research methodology expert specializing in question development."""

def run():
    console.print("[bold cyan]❓ Research Question Refinement Tool[/bold cyan]\n")
    
    console.print("[yellow]Enter your initial research question or topic:[/yellow]")
    question = get_multiline_input("Enter question (type 'END' when done):")
    
    research_type = Prompt.ask("[green]Research type[/green]",
                              choices=["qualitative", "quantitative", "mixed"],
                              default="quantitative")
    
    prompt = f"""Refine research question:

Initial: {question}
Type: {research_type}

1. 🔍 QUESTION ANALYSIS
   - Current strengths
   - Current weaknesses

2. ✨ REFINED VERSIONS
   - Option 1 (more focused)
   - Option 2 (broader scope)
   - Option 3 (different angle)

3. 📊 FINER CRITERIA CHECK
   - Feasible
   - Interesting
   - Novel
   - Ethical
   - Relevant

4. 🎯 SUB-QUESTIONS
   - Supporting questions

5. 📐 VARIABLES
   - Independent
   - Dependent
   - Control"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("❓ Refined Questions", result, "cyan")

if __name__ == "__main__":
    run()
