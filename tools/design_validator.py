"""Tool 2: Experiment Design Validator - Validate research experiment designs."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in research methodology and experimental design."""

def run():
    console.print("[bold cyan]🔬 Experiment Design Validator[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["validate-design", "suggest-improvements", "check-validity", "power-analysis"],
                     default="validate-design")
    
    if mode == "validate-design":
        console.print("\n[yellow]Describe your experiment design:[/yellow]")
        design = get_multiline_input("Enter design (type 'END' when done):")
        
        prompt = f"""Validate experiment design:

{design}

1. ✅ STRENGTHS
   - Well-designed elements

2. ⚠️ WEAKNESSES
   - Design flaws
   - Threats to validity

3. 🔧 RECOMMENDATIONS
   - Specific improvements

4. 📊 VALIDITY CHECK
   - Internal validity
   - External validity
   - Construct validity

5. 📋 REVISED DESIGN
   - Improved version"""

    elif mode == "suggest-improvements":
        design_type = Prompt.ask("[green]Design type[/green]",
                                choices=["experimental", "quasi-experimental", "observational", "survey"],
                                default="experimental")
        
        console.print("\n[yellow]Describe your study:[/yellow]")
        study = get_multiline_input("Enter description (type 'END' when done):")
        
        prompt = f"""Improve {design_type} design:

Study: {study}

1. 🔧 DESIGN IMPROVEMENTS
2. 📊 CONTROL ADDITIONS
3. 📏 MEASUREMENT REFINEMENTS
4. 👥 SAMPLING IMPROVEMENTS"""

    elif mode == "check-validity":
        console.print("\n[yellow]Describe your study design:[/yellow]")
        design = get_multiline_input("Enter design (type 'END' when done):")
        
        prompt = f"""Check validity threats:

{design}

1. 🎯 INTERNAL VALIDITY
   - History
   - Maturation
   - Testing
   - Instrumentation
   - Selection
   - Mortality

2. 🌍 EXTERNAL VALIDITY
   - Population
   - Setting
   - Time

3. 📐 CONSTRUCT VALIDITY
   - Mono-operation bias
   - Mono-method bias

4. 🔧 MITIGATION STRATEGIES"""

    else:  # power-analysis
        prompt = """Power analysis guidance:

1. 📊 WHAT IS POWER
2. 🔢 KEY PARAMETERS
   - Effect size
   - Alpha level
   - Sample size
3. 📐 CALCULATION METHODS
4. 💡 INTERPRETATION"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🔬 Design Validation", result, "green")

if __name__ == "__main__":
    run()
