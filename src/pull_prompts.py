"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from datetime import date
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langsmith import Client
from ruamel.yaml.scalarstring import LiteralScalarString
from utils import save_yaml, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    print_section_header("Pulling prompt from LangSmith")
    client = Client()
    prompt = client.pull_prompt("leonanluppi/bug_to_user_story_v1")

    # Prompt Vars
    system_prompt = LiteralScalarString(
        prompt.messages[0].prompt.template
    )
    user_prompt = prompt.messages[1].prompt.template
    version = "v1"
    tags = [
        "bug-analysis",
        "user-story",
        "product-management",
    ]
    description = "Prompt para converter relatos de bugs em User Stories"

    # Build Prompt Data
    prompt_data = {
        "bug_to_user_story_v1": {
            "description": f"{description}",
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "version": version,
            "created_at": date.today().isoformat(),
            "tags": tags,
        }
    }

    output_path = Path("prompts/bug_to_user_story_v1.yml")

    save_yaml(prompt_data, str(output_path))

    print(f"Prompt saved to: {output_path}")


def main():
    """Função principal"""
    pull_prompts_from_langsmith()


if __name__ == "__main__":
    sys.exit(main())
