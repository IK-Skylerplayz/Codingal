class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        return f"Hello! I am {self.name}, a {self.model} model robot. My purpose is {self.purpose}."

    def perform_task(self, task):
        return f"{self.name} is now performing the task: {task}."

class AssistantRobot(Robot):
    def __init__(self, name, model, purpose, tools):
        super().__init__(name, model, purpose)
        self.tools = tools

    def list_tools(self):
        return f"I am equipped with the following tools: {', '.join(self.tools)}."

general_robot = Robot("Robo-Alpha", "IK", "general assistance")
print(general_robot.introduce())
print(general_robot.perform_task("cleaning"))

assistant_robot = AssistantRobot("Robo-deez", "version 2", "personal assistance", ["Screwdriver", "Sensor Array"])
print(assistant_robot.introduce())
print(assistant_robot.list_tools())
print(assistant_robot.perform_task("helping with calculations"))
