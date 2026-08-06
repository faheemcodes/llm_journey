import json

class TaskLogger:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, prompt_text):
        my_dict= {
            "id" : len(self.tasks) + 1,
            "prompt" : prompt_text
        }
        self.tasks.append(my_dict)
    
    def view_task(self):
        if len(self.tasks) == 0:
            message = "No tasks logged yet."
            print(message)
        else:
            for task in self.tasks:
                print(f"ID: {task['id']} | Prompt: {task['prompt']}")
    
    def save_to_file(self):
          
        try:
            task = json.dumps(self.tasks)
            with open('ai_tasks.txt', 'w') as file:
                file.write(task)
                
        except PermissionError as e:
            return e


logger = TaskLogger()

while True:
    
    print("\n=== AI TASK LOGGER CLI ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save to File")
    print("4. Exit")
    
    user_input = input("Enter any number:")
    
    if user_input == "1":
        prompt_text = input("Input your prompt text: ")
        logger.add_task(prompt_text)
        print("Task added successfully!")
        
    elif user_input == "2":
            logger.view_task()
      
    elif user_input == "3":
        logger.save_to_file()
        print("Tasks saved to ai_tasks.txt successfully!")
        
    elif user_input == "4":
        print("Exiting Task Logger. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
    
