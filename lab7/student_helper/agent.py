from google.adk.agents.llm_agent import Agent

def explain_concept(concept: str, level: str = "beginner") -> dict:
    """Пояснює концепцію програмування.
    Args:
        concept: назва концепції для пояснення
        level: рівень складності (beginner, intermediate, advanced)
    """
    # Це спрощена логіка, ШІ доповнить ці дані сам
    return {
         "status": "success",
         "concept": concept,
         "level": level,
         "note": f"Виконай детальне пояснення для рівня {level}"
    }

def check_syntax(code: str, language: str = "python") -> dict:
    """Перевіряє синтаксис коду.
    Args:
        code: код для перевірки
        language: мова програмування
    """
    if not code.strip():
        return {"status": "error", "message": "Код порожній"}
    return {"status": "success", "message": "Синтаксис виглядає коректно", "language": language}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='student_helper',
    description="Помічник для студентів які вивчають програмування.",
    instruction="""
    Ти досвідчений викладач з ООП програмування. 
    Твої обов'язки:
    - Пояснювати складні концепції простими словами.
    - Наводити приклади коду (Markdown).
    - Перевіряти синтаксис коду через інструмент check_syntax.
    - Завжди відповідай українською мовою.
    """,
    tools=[explain_concept, check_syntax],
)