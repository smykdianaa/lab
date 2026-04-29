from google.adk.agents.llm_agent import Agent
from google.adk.agents.workflow_agents import SequentialAgent, ParallelAgent, LoopAgent

# 1. Паралельні дослідники
researcher_1 = Agent(model='gemini-2.5-flash', name='tech_expert', instruction="Досліди технічні тренди.")
researcher_2 = Agent(model='gemini-2.5-flash', name='market_analyst', instruction="Досліди ринкові показники.")

gather_data = ParallelAgent(
    name="data_gathering",
    agents=[researcher_1, researcher_2]
)

# 2. Послідовний аналітик
writer = Agent(model='gemini-2.5-flash', name='writer', instruction="Склади звіт на основі даних.")
reviewer = Agent(model='gemini-2.5-flash', name='reviewer', instruction="Перевір звіт на помилки.")

process_report = SequentialAgent(
    name="report_pipeline",
    agents=[gather_data, writer, reviewer]
)

# 3. Цикл покращення якості
def check_quality(tool_context, report_text):
    """Вихід з циклу, якщо звіт ідеальний."""
    if "ІДЕАЛЬНО" in report_text:
        return {"exit": True}
    return {"exit": False}

final_agent = LoopAgent(
    name="final_optimizer",
    agent=process_report,
    exit_condition=check_quality
)

root_agent = final_agent