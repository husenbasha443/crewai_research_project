from numpy.testing._private.utils import verbose
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
 
@CrewBase
class ResearchBlog():
    """ResearchBlog crew"""

    agents:List[BaseAgent]
    tasks:List[Task]

    ###Define the Config paths
    agents_config = "config/agents_config.yaml"
    tasks_config = "config/tasks_config.yaml"

    ### Define the agents
    @agent
    def report_generator(self)->Agent:
        return Agent(
            config = self.agents_config["report_generator"]
        )
    @agent
    def blog_writer(self)->Agent:
        return Agent(
            config = self.agents_config["blog_writer"]
        )

    ### Define the tasks
    @task
    def report_task(self)->Task:
        return Task(
            config=self.tasks_config["report_task"]
        )
    @task
    def blog_writing_task(self)->Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file = "outputs/interview_questions.md"

        )

    ### Define the Crew

    @crew
    def crew(self)->Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True,
            tracing=True
        )