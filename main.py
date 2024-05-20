import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks
from google.colab import userdata

#### Run in colab cells
# import os
# from google.colab import userdata
# Set up environment variables
#os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY') #userdata.get('GROQ_API')

class DnDAdventureCrew:
    def __init__(self, campaign_setting, campaign_theme, characters):
        self.campaign_setting = campaign_setting
        self.campaign_theme = campaign_theme
        self.characters = characters
        
        self.agents = CustomAgents()
        self.tasks = CustomTasks()

    def run(self):
        agents = {
            "leadwriter": self.agents.create_agent("Lead Dnd Writer"),
            "characterspecialist": self.agents.create_agent("Character Specialist"),
            "npcspecialist": self.agents.create_agent("NPC Specialist"),
            "encounterdesigner": self.agents.create_agent("Encounter Designer"),
            "worldbuilder": self.agents.create_agent("World Builder"),
            "mainquestdesigner": self.agents.create_agent("Main quest Designer"),
            "sidequestdesigner": self.agents.create_agent("Sidequest Designer")
        }

        tasks = {
            "world_building": self.tasks.create_task(agents["world_builder"], self.campaign_setting, self.campaign_theme, self.characters, "world_building"),
            "characterintegration": self.tasks.create_task(agents["characterspecialist"], self.campaign_setting, self.campaign_theme, self.characters,"characterintegration"),
            "encounterdesigning": self.tasks.create_task(agents["encounterdesigner"], self.campaign_setting, self.campaign_theme, self.characters, "encounterdesigning"),
            "npcdevelopment": self.tasks.create_task(agents["npcspecialist"], self.campaign_setting, self.campaign_theme, self.characters, "npcdevelopment"),
            "side_quest_design": self.tasks.create_task(agents["sidequestdesigner"], self.campaign_setting, self.campaign_theme, self.characters, "side_quest_design"),
            "main_quest_design": self.tasks.create_task(agents["mainquestdesigner"], self.campaign_setting, self.campaign_theme, self.characters, "main_quest_design"),
            "campaignwriting": self.tasks.create_task(agents["leadwriter"], self.campaign_setting, self.campaign_theme, self.characters, "campaignwriting")
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
    campaign_setting = input("Provide a brief overview of the campaign setting, including the world, its history, and any relevant factions or organizations.").strip()
    campaign_theme = input("Specify the desired tone and themes for the adventure (e.g., light-hearted, dark and gritty, humorous, etc.)").strip()
    characters = input("hare the players' character concepts, backstories, and personalities to help the crew tailor the adventure to their strengths and weaknesses.").strip()
    
    automation_crew = DnDAdventureCrew(campaign_setting, campaign_theme, characters)
    dnd_adventur = automation_crew.run()

    print("\n\n########################")
    print("## Here are the results of your business automation project:")
    print("########################\n")
    print(dnd_adventur)
