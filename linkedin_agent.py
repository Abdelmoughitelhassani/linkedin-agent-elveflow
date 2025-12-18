from crewai import Crew, Agent, Task, LLM
from dotenv import load_dotenv
import os
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List



load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "sk-dummy-key-not-used"

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant")
DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "French")

if not GROQ_API_KEY:
    print("❌ ERREUR : GROQ_API_KEY non trouvée!")
    print("📝 Obtenir une clé : https://console.groq.com/keys")
    exit(1)

llm = LLM(
    model=f"groq/{GROQ_MODEL}",
    api_key=GROQ_API_KEY,
    temperature=0.7,
    max_tokens=1000,
)

print(f"✅ LLM configuré: {GROQ_MODEL} via Groq")

# =====================================================
# DONNÉES PRODUIT COBALT (extraites de la vraie page)
# =====================================================

PRODUCT_NAME = "COBALT - Autonomous Microfluidic Pump"
PRODUCT_URL = "https://elveflow.com/microfluidic-products/microfluidics-flow-control-systems/autonomous-vacuum-pressure-pumps/"

PRODUCT_INFO = """
PRODUIT: COBALT - Autonomous Microfluidic Pump
Pompe microfluidique autonome - Contrôleur de pression/vacuum standalone

=== CARACTÉRISTIQUES CLÉS ===
- Deux versions disponibles:
  * Cobalt: 0 à 2000 mbar (pression positive uniquement)
  * Cobalt-DUAL: -700 à 1000 mbar (pression et vacuum)
- Source de pression INTÉGRÉE: pas besoin de compresseur externe ni d'alimentation en gaz
- Stabilité de pression: 0.1 mbar
- Temps de réponse: jusqu'à 10ms (logiciel embarqué) ou 100ms (logiciel PC)
- Temps de stabilisation: 75ms (Cobalt) / 105ms (Cobalt-DUAL)
- Compatible capteurs de débit MFS (MFS2: 0-7µl/min, MFS3: 0-80µl/min, MFS4: 0-1000µl/min, MFS5: 0-5000µl/min)
- Calibration automatique des capteurs
- Enregistrement de données intégré (jusqu'à 6000 sec)

=== BÉNÉFICES UTILISATEURS ===
- AUTONOME: fonctionne sans ordinateur grâce à l'interface embarquée
- STANDALONE: pas besoin de source de pression/vacuum externe
- PORTABLE: compact (328x235x168mm), léger (3.3kg / 4.1kg)
- SILENCIEUX: design minimisant vibrations et bruit
- FACILE: contrôle par bouton rotatif intuitif
- FLEXIBLE: utilisable avec ou sans ordinateur (logiciel Windows disponible)
- POLYVALENT: compatible avec solvants aqueux, organiques, huiles, solutions biologiques

=== APPLICATIONS ===
- Développement Lab-on-chip
- Tests et caractérisation (puces, capteurs, filtres)
- Mécanobiologie (confinement cellulaire, ingénierie tissulaire)
- Perfusion cellulaire
- Prototypage rapide
- Formation et enseignement en microfluidique
- Laboratoires sans accès à l'air comprimé

=== AVANTAGES vs CONCURRENCE ===
- Seule pompe microfluidique vraiment autonome du marché
- Basé sur la technologie OB1 MK4 (best-seller Elveflow, technologie piézoélectrique)
- Performances supérieures aux pompes seringues ou péristaltiques
- Flux lisse et précis sans pièce mécanique
- Haute répétabilité: de 3.5 nL/min (MFS2) à 1 µL/min (MFS5)
"""

# =====================================================
# CONTEXTE ENTREPRISE (extrait de l'offre WTTJ)
# =====================================================

COMPANY_CONTEXT = """
ENTREPRISE: Elvesys / Elveflow
Secteur: Biotechnologies / Instrumentation Microfluidique
Localisation: Paris (172 Rue de Charonne, 75011)

MISSION: Concevoir une instrumentation microfluidique de pointe pour permettre 
aux chercheurs et industriels de repousser les limites de leurs domaines.

PROFIL: Fondée en 2011 par 3 docteurs en microfluidique, 30 collaborateurs, 
équipe jeune (âge moyen 33 ans), culture startup à taille humaine.

PUBLIC CIBLE: Chercheurs en laboratoire, industriels en biotechnologie, 
pharmaceutique, cosmétique, énergie.
"""

# =====================================================
# GUIDE DE STYLE STRICT
# =====================================================

