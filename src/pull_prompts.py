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
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    print_section_header("Pulling prompt from LangSmith")

    client = Client()

    prompt = client.pull_prompt("leonanluppi/bug_to_user_story_v1")

    prompt_data = {
        "bug_to_user_story_v1": {
            "description": "Prompt para converter relatos de bugs em User Stories",
            "system_prompt": prompt.messages[0].prompt.template,
            "user_prompt": prompt.messages[1].prompt.template,
            "version": "v1",
            "created_at": "2025-01-15",
            "tags": [
                "bug-analysis",
                "user-story",
                "product-management",
            ],
        }
    }

    output_path = Path("prompts/bug_to_user_story_v1_new.yml")

    save_yaml(prompt_data, str(output_path))

    print(f"Prompt saved to: {output_path}")


def main():
    """Função principal"""
    pull_prompts_from_langsmith()


if __name__ == "__main__":
    sys.exit(main())
