"""Tool 6: Statistical Significance Explainer - Understand statistical significance."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert statistician explaining concepts clearly."""

def run():
    console.print("[bold cyan]📊 Statistical Significance Explainer[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["interpret-results", "explain-concept", "common-mistakes"],
                     default="interpret-results")
    
    if mode == "interpret-results":
        console.print("\n[yellow]Enter your statistical results:[/yellow]")
        results = get_multiline_input("Enter results (type 'END' when done):")
        
        prompt = f"""Interpret statistical results:

{results}

1. 📊 INTERPRETATION
   - What the numbers mean
   - Statistical significance
   - Practical significance

2. 🎯 EFFECT SIZE
   - Magnitude interpretation

3. ⚠️ LIMITATIONS
   - What NOT to conclude

4. 📝 REPORTING
   - How to report these results"""

    elif mode == "explain-concept":
        concept = Prompt.ask("[green]Statistical concept[/green]")
        
        prompt = f"""Explain: {concept}

1. 📚 PLAIN ENGLISH
2. 🔢 MATHEMATICAL
3. 📊 VISUAL INTUITION
4. 💡 EXAMPLES
5. ⚠️ COMMON MISUNDERSTANDINGS"""

    else:
        prompt = """Common statistical mistakes:

1. ❌ P-VALUE MISTAKES
2. ❌ CORRELATION VS CAUSATION
3. ❌ MULTIPLE COMPARISONS
4. ❌ SAMPLE SIZE ISSUES
5. ❌ EFFECT SIZE NEGLECT
6. ✅ HOW TO AVOID EACH"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📊 Statistical Explanation", result, "blue")

if __name__ == "__main__":
    run()
