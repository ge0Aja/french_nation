import os
import openai


# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_answer(question):
    """Query OpenAI API to get an answer for the given question."""
    try:
        response = openai.completions.create(
            model="gpt-4o-mini",
            prompt=question,
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    # Read questions from the file
    with open("questions.txt", "r") as f:
        lines = f.readlines()
        questions = [line.strip() for line in lines if line.strip()]
    
    # Generate answers for each question
    answers = {}
    for i, question in enumerate(questions):
        print(f"Processing question {i + 1}: {question}")
        answer = get_answer(question)
        answers[question] = answer
        print(f"Answer: {answer}\n")
        break
    
    # Save answers to a file
    with open("answers.txt", "w") as f:
        for question, answer in answers.items():
            f.write(f"Q: {question}\nA: {answer}\n\n")

if __name__ == "__main__":
    main()
