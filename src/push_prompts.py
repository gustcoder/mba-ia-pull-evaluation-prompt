"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
import yaml
from typing import Dict, Any
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from langsmith import Client
from utils import load_yaml, check_env_vars, print_section_header
from validators.prompt_validator import PromptValidator

load_dotenv()


def load_prompt_yaml(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Pega a primeira chave raiz do YAML
    # Exemplo:
    # bug_to_user_story_v2:
    #   description: ...
    root_key = next(iter(data))

    return {
        "name": root_key,
        **data[root_key],
    }

def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        client = Client()

        # Extrai informações do dict
        description = prompt_data.get("description", "")
        system_prompt = prompt_data.get("system_prompt", "")
        user_prompt = prompt_data.get("user_prompt", "")
        tags = prompt_data.get("tags", ["bug-analysis", "user-story", "product-management"])

        # Cria PromptTemplate
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", user_prompt),
            ]
        )

        # Faz push para o Hub
        # Formato geralmente: "username/prompt_name"
        client.push_prompt(
            prompt_identifier=prompt_name,
            object=prompt,
            description=description,
            tags=tags,
            is_public=True,
        )

        print(f"✅ Prompt sent to LangSmith Hub: {prompt_name}")
        return True

    except Exception as e:
        print(f"❌ Error to sent prompt to LangSmith: {e}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    validator = PromptValidator()

    return validator.validate(prompt_data)


def main():
    """Função principal"""
    prompt_name = "bug_to_user_story_v2"
    prompt_data = load_prompt_yaml(
        "prompts/" + prompt_name + ".yml"
    )

    validate_prompt(prompt_data)

    push_prompt_to_langsmith(
        prompt_name=f"{os.getenv("USERNAME_LANGSMITH_HUB", "")}/{prompt_data['name']}",
        prompt_data=prompt_data,
    )


if __name__ == "__main__":
    sys.exit(main())
