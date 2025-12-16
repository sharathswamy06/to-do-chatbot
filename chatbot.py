# Simple To-Do List Chatbot in Python

class ToDoChatbot:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        return f"Added: '{task}'"

    def show_tasks(self):
        if not self.tasks:
            return "Your to-do list is empty!"
        result = "Here are your tasks:\n"
        for i, t in enumerate(self.tasks, 1):
            status = "✅" if t["done"] else "❌"
            result += f"{i}. {t['task']} [{status}]\n"
        return result

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return f"Marked '{self.tasks[index]['task']}' as done ✅"
        return "Invalid task number!"

    def chat(self):
        print("Hello! I'm your To-Do Bot. Type 'help' for commands.")
        while True:
            user_input = input("You: ").strip().lower()
            if user_input == "help":
                print("Commands: add <task>, show, done <number>, exit")
            elif user_input.startswith("add "):
                task = user_input[4:]
                print(self.add_task(task))
            elif user_input == "show":
                print(self.show_tasks())
            elif user_input.startswith("done "):
                try:
                    index = int(user_input.split()[1]) - 1
                    print(self.mark_done(index))
                except:
                    print("Please enter a valid task number.")
            elif user_input == "exit":
                print("Goodbye! 👋")
                break
            else:
                print("I didn't understand. Type 'help' for commands.")

if __name__ == "__main__":
    bot = ToDoChatbot()
    bot.chat()