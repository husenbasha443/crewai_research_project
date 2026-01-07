from datetime import datetime

from research_blog.crew import ResearchBlog

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Agentic AI ',
        'current_year': str(datetime.now().year)
    }

    try:
        ResearchBlog().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")