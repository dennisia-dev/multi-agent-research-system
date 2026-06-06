from agents.research_agent import ResearchAgent

def main():
    agent = ResearchAgent()

    print("\nMulti-Agent Research System (Planner + Tools + Memory + Critic)")
    print("Type 'exit' to quit\n")

    while True:
        query = input("\nAsk a question: ")

        if query.lower() == "exit":
            print("Goodbye 👋")
            break

        print("\n" + "=" * 80)

        try:
            result = agent.run(query)

            print("\nFINAL REPORT\n")
            print(result)

        except Exception as e:
            print("\n❌ Error occurred:")
            print(str(e))

        print("\n" + "=" * 80)


if __name__ == "__main__":
    main()