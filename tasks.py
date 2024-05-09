from crewai import Task

class CustomTasks:
    def __init__(self):
        pass

    def create_task(self, agent, business_type, task_type):
        task_descriptions = {
            "market_analysis": (
                f"Conduct an in-depth market analysis for a {business_type}, focusing on understanding market size, "
                f"identifying current trends, analyzing competitor strategies, and evaluating customer demographics. "
                f"Assess the regulatory environment and potential barriers to entry that might affect the launch and "
                f"sustainability of the business."
            ),
            "marketing_strategy": (
                f"Develop a detailed marketing strategy for a {business_type} using the insights gained from the "
                f"market analysis. This strategy should outline targeted marketing channels, customer engagement plans, "
                f"brand positioning, and promotional tactics. Include a budget forecast and expected impacts on market penetration."
            ),
            "integration": (
                f"Create a comprehensive 30-day launch plan for a {business_type} that delineates daily activities, "
                f"strategic objectives, and operational requirements. Ensure the plan includes a timeline for each phase "
                f"of the launch, identifies key milestones, and outlines resource allocation to establish a roadmap for "
                f"a successful market entry."
            )
        }

        expected_outputs = {
            "market_analysis": (
                f"Detailed report on the market conditions for a {business_type}, including data on market size, growth potential, "
                f"key competitors, and customer profiles. The report should also provide actionable insights and strategic recommendations."
            ),
            "marketing_strategy": (
                f"Comprehensive marketing playbook for a {business_type}, detailing all marketing efforts, channel strategies, "
                f"and communication plans along with a schedule and projected outcomes. The playbook should align with the business's "
                f"overall objectives and customer acquisition targets."
            ),
            "integration": (
                f"A fully articulated 30-day launch plan for a {business_type} with clear action items, responsibilities, "
                f"and checkpoints. The plan should cover all necessary preparations for the business to commence operations "
                f"smoothly and achieve early traction."
            )
        }

        return Task(
            description=task_descriptions[task_type],
            agent=agent,
            expected_output=expected_outputs[task_type]
        )
