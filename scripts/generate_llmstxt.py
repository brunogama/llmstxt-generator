#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests>=2.28.0",
#     "pathlib2>=2.3.7.post1",
#     "typer>=0.9.0",
#     "rich>=13.0.0",
# ]
# ///

"""
generate_llmstxt.py - Generate llms.txt files using Ollama LLM models

This script analyzes project documentation and uses Ollama to intelligently
generate llms.txt files that are LLM-optimized and follow the llmstxt.org spec.

Usage:
    uv run generate_llmstxt.py --project /path/to/project --model llama2
    python generate_llmstxt.py --project . --output ./llms.txt
    uvx --from llmstxt-generator generate_llmstxt.py --help
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any
import sys

try:
    import requests
    import typer
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.panel import Panel
    from rich.syntax import Syntax
except ImportError:
    print("Error: Missing dependencies. Install with:")
    print("  pip install requests typer rich")
    print("Or run with: uvx --from llmstxt-generator generate_llmstxt.py")
    sys.exit(1)

# Rich console for pretty output
console = Console()
app = typer.Typer(help="Generate llms.txt files using Ollama LLM models")


class OllamaClient:
    """Client for communicating with Ollama API"""

    def __init__(self, host: str = "http://localhost:11434"):
        self.host = host
        self.timeout = 300  # 5 minute timeout for generation

    def check_connection(self) -> bool:
        """Check if Ollama is running and accessible"""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception as e:
            console.print(f"❌ Cannot connect to Ollama at {self.host}", style="red")
            console.print(f"   Error: {str(e)}", style="dim red")
            return False

    def list_models(self) -> List[str]:
        """Get list of available models"""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return [m["name"].split(":")[0] for m in data.get("models", [])]
            return []
        except Exception:
            return []

    def generate(self, model: str, prompt: str, context: Optional[str] = None) -> str:
        """Generate text using Ollama model"""
        full_prompt = f"{context}\n\n{prompt}" if context else prompt

        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console
            ) as progress:
                progress.add_task(f"[cyan]Generating with {model}...", total=None)

                response = requests.post(
                    f"{self.host}/api/generate",
                    json={
                        "model": model,
                        "prompt": full_prompt,
                        "stream": False,
                        "temperature": 0.7,
                    },
                    timeout=self.timeout
                )

                if response.status_code == 200:
                    return response.json()["response"]
                else:
                    console.print(f"❌ Generation failed: {response.text}", style="red")
                    return ""
        except Exception as e:
            console.print(f"❌ Error during generation: {str(e)}", style="red")
            return ""


class DocumentationAnalyzer:
    """Analyze project documentation structure"""

    def __init__(self, project_path: Path):
        self.project_path = Path(project_path).resolve()
        self.docs_files = []
        self.project_type = "unknown"
        self.readme_content = ""

    def analyze(self) -> Dict[str, Any]:
        """Analyze project and find documentation"""
        console.print("🔍 Analyzing project structure...", style="cyan")

        self._detect_project_type()
        self._find_documentation()
        self._read_readme()

        return {
            "project_type": self.project_type,
            "path": str(self.project_path),
            "docs_files": self.docs_files,
            "readme": self.readme_content,
            "file_count": len(self.docs_files),
        }

    def _detect_project_type(self):
        """Detect project type from files present"""
        files = list(self.project_path.rglob("*"))
        file_names = [f.name for f in files]

        if "package.json" in file_names:
            self.project_type = "Node.js"
        elif "pyproject.toml" in file_names or "setup.py" in file_names:
            self.project_type = "Python"
        elif "Cargo.toml" in file_names:
            self.project_type = "Rust"
        elif "Package.swift" in file_names:
            self.project_type = "Swift"
        elif "go.mod" in file_names:
            self.project_type = "Go"
        else:
            # Assume docs site if lots of markdown
            md_count = len(list(self.project_path.rglob("*.md")))
            if md_count > 5:
                self.project_type = "Documentation Site"

    def _find_documentation(self):
        """Find documentation files in project"""
        patterns = ["*.md", "**/*.md", "**/*.html", "**/*.rst"]
        ignore_dirs = ["node_modules", ".git", "build", "dist", ".next", "venv"]

        for pattern in patterns:
            for file_path in self.project_path.glob(pattern):
                # Skip ignored directories
                if any(ignore in str(file_path) for ignore in ignore_dirs):
                    continue

                # Skip non-docs
                if file_path.name.startswith("."):
                    continue

                self.docs_files.append(str(file_path.relative_to(self.project_path)))

        self.docs_files = sorted(list(set(self.docs_files)))[:50]  # Limit to 50 files

    def _read_readme(self):
        """Read README to understand project"""
        readme_paths = [
            self.project_path / "README.md",
            self.project_path / "readme.md",
            self.project_path / "README.rst",
        ]

        for readme_path in readme_paths:
            if readme_path.exists():
                try:
                    with open(readme_path, "r", encoding="utf-8") as f:
                        self.readme_content = f.read()[:500]  # First 500 chars
                    break
                except Exception:
                    continue


def generate_llmstxt_prompt(analysis: Dict[str, Any]) -> str:
    """Create prompt for Ollama to generate llms.txt"""
    docs_list = "\n".join(f"  - {doc}" for doc in analysis["docs_files"][:15])

    prompt = f"""Create an llms.txt file for this {analysis['project_type']} project.

