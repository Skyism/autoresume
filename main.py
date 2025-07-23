from agent import Agent
from time import sleep
def execute(agent):

    prompt = agent.format_prompt()
    response = agent.generate_response(prompt)
    agent.save_response(response)
    print(f"Response saved to results")

    print("Done!")

    print("Would you like to optimize another resume? If so, go to resume.tex and change the job description and type y. (y/n)")
    if input() == "y":
        execute(agent)
    else:
        print("Goodbye!")

def main():
    agent = Agent()
    print("Generating response...")
    execute(agent)

    

if __name__ == "__main__":
    main()