import os
from dotenv import load_dotenv
from litellm import completion
from crewai import Task, Crew, Agent, LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai import configure, GenerativeModel

load_dotenv()

os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY")

## Setting up LLM
llm=LLM(
    model="gemini/gemini-pro",
    verbose=True,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

## Defining a student agent
student_agent = Agent(
    role="student",
    goal="Ask popular questions about generative AI.",
    backstory="A curious student eager to learn about generative AI concepts.",
    llm=llm,
    verbose=True,
)

## Defining a teacher agent
teacher_agent = Agent(
    role="teacher",
    goal="Answer questions about generative AI in an informative manner.",
    backstory="A knowledgeable AI teacher, ready to explain generative AI concepts.",
    llm=llm,
    verbose=True,
)

## Some questions
popular_questions = [
    "What is generative AI?",
    "How does a generative adversarial network (GAN) work?",
    "What are the main applications of generative AI?",
    "What are transformers in AI?",
    "How does text generation work in models like GPT?",
    "What are diffusion models?",
    "How do AI models like DALL-E generate images?",
    "What is the difference between discriminative and generative models?",
    "How can generative AI models be fine-tuned?",
    "What are the challenges and limitations of generative AI?"
]

## Creating tasks for student agent
student_tasks = [
    Task(
        description=f"Ask question: '{question}'",
        expected_output=f"The answer to: '{question}'",
        agent=student_agent,
    )
    for question in popular_questions
]

## Creating tasks for teacher agent
teacher_tasks = [
    Task(
        description="Provide an answer to the student's question.",
        expected_output="An informative explanation of the question.",
        agent=teacher_agent,
        context=[student_task],
    )
    for student_task in student_tasks
]

##Creating a crew  
my_crew = Crew(
    agents=[student_agent, teacher_agent], 
    tasks=teacher_tasks,
    verbose=True
)

if __name__ == "__main__":
    my_crew.kickoff()
