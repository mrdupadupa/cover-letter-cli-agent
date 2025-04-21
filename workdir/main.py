# This script generates a cover letter using a language model and saves it to a file.
import os
import time
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits import FileManagementToolkit

# Load environment variables from .env file
load_dotenv()

# Configuration
proxy_endpoint = os.getenv("PROXY_ENDPOINT")
api_key = os.getenv("OPENAI_API_KEY")
model_name= os.getenv("MODEL_NAME")

# Initialize LLM
llm = ChatOpenAI(api_key=api_key, base_url=proxy_endpoint, model=model_name, temperature=0, verbose=False)

# Load configuration
def load_config():
    config_path = os.path.join(os.getcwd(), 'prompts', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Load prompt templates
def load_prompt_template(template_name):
    template_path = os.path.join(os.getcwd(), 'prompts', f'{template_name}.md')
    with open(template_path, 'r') as file:
        return file.read()


# Initialize file management toolkit
tools = FileManagementToolkit(
    root_dir=str("/workspace/cover_letters"),
    selected_tools=["read_file", "write_file", "list_directory"],
).get_tools()
write_tool = tools[1]
print(f"Selected tool: {write_tool}")

# Initialize agent with the write tool
self_ask_with_search = initialize_agent(
    [write_tool], llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True, verbose=True
)

config = load_config()
loaded_template = load_prompt_template('cover_letter_template')

# Create a prompt template
# PromptTemplate is a class that helps in creating prompts for LLMs
# It takes a template string and formats it with the provided arguments
prompt = PromptTemplate.from_template(loaded_template)

prepared_promt = prompt.format(
    candidate_name=config['candidate']['name'],
    candidate_email=config['candidate']['email'],
    candidate_phone=config['candidate']['phone'],
    candidate_address=config['candidate']['address'],
    date=time.strftime("%d-%m-%Y"),
    position=config['company']['position'],
    company_name=config['company']['name'],
    requirements=config['company']['requirements'],
    years_experience=config['candidate']['years_experience'],
    field = config['company']['field'],
    skills = config['candidate']['highlight_skills'],
    max_length=config["templates"]["cover_letter"]["max_length"]
    )


self_ask_with_search.run(prepared_promt)
