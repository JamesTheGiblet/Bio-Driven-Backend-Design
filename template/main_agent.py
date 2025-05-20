from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from reviewer import review_architecture
from layout_generator import generate_bio_layout
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4")

tools = [
    Tool(
        name="SystemStructureGenerator",
        func=generate_bio_layout,
        description="Generates a bio-inspired backend layout from goals"
    ),
    Tool(
        name="ArchitectureReviewer",
        func=review_architecture,
        description="Evaluates architecture and gives bio-analogy feedback"
    ),
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

if __name__ == "__main__":
    query = input("Describe your system or request: ")
    response = agent.run(query)
    print(response)