STYLE_GUIDE = """
=== STYLE DE COMMUNICATION ELVEFLOW ===

TON OBLIGATOIRE:
- Scientifique et professionnel (PAS casual, PAS humoristique)
- Informatif et éducatif (PAS publicitaire)
- Direct et factuel

INTERDICTIONS ABSOLUES:
❌ Pas de métaphores (ex: "Swiss watch", "toddler", "game-changer")
❌ Pas d'humour ou de blagues
❌ Pas de langage marketing exagéré ("revolutionary", "ultimate")
❌ Pas d'emojis inappropriés (ex: 🤦‍♀️ 😂 💪)
❌ Pas de questions rhétoriques excessives

EMOJIS AUTORISÉS: 🔬 🧪 ✅ 👉 🚀 💡

STRUCTURE:
1. Accroche (1 ligne): Style "No X. No Y. Just Z."
2. Contexte (2-3 lignes): Le défi des chercheurs
3. Solution (2-3 lignes): Comment COBALT répond
4. Features (3 lignes): Avec ✅
5. CTA (1 ligne): Avec 👉 et le VRAI lien
6. Hashtags: 4-5 tags

LONGUEUR: 100-150 mots MAXIMUM
"""

# =====================================================
# EXEMPLES DE POSTS DE RÉFÉRENCE
# =====================================================

REFERENCE_POSTS = """
=== POSTS LINKEDIN ELVEFLOW DE RÉFÉRENCE ===

POST 1 (Produit - Bubble Remover):
"No Bubble. No Trouble. Just Stable Flow.
In microfluidics, even the tiniest bubbles can disturb your flow stability, damage cells, or interrupt continuous experiments.
That's why we designed the Elveflow Microfluidic Bubble Remover, a simple yet powerful solution to keep your experiments free from bubbles.
✅ Remove air bubbles in-line before they reach your chip
✅ Biocompatible and autoclavable equipment
✅ Compatible with standard 1/32", 1/16″ and 1/8″ OD tubing
👉 Discover the Microfluidic Bubble Remover: https://bit.ly/3L8jxOU
#Microfluidics #BubbleRemoval #FlowStability #LabOnChip #Elveflow"

POST 2 (Conférence):
"New Conference Report from MicroTAS 2025 🦘🧪
We are pleased to share our conference report from MicroTAS 2025 in Adelaide, where Elveflow participated as a sponsor with a booth, a workshop, a poster, and a TechTalk.
Our recap covers key scientific trends, standout topics, and insights from this year's talks.
👉 Read the full MicroTAS 2025 highlights here: https://lnkd.in/esuH7ddm
#microtas2025 #microfluidics #elveflow #conferencereport #researchcommunity"

POST 3 (Research):
"🔬 Always pushing research forward
We have just updated our application note following the recent publication of the results in ACS Omega.
This work presents a high-resolution microfluidic approach that enables precise control and in-depth analysis of oil-in-water emulsions.
📄 You can read the updated version here: https://lnkd.in/eMPm7WE3
#microfluidics #Elveflow #research"
"""

# =====================================================
# MODÈLE DE SORTIE
# =====================================================

class LinkedInPost(BaseModel):
    """Post LinkedIn généré"""
    post_content: str = Field(description="Contenu complet du post prêt à publier")
    hashtags: List[str] = Field(description="Liste des hashtags utilisés")
    key_message: str = Field(description="Message principal / accroche du post")


# =====================================================
# AGENT
# =====================================================

def create_content_creator_agent() -> Agent:
    """Agent optimisé pour générer des posts style Elveflow"""
    return Agent(
        role="Rédacteur LinkedIn Scientifique - Elveflow",
        goal="Créer un post LinkedIn court, factuel et professionnel pour COBALT, en imitant exactement le style des posts de référence Elveflow",
        backstory="""Tu es le rédacteur LinkedIn officiel d'Elveflow.
        
        Tu connais PARFAITEMENT le ton Elveflow:
        - Scientifique et professionnel (JAMAIS humoristique)
        - Informatif et factuel (JAMAIS publicitaire)
        - Court et direct (100-150 mots MAX)
        
        Tu NE FAIS JAMAIS:
        - De métaphores ou comparaisons
        - D'humour ou de blagues
        - De langage marketing exagéré
        
        Tu écris EXACTEMENT comme les posts de référence fournis.""",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )


# =====================================================
# TÂCHE
# =====================================================

