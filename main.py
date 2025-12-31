#!/usr/bin/env python3
"""Ollama Research & Analysis Tools - 10 AI-Powered Research Assistants"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt

console = Console()

TOOLS = {
    1: ("Literature Gap Identifier", "tools.gap_identifier", "Find gaps in research"),
    2: ("Experiment Design Validator", "tools.design_validator", "Validate experiment designs"),
    3: ("Research Journal Recommender", "tools.journal_recommender", "Find suitable journals"),
    4: ("Conference Abstract Generator", "tools.abstract_generator", "Create abstracts"),
    5: ("Methodology Comparison Tool", "tools.methodology_comparison", "Compare methodologies"),
    6: ("Statistical Significance Explainer", "tools.stats_explainer", "Understand statistics"),
    7: ("Grant Opportunity Matcher", "tools.grant_matcher", "Find relevant grants"),
    8: ("Research Question Refinement", "tools.question_refinement", "Refine questions"),
    9: ("Interdisciplinary Connection Mapper", "tools.interdisciplinary_mapper", "Map connections"),
    10: ("Experimental Bias Detective", "tools.bias_detective", "Identify biases"),
}

def show_menu():
    console.clear()
    console.print(Panel.fit("[bold cyan]🔬 Ollama Research & Analysis Tools[/bold cyan]\n[dim]10 AI-Powered Research Assistants[/dim]", border_style="cyan"))
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Tool", style="green", width=38)
    table.add_column("Description", style="dim")
    for num, (name, _, desc) in TOOLS.items():
        table.add_row(str(num), name, desc)
    table.add_row("0", "Exit", "Quit")
    console.print(table)

def run_tool(choice: int):
    if choice == 0:
        console.print("[yellow]Goodbye! Happy researching! 🔬[/yellow]")
        sys.exit(0)
    if choice not in TOOLS:
        console.print("[red]Invalid choice.[/red]")
        return
    name, module_path, _ = TOOLS[choice]
    console.print(f"\n[bold green]Starting {name}...[/bold green]\n")
    try:
        module = __import__(module_path, fromlist=['run'])
        module.run()
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    console.print("\n[dim]Press Enter to continue...[/dim]")
    input()

def main():
    try:
        import ollama
        ollama.list()
    except:
        console.print("[red]Ollama not running. Run: ollama serve[/red]")
        sys.exit(1)
    while True:
        show_menu()
        try:
            choice = IntPrompt.ask("Select", default=0)
            run_tool(choice)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
