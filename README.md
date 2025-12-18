# 🔬 Agent IA - Générateur de Posts LinkedIn pour Elveflow

Agent IA qui génère automatiquement des posts LinkedIn professionnels pour les produits Elveflow (instrumentation microfluidique).

## 📋 Contexte

Ce projet a été réalisé dans le cadre du **test technique** pour le poste d'**Ingénieur Technico-Commercial** chez **Elvesys/Elveflow**.

**Objectif** : Créer un agent IA capable de transformer une page produit technique en post LinkedIn engageant, en respectant le ton et le style de communication d'Elveflow.

## 🚀 Démonstration

```
============================================================
🤖 GÉNÉRATEUR DE POST LINKEDIN
📦 Produit: COBALT - Autonomous Microfluidic Pump
🦙 Propulsé par Groq + Llama
============================================================

🌍 Choisir la langue:
  1. Français
  2. English
```

### Exemple de post généré :

> **No Compressor. No Computer. Just Flow. 🔬**
>
> In many labs, access to compressed air remains a challenge for microfluidic experiments, where stable flow control is crucial for reliable results.
>
> COBALT solves this with its built-in pressure source, enabling stable and autonomous flow control right on your bench.
>
> ✅ Built-in pressure source – no external compressor needed  
> ✅ Works with or without a computer  
> ✅ Compact and quiet design
>
> 👉 Learn more: https://elveflow.com/microfluidic-products/microfluidics-flow-control-systems/autonomous-vacuum-pressure-pumps/
>
> #microfluidics #Elveflow #flowcontrol #labonaship #autonomouspump

## 🛠️ Stack Technique

| Composant | Technologie |
|-----------|-------------|
| Framework | [CrewAI](https://github.com/joaomdmoura/crewAI) |
| LLM | Llama 3.1 8B via [Groq](https://groq.com/) (gratuit) |
| Langage | Python 3.12 |
| Dépendances | Poetry |

## 📦 Installation

### Prérequis
- Python 3.10+
- Poetry
- Clé API Groq (gratuite sur [console.groq.com](https://console.groq.com/keys))

### Installation

```bash
# Cloner le repo
git clone https://github.com/Abdelmoughitelhassani/linkedin-agent-elveflow.git
cd linkedin-agent-elveflow

# Installer les dépendances
poetry install

# Configurer l'environnement
cp .env.example .env
# Éditer .env et ajouter votre clé GROQ_API_KEY
```

### Lancer l'agent

```bash
poetry run python linkedin_agent_final.py
```

## 📄 Livrables du Test Technique

1. **Analyse du contexte** - Compréhension d'Elveflow, du produit COBALT et du ton LinkedIn
2. **Post LinkedIn rédigé** - Généré par l'agent IA
3. **Prompt d'agent IA** - Instructions optimisées pour le style Elveflow
4. **Workflow d'automatisation** - Architecture et flux de données
5. **Note explicative** - Choix techniques et pistes d'amélioration

📎 Voir le document complet : [`docs/Test_Technique_Livrables.docx`](docs/Test_Technique_Livrables.docx)

## 🔧 Architecture Actuelle

```
[Données pré-chargées] → [Prompt + LLM] → [Post LinkedIn]
```

**Note** : Dans cette version prototype, les données (page produit, posts de référence, contexte entreprise) sont pré-chargées dans le code. Il n'y a pas de scraping automatique.

## 🚀 Améliorations Futures

Avec plus de temps et de ressources, le projet pourrait évoluer vers :

1. **LLM plus performant** - GPT-4, Claude ou Llama 70B pour de meilleurs résultats
2. **Architecture multi-agents** - Agent Scraper + Agent Analyste + Agent Rédacteur
3. **Scraping dynamique** - Extraction automatique depuis n'importe quelle URL produit
4. **Prompt générique** - Adaptation automatique à tous les produits Elveflow
5. **Publication automatique** - Intégration avec l'API LinkedIn (OAuth)

## 📁 Structure du Projet

```
├── linkedin_agent_final.py   # Agent principal
├── pyproject.toml            # Configuration Poetry
├── .env.example              # Template variables d'environnement
├── output/                   # Posts générés
└── docs/                     # Documentation et livrables
```

## 👤 Auteur

Projet réalisé pour le test technique Elvesys/Elveflow - Décembre 2024

---

*Ce projet utilise des technologies open-source (CrewAI, Llama) et une API gratuite (Groq).*
