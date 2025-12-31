"""Tool 10: Experimental Bias Detective - Identify biases in research."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in research methodology and bias detection."""

def run():
    console.print("[bold cyan]🔍 Experimental Bias Detective[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["detect-bias", "bias-types", "mitigation"],
                     default="detect-bias")
    
    if mode == "detect-bias":
        console.print("\n[yellow]Describe your research design:[/yellow]")
        design = get_multiline_input("Enter design (type 'END' when done):")
        
        prompt = f"""Detect biases in research:

{design}

1. 🔍 BIASES IDENTIFIED
   For each bias:
   - Type
   - Where it occurs
   - Severity

2. 📊 BIAS CATEGORIES
   - Selection bias
   - Information bias
   - Confounding
   - Researcher bias

3. ⚠️ IMPACT ASSESSMENT
   - How each affects validity

4. 🔧 MITIGATION STRATEGIES
   - For each bias identified

5. ✅ REVISED APPROACH
   - Improved design"""

    elif mode == "bias-types":
        prompt = """Research bias types:

1. 👥 SELECTION BIAS
   - Types & examples
   - How to prevent

2. 📊 INFORMATION BIAS
   - Types & examples
   - How to prevent

3. 🔀 CONFOUNDING
   - Definition
   - Control strategies

4. 🧠 COGNITIVE BIAS
   - Researcher biases
   - Mitigation

5. 📝 PUBLICATION BIAS
   - What it is
   - Impact"""

    else:  # mitigation
        bias = Prompt.ask("[green]Bias to address[/green]")
        
        prompt = f"""Mitigate bias: {bias}

1. 📚 UNDERSTANDING THE BIAS
2. 🔧 PREVENTION STRATEGIES
3. 📊 DESIGN MODIFICATIONS
4. 📐 STATISTICAL CONTROLS
5. 📝 REPORTING TRANSPARENCY"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🔍 Bias Analysis", result, "yellow")

if __name__ == "__main__":
    run()
