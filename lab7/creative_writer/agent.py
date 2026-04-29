from google.adk.agents.llm_agent import Agent
from google.genai.types import GenerateContentConfig

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії.
    Args:
        theme: тема історії
        characters: кількість персонажів
    """
    return f"Створи цікаву історію на тему '{theme}' з {characters} персонажами."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='creative_writer',
    description="Креативний письменник історій.",
    instruction="""
    Ти талановитий письменник. Твої історії мають бути захоплюючими, 
    з несподіваними поворотами та яскравими персонажами. 
    Використовуй багату українську мову.
    """,
    tools=[generate_story_prompt],
    # Налаштування для високої креативності
    config=GenerateContentConfig(
        temperature=1.5,  # Чим вище значення, тим більше "фантазії" у моделі
        top_k=40,
        top_p=0.95,
    )
)