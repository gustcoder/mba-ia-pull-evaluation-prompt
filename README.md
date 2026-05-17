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

## Técnicas Aplicadas (Fase 2)
* Role Prompting: trabalhar com um papel designado para a IA ajuda no contexto e na atuação na hora de avaliar e processar os prompts, por isso escolhi esta técnica.
* Few-Shot Learning: exemplos, juntamente com o papel definido, constroem um bom combo para execução assertiva de tarefas visando os outputs desejados.

## Resultados Finais
<img width="914" height="1023" alt="image" src="https://github.com/user-attachments/assets/1dc93fe3-d93c-4d1b-b062-d8fb0ecb4943" />

## Como Executar

```bash
# Navegue até a raiz da pasta do desafio
cd mba-ia-pull-evaluation-prompt

# Subir ambiente Docker
docker compose up -d

# Executar pull dos prompts ruins 
docker exec -it python_app_evaluation_prompt python src/pull_prompts.py

# Fazer push dos prompts otimizados
docker exec -it python_app_evaluation_prompt python src/push_prompts.py

# Executar avaliação
docker exec -it python_app_evaluation_prompt python src/evaluate.py
```

## Evidências no LangSmith
<img width="1902" height="900" alt="image" src="https://github.com/user-attachments/assets/e7b964ae-9f48-40a4-ba48-20866752abab" />
[Tracing/mba-ia-pull-evaluation-prompt](https://smith.langchain.com/o/06c96cef-80d5-45d8-a69a-c82731cb692c/projects/p/e1280f82-97ec-420c-b1b8-79913fd1735c?scroll_to=feedback&timeModel=%7B%22duration%22%3A%221h%22%7D)
<img width="1265" height="892" alt="image" src="https://github.com/user-attachments/assets/43226f8b-c6df-493b-a8e2-8610a5144bf8" />
