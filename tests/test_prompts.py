"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    prompt_file = (
        Path(__file__).resolve().parents[1]
        / "prompts"
        / "bug_to_user_story_v2.yml"
    )

    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""

        prompts = load_prompts(self.prompt_file)

        for prompt_name, prompt in prompts.items():
            system_prompt = prompt.get("system_prompt")

            assert system_prompt is not None, (
                f"{prompt_name}: system_prompt ausente"
            )

            assert isinstance(system_prompt, str), (
                f"{prompt_name}: system_prompt inválido"
            )

            assert system_prompt.strip(), (
                f"{prompt_name}: system_prompt vazio"
            )

    def test_prompt_has_role_definition(self):
        """
        Verifica se o prompt define uma persona.
        """

        import re

        prompts = load_prompts(self.prompt_file)

        role_patterns = [
            r"Você é um",
            r"Você é uma",
            r"##\s*Role",
            r"##\s*Papel"
        ]

        for prompt_name, prompt in prompts.items():

            system_prompt = prompt.get(
                "system_prompt",
                ""
            )

            found = any(
                re.search(
                    pattern,
                    system_prompt,
                    re.IGNORECASE
                )
                for pattern in role_patterns
            )

            assert found, (
                f"{prompt_name}: persona não encontrada"
            )

    def test_prompt_mentions_format(self):
        """
        Verifica se existe definição de formato.
        """

        import re

        prompts = load_prompts(self.prompt_file)

        expected_patterns = [
            r"Formato de Saída",
            r"História de Usuário",
            r"Critérios de Aceitação",
            r"Markdown"
        ]

        for prompt_name, prompt in prompts.items():

            system_prompt = prompt.get(
                "system_prompt",
                ""
            )

            found = any(
                re.search(
                    pattern,
                    system_prompt,
                    re.IGNORECASE
                )
                for pattern in expected_patterns
            )

            assert found, (
                f"{prompt_name}: formato não encontrado"
            )

    def test_prompt_has_few_shot_examples(self):
        """
        Verifica se existem exemplos few-shot.
        """

        import re

        prompts = load_prompts(self.prompt_file)

        for prompt_name, prompt in prompts.items():

            system_prompt = prompt.get(
                "system_prompt",
                ""
            )

            examples = re.findall(
                r"##\s*Exemplo\s+\d+",
                system_prompt,
                re.IGNORECASE
            )

            assert len(examples) >= 2, (
                f"{prompt_name}: "
                f"few-shot insuficiente "
                f"({len(examples)} encontrado(s))"
            )

    def test_prompt_no_todos(self):
        """
        Garante ausência de TODO/FIXME esquecidos.
        """

        import re

        prompts = load_prompts(self.prompt_file)

        patterns = [
            r"\[TODO\]",
            r"TODO:",
            r"FIXME",
            r"XXX"
        ]

        for prompt_name, prompt in prompts.items():

            full_text = (
                prompt.get("system_prompt", "")
                + "\n"
                + prompt.get("user_prompt", "")
            )

            found = any(
                re.search(
                    pattern,
                    full_text,
                    re.IGNORECASE
                )
                for pattern in patterns
            )

            assert not found, (
                f"{prompt_name}: TODO encontrado"
            )

    def test_minimum_techniques(self):
        """
        Verifica se há pelo menos
        duas técnicas de prompting.
        """

        import re

        prompts = load_prompts(self.prompt_file)

        for prompt_name, prompt in prompts.items():

            techniques = set()

            tags = prompt.get(
                "tags",
                []
            )

            techniques.update(tags)

            system_prompt = prompt.get(
                "system_prompt",
                ""
            )

            if re.search(
                r"Você é|Role",
                system_prompt,
                re.IGNORECASE
            ):
                techniques.add("role")

            if re.search(
                r"##\s*Exemplo",
                system_prompt,
                re.IGNORECASE
            ):
                techniques.add("few-shot")

            if re.search(
                r"Instruções|Restrições",
                system_prompt,
                re.IGNORECASE
            ):
                techniques.add("constraints")

            assert len(techniques) >= 2, (
                f"{prompt_name}: "
                f"técnicas insuficientes: "
                f"{list(techniques)}"
            )

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])