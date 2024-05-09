import os
from crewai import Agent
from langchain_groq import ChatGroq

class CustomAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768",
        )
    def create_agent(self, role):
        descriptions = {
            "Market Analyst": "I specialize in market research and analysis, providing insights that are crucial for strategic planning.",
            "Marketing Strategist": "I develop marketing strategies that effectively target key demographics and maximize market penetration."
        }

        return Agent(
            role=role,
            backstory=descriptions[role],
            goal=f"Develop detailed, actionable insights for {role}.",
            verbose=True,
            llm=self.llm,
            max_rpm=29,
        )
