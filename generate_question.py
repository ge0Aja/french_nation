import os
import re


question_number_regex = re.compile(r"^(\d+).")

questions = []
for file in os.listdir("questions"):
    with open(os.path.join("questions", file), "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("###"):
                line = line[3:].replace("\\", "").strip()
                questions.append(line)


sorted_questions = sorted(questions, key=lambda x: int(re.search(question_number_regex, x).group(1)) if re.search(question_number_regex, x) else 0)

with open("questions.txt", "w") as f:
    for question in sorted_questions:
        f.write(question + "\n")
