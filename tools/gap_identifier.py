"""Tool 1: Literature Gap Identifier - Find gaps in research literature."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert research methodology consultant specializing in literature review and gap analysis."""

def run():
    console.print("[bold cyan]📚 Literature Gap Identifier[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["analyze-gaps", "review-strategy", "gap-types", "research-questions"],
                     default="analyze-gaps")
    
    if mode == "analyze-gaps":
        field = Prompt.ask("[green]Research field/topic[/green]")
        
        console.print("\n[yellow]Describe what you know about the existing research:[/yellow]")
        existing = get_multiline_input("Enter summary (type 'END' when done):")
        
        prompt = f"""Identify literature gaps:

Field: {field}
Existing research: {existing}

1. 🔍 GAP ANALYSIS
   - Theoretical gaps
   - Methodological gaps
   - Empirical gaps
   - Population gaps
   - Geographic gaps

2. 📊 GAP SIGNIFICANCE
   - Why each gap matters
   - Potential impact

3. 🎯 RESEARCH OPPORTUNITIES
   - Promising directions
   - Feasibility assessment

4. ❓ RESEARCH QUESTIONS
   - Questions addressing gaps

5. 💡 CONTRIBUTION POTENTIAL
   - How filling gaps advances field"""

    elif mode == "review-strategy":
        topic = Prompt.ask("[green]Research topic[/green]")
        
        prompt = f"""Literature review strategy for: {topic}

1. 🔍 SEARCH STRATEGY
   - Databases to use
   - Search terms
   - Boolean operators

2. 📋 INCLUSION/EXCLUSION
   - Criteria to apply

3. 📊 ORGANIZATION
   - Themes to track
   - Data extraction

4. 🎯 GAP IDENTIFICATION
   - What to look for"""

    elif mode == "gap-types":
        prompt = """Types of literature gaps:

1. 📚 THEORETICAL GAPS
   - Definition
   - How to identify
   - Examples

2. 🔬 METHODOLOGICAL GAPS
   - Definition
   - How to identify
   - Examples

3. 📊 EMPIRICAL GAPS
   - Definition
   - How to identify
   - Examples

4. 👥 POPULATION GAPS
   - Definition
   - How to identify
   - Examples

5. 💡 FINDING GAPS
   - Practical strategies"""

    else:  # research-questions
        console.print("\n[yellow]Describe the gap you've identified:[/yellow]")
        gap = get_multiline_input("Enter gap (type 'END' when done):")
        
        prompt = f"""Generate research questions:

Gap: {gap}

1. ❓ PRIMARY RESEARCH QUESTIONS
2. ❓ SECONDARY QUESTIONS
3. 🎯 HYPOTHESES
4. 📊 VARIABLES
5. 🔬 METHODOLOGY SUGGESTIONS"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📚 Literature Gap Analysis", result, "blue")

if __name__ == "__main__":
    run()
