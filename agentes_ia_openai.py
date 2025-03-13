from agents import Agent, Runner, WebSearchTool
import asyncio
from dotenv import load_dotenv
load_dotenv()

history_tutor_agent = Agent(
    name="Tutor de Historia",
    handoff_description="Agente especialista em história",
    instructions="Você fornece ajuda na área de história. Explica com clareza e simplicidade.",
)

math_tutor_agent = Agent(
    name="Tutor de Matematica",
    handoff_description="Agente especialista em matemática",
    instructions="Você ajuda a resolver questões de matemática. Explica tudo passo a passo e fornece exemplos.",
)

web_search_agent = Agent(
    name="Agente de Busca na Web",
    handoff_description="Agente que faz busca na web",
    instructions="Você faz busca na web e retorna os resultados.",
    tools=[
        WebSearchTool()
    ]
)

triage_agent = Agent(
    name="Agente de Triagem",
    instructions="Você define qual agente chamar de acordo com a pergunta.",
    handoffs=[history_tutor_agent, math_tutor_agent, web_search_agent]
)

async def main():
    result = await Runner.run(triage_agent, "Quais as notícias na web sobre Inteligência Artificial?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())