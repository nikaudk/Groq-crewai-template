import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks
from google.colab import userdata

# Set up environment variables
os.environ["GROQ_API_KEY"] = "userdata.get('GROQ_API_KEY')

class BusinessAutomationCrew:
    def __init__(self, business_type):
        self.business_type = business_type
        self.agents = CustomAgents()
        self.tasks = CustomTasks()

    def run(self):
        agents = {
            "market_analyst": self.agents.create_agent("Market Analyst"),
            "marketing_strategist": self.agents.create_agent("Marketing Strategist")
        }

        tasks = {
            "market_analysis": self.tasks.create_task(agents["market_analyst"], self.business_type, "market_analysis"),
            "marketing_strategy": self.tasks.create_task(agents["marketing_strategist"], self.business_type, "marketing_strategy"),
            "integration": self.tasks.create_task(agents["marketing_strategist"], self.business_type, "integration")
        }

        crew = Crew(
            agents=list(agents.values()),
            tasks=list(tasks.values()),
            verbose=False
        )

        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Business Automation Crew Setup")
    print("------------------------------------------------")
    business_type = input("What business do you seek to build today? ").strip()

    automation_crew = BusinessAutomationCrew(business_type)
    business_plan = automation_crew.run()

    print("\n\n########################")
    print("## Here are the results of your business automation project:")
    print("########################\n")
    print(business_plan)
