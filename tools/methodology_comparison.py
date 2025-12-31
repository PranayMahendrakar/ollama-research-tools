"""Tool 5: Methodology Comparison Tool - Compare research methodologies."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in research methodology across disciplines."""

def run():
    console.print("[bold cyan]🔄 Methodology Comparison Tool[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["compare", "select-method", "explain"],
                     default="compare")
    
    if mode == "compare":
        method1 = Prompt.ask("[green]First methodology[/green]")
        method2 = Prompt.ask("[green]Second methodology[/green]")
        
        prompt = f"""Compare methodologies:

{method1} vs {method2}

1. 📊 COMPARISON TABLE
   | Aspect | {method1} | {method2} |

2. ✅ STRENGTHS OF EACH
3. ⚠️ LIMITATIONS OF EACH
4. 🎯 BEST USE CASES
5. 💡 WHEN TO USE WHICH"""

    elif mode == "select-method":
        console.print("\n[yellow]Describe your research question:[/yellow]")
        question = get_multiline_input("Enter question (type 'END' when done):")
        
        prompt = f"""Select methodology for:

{question}

1. 🎯 RECOMMENDED APPROACHES
2. 📊 COMPARISON
3. 💡 RATIONALE
4. ⚠️ CONSIDERATIONS"""

    else:
        method = Prompt.ask("[green]Methodology to explain[/green]")
        prompt = f"""Explain methodology: {method}

1. 📚 DEFINITION
2. 🔧 KEY COMPONENTS
3. 📋 PROCEDURES
4. ✅ ADVANTAGES
5. ⚠️ LIMITATIONS
6. 💡 EXAMPLES"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🔄 Methodology", result, "magenta")

if __name__ == "__main__":
    run()
