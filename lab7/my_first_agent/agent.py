from google.adk.agents.llm_agent import Agent

# Базовий шаблон без додаткових інструментів
root_agent = Agent(
    model='gemini-2.5-flash',
    name='my_first_agent',
    description="Простий розмовний агент.",
    instruction="Ти корисний асистент. Відповідай українською мовою.",
)