def create_post_task(agent: Agent, language: str = "French") -> Task:
    """Tâche de génération de post pour COBALT"""
    
    if language == "French":
        example = """EXEMPLE EN FRANÇAIS:
"Pas de compresseur. Pas d'ordinateur. Juste du flux. 🔬
Dans de nombreux laboratoires, l'accès à l'air comprimé reste un défi pour les expériences microfluidiques.
COBALT résout ce problème avec sa source de pression intégrée, permettant un contrôle de flux stable et autonome.
✅ Source de pression intégrée
✅ Fonctionne avec ou sans ordinateur  
✅ Compact et silencieux
👉 En savoir plus: {url}
#microfluidics #Elveflow #flowcontrol #labonaship #autonomouspump"
""".format(url=PRODUCT_URL)
    else:
        example = """EXAMPLE IN ENGLISH:
"No Compressor. No Computer. Just Flow. 🔬
In many labs, access to compressed air remains a challenge for microfluidic experiments.
COBALT solves this with its built-in pressure source, enabling stable and autonomous flow control right on your bench.
✅ Built-in pressure source
✅ Works with or without a computer
✅ Compact and quiet design
👉 Learn more: {url}
#microfluidics #Elveflow #flowcontrol #labonaship #autonomouspump"
""".format(url=PRODUCT_URL)
    
    return Task(
        description=f"""
Génère un post LinkedIn en {language} pour COBALT - Autonomous Microfluidic Pump.

{example}

=== INFORMATIONS PRODUIT ===
{PRODUCT_INFO}

=== CONTEXTE ENTREPRISE ===
{COMPANY_CONTEXT}

=== POSTS DE RÉFÉRENCE À IMITER ===
{REFERENCE_POSTS}

=== RÈGLES STRICTES ===

1. LONGUEUR: 100-150 mots MAXIMUM

2. STRUCTURE:
   - Accroche courte (style "No X. No Y. Just Z.")
   - Contexte/problème (2-3 lignes)
   - Solution COBALT (2-3 lignes)
   - 3 features avec ✅
   - CTA avec 👉 et ce lien EXACT: {PRODUCT_URL}
   - 4-5 hashtags incluant #microfluidics et #Elveflow

3. TON: Professionnel, scientifique, factuel
   - PAS d'humour ni de métaphores
   - PAS de superlatifs marketing

4. EMOJIS: Max 3-4 (🔬 🧪 ✅ 👉 uniquement)

5. LIEN: Utilise EXACTEMENT ce lien dans le CTA: {PRODUCT_URL}

6. LANGUE: {language} UNIQUEMENT

Le post doit être IDENTIQUE en style aux posts de référence.
        """,
        expected_output=f"Un post LinkedIn de 100-150 mots en {language}, avec le vrai lien {PRODUCT_URL}",
        agent=agent,
        output_pydantic=LinkedInPost
    )


# =====================================================
# GÉNÉRATION
# =====================================================

def generate_post(language: str = "French") -> LinkedInPost:
    """Génère un post LinkedIn pour COBALT"""
    
    print("\n" + "=" * 60)
    print("🚀 GÉNÉRATEUR DE POST LINKEDIN - COBALT")
    print("=" * 60)
    print(f"🤖 Modèle: {GROQ_MODEL}")
    print(f"📦 Produit: {PRODUCT_NAME}")
    print(f"🌍 Langue: {language}")
    print(f"🔗 URL: {PRODUCT_URL}")
    print("=" * 60 + "\n")
    
    agent = create_content_creator_agent()
    task = create_post_task(agent, language)
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )
    
    print("⏳ Génération en cours...\n")
    result = crew.kickoff()
    
    if result and hasattr(result, 'pydantic') and result.pydantic:
        post = result.pydantic
        
        # Vérifier si le lien est présent, sinon l'ajouter
        if PRODUCT_URL not in post.post_content and "[link]" in post.post_content:
            post.post_content = post.post_content.replace("[link]", PRODUCT_URL)
        
        print("\n" + "=" * 60)
        print("✅ POST GÉNÉRÉ AVEC SUCCÈS!")
        print("=" * 60)
        print(f"\n{post.post_content}\n")
        print("-" * 60)
        print(f"📌 Hashtags: {', '.join(post.hashtags)}")
        print(f"💡 Accroche: {post.key_message}")
        print(f"🔗 Lien: {PRODUCT_URL}")
        print("=" * 60 + "\n")
        
        return post
    
    print("\n📝 Résultat brut:")
    print(result)
    return None


# =====================================================
# INTERFACE CLI
# =====================================================

def main():
    print("\n" + "=" * 60)
    print("🤖 GÉNÉRATEUR DE POST LINKEDIN")
    print("📦 Produit: COBALT - Autonomous Microfluidic Pump")
    print("🦙 Propulsé par Groq + Llama")
    print("=" * 60)
    
    print("\n🌍 Choisir la langue:")
    print("  1. Français")
    print("  2. English")
    
    lang_choice = input("\nLangue (1 ou 2) [défaut: 1]: ").strip() or "1"
    language = "French" if lang_choice == "1" else "English"
    
    result = generate_post(language)
    
    if result:
        save = input("\n💾 Sauvegarder le post? (o/n) [o]: ").strip().lower()
        if save in ["o", "oui", "y", "yes", ""]:
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            
            filename = output_dir / f"post_cobalt_{language.lower()}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=" * 50 + "\n")
                f.write(f"POST LINKEDIN - {PRODUCT_NAME}\n")
                f.write("=" * 50 + "\n\n")
                f.write(result.post_content)
                f.write(f"\n\n---")
                f.write(f"\nHashtags: {' '.join(result.hashtags)}")
                f.write(f"\nAccroche: {result.key_message}")
                f.write(f"\nURL: {PRODUCT_URL}")
            
            print(f"✅ Sauvegardé: {filename}")
    
    another = input("\n🔄 Générer un autre post? (o/n) [n]: ").strip().lower()
    if another in ["o", "oui", "y", "yes"]:
        main()


if __name__ == "__main__":
    main()