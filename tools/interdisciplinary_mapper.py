"""Tool 9: Interdisciplinary Connection Mapper - Map connections across fields."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in interdisciplinary research and knowledge integration."""

def run():
    console.print("[bold cyan]🔗 Interdisciplinary Connection Mapper[/bold cyan]\n")
    
    primary_field = Prompt.ask("[green]Your primary field[/green]")
    topic = Prompt.ask("[green]Research topic[/green]")
    
    prompt = f"""Map interdisciplinary connections:

Primary field: {primary_field}
Topic: {topic}

1. 🔗 CONNECTED DISCIPLINES
   - Related fields
   - Potential contributions from each

2. 📚 THEORETICAL BRIDGES
   - Shared concepts
   - Complementary theories

3. 🔬 METHODOLOGICAL CROSSOVERS
   - Methods from other fields
   - Novel combinations

4. 👥 COLLABORATION OPPORTUNITIES
   - Types of expertise needed
   - Potential partners

5. 💡 INNOVATION POTENTIAL
   - Unique insights from integration

6. ⚠️ CHALLENGES
   - Communication barriers
   - Paradigm differences"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🔗 Interdisciplinary Map", result, "magenta")

if __name__ == "__main__":
    run()
