from google.adk.agents.llm_agent import Agent
import math

# 1. Інструмент: Площа прямокутника
def calculate_rectangle_area(width: float, height: float) -> float:
    """Обчислює площу прямокутника.
    Args:
        width: ширина прямокутника
        height: висота прямокутника
    """
    return width * height

# 2. Інструмент: Площа кола
def calculate_circle_area(radius: float) -> float:
    """Обчислює площу кола.
    Args:
        radius: радіус кола
    """
    return math.pi * radius ** 2

# 3. Інструмент: Об'єм куба
def calculate_cube_volume(side: float) -> float:
    """Обчислює об'єм куба.
    Args:
        side: довжина ребра куба
    """
    return side ** 3

# ⭐ 4. ДОДАТКОВИЙ ІНСТРУМЕНТ: Площа трикутника
def calculate_triangle_area(base: float, height: float) -> float:
    """Обчислює площу трикутника за основою та висотою.
    Args:
        base: основа трикутника
        height: висота трикутника
    """
    return 0.5 * base * height

# Створення математичного агента
root_agent = Agent(
    model='gemini-2.5-flash', #
    name='math_agent',
    description="Виконує математичні обчислення геометричних фігур.",
    instruction="""
    Ти експертний математичний асистент. 
    У тебе є інструменти для обчислення площі прямокутника, кола, трикутника та об'єму куба.
    Завжди використовуй відповідні функції (tools) для розрахунків. 
    Відповідай українською мовою та пояснюй логіку.
    """,
    tools=[
        calculate_rectangle_area, 
        calculate_circle_area, 
        calculate_cube_volume, 
        calculate_triangle_area
    ], #
)