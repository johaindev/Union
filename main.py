import questionary

projectName = questionary.text("What should the project be named:").ask()

if (projectName == "" or None):
    print("You must input a project name.")
    exit(0)

projectPath = questionary.select(
    "Where should the project be located:",
    choices=["Current", "Subfolder"]
).ask()

if (projectPath == "" or None):
    print("You must input a project path.")
    exit(0)

projectTemplate = questionary.select(
    "Select a project template",
    choices=["Node", "Discord", "Lua", "Python", "HTML, CSS, JS"]
).ask()

if (projectTemplate == "Node"):
    nodeProjectTemplate = questionary.select(
        "Select a programming language",
        choices=["JavaScript", "Typescript"]
    ).ask()

if (projectTemplate == "Discord"):
    discordProjectTemplate = questionary.select(
        "Select a programming language",
        choices=["JavaScript", "Typescript", "Python"]
    ).ask()



print("finish")