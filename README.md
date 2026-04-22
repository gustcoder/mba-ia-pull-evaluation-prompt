# 🚀 Desafio MBA Engenharia de Software com IA - Full Cycle

![Status](https://img.shields.io/badge/Status-Em%20Progresso-orange?style=for-the-badge&logo=github)
![IA](https://img.shields.io/badge/Focus-AI%20Engineering-blueviolet?style=for-the-badge&logo=openai)
![FullCycle](https://img.shields.io/badge/School-FullCycle-yellow?style=for-the-badge)

**Objetivos:**
* 1. Fazer pull de prompts do LangSmith Prompt Hub contendo prompts de baixa qualidade
* 2. Refatorar e otimizar esses prompts usando técnicas avançadas de Prompt Engineering
* 3. Fazer push dos prompts otimizados de volta ao LangSmith
* 4. Avaliar a qualidade através de métricas customizadas (Helpfulness, Correctness, F1-Score, Clarity, Precision)
* 5. Atingir pontuação mínima de 0.9 (90%) em todas as métricas de avaliação

---

## 🛠️ Tecnologias e Requisitos

* Linguagem: Python 3.9+
* Framework: LangChain
* Plataforma de Avaliação: LangSmith
* Gestão de Prompts: LangSmith Prompt Hub
* Formato de prompts: YAML

---

## 💻 Como Executar o Desafio

```bash
# Navegue até a raiz da pasta do desafio
cd mba-ia-pull-evaluation-prompt

# Executar pull dos prompts ruins 
python src/pull_prompts.py

# Refatorar prompts
Edite manualmente o arquivo prompts/bug_to_user_story_v2.yml aplicando as técnicas aprendidas no curso.

# Fazer push dos prompts otimizados
python src/push_prompts.p

# Executar avaliação
python src/evaluate.py
