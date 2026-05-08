from __future__ import annotations

from typing import Any


class PromptValidator:
    """
    Responsável por validar a estrutura de prompts.
    """

    REQUIRED_FIELDS = (
        "description",
        "system_prompt",
        "user_prompt",
    )

    OPTIONAL_LIST_FIELDS = (
        "tags",
    )

    def validate(
        self,
        prompt_data: dict[str, Any],
    ) -> tuple[bool, list]:
        """
        Valida estrutura básica de um prompt.

        Args:
            prompt_data: Dados do prompt

        Returns:
            Tuple contendo:
            - bool: status da validação
            - list[str]: lista de erros encontrados
        """

        errors: list[str] = []

        # =========================
        # Estrutura base
        # =========================
        if not isinstance(prompt_data, dict):
            return False, ["prompt_data deve ser um dict"]

        # =========================
        # Campos obrigatórios
        # =========================
        for field in self.REQUIRED_FIELDS:
            if field not in prompt_data:
                errors.append(
                    f"Campo obrigatório ausente: '{field}'"
                )

        # Evita validações redundantes
        if errors:
            return False, errors

        # =========================
        # Strings obrigatórias
        # =========================
        for field in self.REQUIRED_FIELDS:
            self._validate_non_empty_string(
                field_name=field,
                value=prompt_data.get(field),
                errors=errors,
            )

        # =========================
        # Listas opcionais
        # =========================
        for field in self.OPTIONAL_LIST_FIELDS:
            if field in prompt_data:
                self._validate_string_list(
                    field_name=field,
                    value=prompt_data[field],
                    errors=errors,
                )

        return len(errors) == 0, errors

    # ==========================================================
    # Métodos privados
    # ==========================================================

    def _validate_non_empty_string(
        self,
        field_name: str,
        value: Any,
        errors: list[str],
    ) -> None:
        """
        Valida se o valor é uma string não vazia.
        """

        if not isinstance(value, str):
            errors.append(
                f"'{field_name}' deve ser uma string"
            )
            return

        if not value.strip():
            errors.append(
                f"'{field_name}' não pode estar vazio"
            )

    def _validate_string_list(
        self,
        field_name: str,
        value: Any,
        errors: list[str],
    ) -> None:
        """
        Valida listas contendo apenas strings.
        """

        if not isinstance(value, list):
            errors.append(
                f"'{field_name}' deve ser uma lista"
            )
            return

        if not all(isinstance(item, str) for item in value):
            errors.append(
                f"'{field_name}' deve conter apenas strings"
            )

