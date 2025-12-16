# to-do-chatbot
## 1. **Problem Statement**
 Managing daily tasks efficiently is a common challenge. Many people need a simple and interactive way to keep track of their tasks without using complex applications or external tools. The objective of this project is to design and implement a command-line based To-Do List Chatbot using Python that allows users to manage tasks through conversational commands.
 
 ## 2. Problem Understanding
   The problem requires building a chatbot that:
  
  *  Accepts user input in text form*
  *  Understands simple commands
  *  Maintains a list of tasks
   *  Allows tasks to be added, viewed, and marked as completed
  *  Runs continuously until the user exits

The system should be easy to use, interactive, and lightweight, making it suitable for beginners learning Python and basic chatbot logic.


## 3. Approach Used
  The project is implemented using an Object-Oriented Programming (OOP) approach in Python.
  key ideas:
 *   A class is used to encapsulate chatbot behavior
*  Tasks are stored in a list of dictionaries
*   Each task contains a description and a completion status
*   User commands are processed using conditional statements and string parsing
## 4. Logic and Implementation
  @ data structure
  *  *task are stored as*

         {"task": "Task description", "done": False}
  @ core functionalities
 *   Add Task: Appends a new task to the list
*  Show Tasks: Displays all tasks with completion status
*  Mark Task as Done: Updates task status using index
*  Chat Loop: Continuously listens for user input until exit
  
 @ Implementation Highlights
*  Uses while True loop for continuous interaction
*  Uses enumerate() to number tasks
*  Error handling ensures invalid inputs do not crash the program
*   Clean command-based interaction (add, show, done, exit)
## 4. Innovation
*  Chatbot-style interaction instead of traditional menu-driven programs
*  Visual task status using emojis (✅ / ❌)
*  Beginner-friendly design with clear commands
*  Modular methods improve readability and future extensibility
## 5. sample output
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/9170a2e0-de85-40a7-8217-c8b7bdebe0ea" />

## 6. Challenges Faced
* Handling invalid user inputs gracefully
*  Managing task indexing (user input vs list index)
*  Keeping the chatbot responsive and error-free
*  Designing a simple yet effective command parser
*  Designing a continous chatbot loop
*  ensuring clarity in user interaction

These challenges were addressed using exception handling, input validation, and structured programming. 

## 7. Conclusion
The Simple To-Do List Chatbot successfully demonstrates how Python can be used to build an interactive, real-world application using basic programming concepts. This project strengthens understanding of:
* Object-Oriented Programming
* Lists and dictionaries
*  User input handling
*  Control flow and logic building

It serves as a strong foundation for more advanced chatbot systems and can be extended with features such as file storage, natural language processing, or graphical interfaces. 
