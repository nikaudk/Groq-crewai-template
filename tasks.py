from crewai import Task

class CustomTasks:
    def __init__(self):
        pass
 
    def create_task(self, agent, campaign_setting, campaign_theme, characters, task_type):
        task_descriptions = {
            "world_building": (
                f"Conduct an in-depth analysis of: {campaign_setting}." 
                f"Gather information on player count, levels and classes from {characters}."
                f"Review the text: {campaign_theme}, gather information about the theme of the adventure"
                f"Provide a brief overview of the campaign setting, including the world, its history, and any relevant factions or organizations."
                f"Specify the desired tone and themes for the adventure (e.g., light-hearted, dark and gritty, humorous, etc.)."
                f"Share bits of the players' character concepts, backstories, and personalities to help the crew tailor the adventure to their strengths and weaknesses."
            ),
            "encounterdesigning": (
                f"Specify the desired difficulty level for combat encounters, including the number and types of enemies, terrain, and environmental hazards."
                f"The encounters need to roughly match the abilities of {characters}. Encounters must be faily challenging"
            ),
            "npcdevelopment": (
                f"Introduce key NPCs, factions, and organizations that will feature prominently in the adventure."
            ),
            "side_quest_design": (
                f"Suggest potential side quests or branching storylines to add depth and variety to the adventure."
                f"Provide hints or suggestions for unexpected twists or surprises to keep the players engaged."
                f"Provide guidelines for puzzle design, exploration opportunities, and skill challenges."
            ),
            "main_quest_design": (
                f"Offer a rough outline of the main quest or storyline, including key plot points, villains, and MacGuffins."
                f"Provide hints or suggestions for unexpected twists or surprises to keep the players engaged."
            ),
            "campaignwriting": (
                f"This is the final task. You are responsible for gathering all information from the other agents in order to write the full compaign based on {campaign_setting}"
            )
        }

        expected_outputs = {
            "world_building": (
                f"Based on {campaign_setting}, {campaign_theme} and {characters}, provide a brief overview of the campaign setting, including the world, its history, and any relevant factions or organizations."
                f"Specify the desired tone and themes for the adventure (e.g., light-hearted, dark and gritty, humorous, etc.)."
                f"Share bits of the players' character concepts, backstories, and personalities to help the crew tailor the adventure to their strengths and weaknesses."
            ),
            "main_quest_design": (
                f"Based on {campaign_setting}, {campaign_theme} and {characters} wirte a storyline for the main quest."
            ),
            "encounterdesigning": (
                f"You have the following information avaliable about the campaign: {campaign_setting}, {campaign_theme} and {characters}. Create 3 to 5 encounters that fit the background information."
            ),
            "campaignwriting": (
                f"Write the full DnD adventure from {campaign_setting} and {campaign_theme} with main quest and side quest."
            )
        }

        return Task(
            description=task_descriptions[task_type],
            agent=agent,
            expected_output=expected_outputs[task_type]
        )
