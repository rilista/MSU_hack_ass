with open("C:\\Users\пк\Downloads\\answers (1) (1).txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
with open("C:\\Users\пк\Downloads\\answers (1) (1).txt", "w", encoding='utf-8') as f:
    for line in lines:
        if line.strip("\n") != "Выберите один или несколько ответов:":
            f.write(line)