Project: {analysis['path']}
Documentation files ({analysis['file_count']} found):
{docs_list}

Project Description (from README):
{analysis['readme'][:200]}...

Generate a valid llms.txt file following the llmstxt.org specification:
- Start with # [Project Name]
- Add a > blockquote summary (2-3 sentences)
- Include 3-5 well-organized sections with H2 headings
- Add 3-6 relevant links per section with descriptions
- Make descriptions specific and under 100 characters
- Include an ## Optional section for supplementary links

Important:
- Focus on key documentation and guides
- Be specific in descriptions (not vague)
- Follow Markdown format exactly
- Links should point to actual doc files or resources
- Make it LLM-friendly and concise

Generate only the llms.txt content, no explanations:"""

    return prompt


@app.command()
def main(
    project: Optional[str] = typer.Option(
        ".",
        "--project", "-p",
        help="Path to project directory",
        metavar="PATH"
    ),
    output: Optional[str] = typer.Option(
        None,
        "--output", "-o",
        help="Output file path (default: ./llms.txt)",
        metavar="PATH"
    ),
    model: Optional[str] = typer.Option(
        None,
        "--model", "-m",
        help="Ollama model to use (auto-detects if not specified)",
        metavar="MODEL"
    ),
    host: Optional[str] = typer.Option(
        "http://localhost:11434",
        "--host", "-h",
        help="Ollama API host",
        metavar="URL"
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose", "-v",
        help="Show detailed output"
    ),
):
    """Generate an llms.txt file for a project using Ollama"""

    console.print("\n[bold cyan]llms.txt Generator[/bold cyan]", justify="center")
    console.print("Powered by Ollama LLM\n", justify="center", style="dim")

    # Initialize clients
    ollama = OllamaClient(host)

    # Check Ollama connection
    console.print("🤖 Checking Ollama connection...", style="cyan")
    if not ollama.check_connection():
        console.print("\n[red]❌ Error: Cannot connect to Ollama[/red]")
        console.print("   Make sure Ollama is running:", style="dim")
        console.print("   $ ollama serve", style="dim yellow")
        raise typer.Exit(1)

    console.print("✓ Connected to Ollama", style="green")

    # List available models
    console.print("\n🤖 Available models:", style="cyan")
    models = ollama.list_models()

    if not models:
        console.print("[red]❌ No models found. Install one:[/red]")
        console.print("   $ ollama pull llama2", style="dim yellow")
        raise typer.Exit(1)

    for m in models:
        console.print(f"   • {m}", style="dim")

    # Select or use specified model
    if model is None:
        model = models[0] if "llama2" in models else models[0]
        console.print(f"\nℹ️  Using default model: {model}", style="dim")
    elif model not in models:
        console.print(f"\n[red]❌ Model '{model}' not found[/red]", style="red")
        console.print(f"   Available: {', '.join(models)}", style="dim red")
        raise typer.Exit(1)

    # Analyze project
    console.print("\n📂 Analyzing project...", style="cyan")
    analyzer = DocumentationAnalyzer(project)
    analysis = analyzer.analyze()

    console.print(f"   Project type: {analysis['project_type']}", style="dim")
    console.print(f"   Documentation files: {analysis['file_count']}", style="dim")

    # Generate with Ollama
    console.print(f"\n⏳ Generating llms.txt with {model}...", style="cyan")
    prompt = generate_llmstxt_prompt(analysis)

    if verbose:
        console.print("\n[dim]Prompt sent to Ollama:[/dim]")
        syntax = Syntax(prompt, "markdown", theme="monokai", line_numbers=False)
        console.print(syntax)

    generated_content = ollama.generate(model, prompt)

    if not generated_content:
        console.print("\n[red]❌ Generation failed[/red]")
        raise typer.Exit(1)

    # Determine output path
    output_path = Path(output or "./llms.txt").resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save generated file
    console.print(f"\n💾 Saving to: {output_path}", style="cyan")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generated_content)

    # Show result
    console.print("\n✅ Success! Generated llms.txt\n", style="green")

    console.print(Panel(
        generated_content[:500] + "..." if len(generated_content) > 500 else generated_content,
        title="Generated Content (Preview)",
        border_style="green"
    ))

    console.print(f"\n📍 File: {output_path}", style="dim")
    console.print(f"📊 Size: {len(generated_content)} characters", style="dim")

    console.print("\n💡 Next steps:", style="cyan")
    console.print("   1. Review the generated file")
    console.print("   2. Run: /llmstxt:validate")
    console.print("   3. Edit if needed: /llmstxt:edit")
    console.print("   4. Commit to git: git add llms.txt")
    console.print()


if __name__ == "__main__":
    app()
