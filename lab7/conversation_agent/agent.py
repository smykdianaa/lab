from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext

def save_user_preference(tool_context: ToolContext, preference_type: str, value: str) -> dict:
    """Зберігає вподобання користувача в стані агента."""
    existing_state = tool_context.state.get(preference_type, [])
    # Оновлюємо стан
    tool_context.state[preference_type] = existing_state + [value]
    print(f"[Memory Added] {preference_type}: {value}")
    return {
        "status": "success",
        "message": f"Запам'ятав: {preference_type} - {value}"
    }

def recall_preference(tool_context: ToolContext, preference_type: str) -> dict:
    """Дістає вподобання зі стану агента."""
    preferences = tool_context.state.get(preference_type, [])
    if preferences:
        return {
            "status": "success",
            "values": preferences
        }
    return {"status": "error", "message": "Інформація відсутня"}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='conversation_agent',
    description="Агент з довготривалою пам'яттю.",
    instruction="""
    Ти дружелюбний асистент. 
    Твоє завдання — знайомитися з користувачем та запам'ятовувати факти про нього.
    Коли користувач називає ім'я, хобі чи колір — викликай save_user_preference.
    Коли запитує про себе — викликай recall_preference.
    Відповідай українською мовою.
    """,
    tools=[save_user_preference, recall_preference],
)