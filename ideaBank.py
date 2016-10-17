# ========== Functions ==========

def InputIdea:
    Ideas = []
    Ideas.append(str(input("What is your new idea: ")))
    return Ideas

def ReadFile:


def WriteFile(ideas):
    file = open("ideas.txt")
    file.write(ideas)
    file.close()


# ========== Main ==========