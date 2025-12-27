# make a todo list 
class todolist:
    
    def __init__(self , filename = 'tasks.txt'):
        self.filename = filename
        self.task = self.load_task()
        
    def load_task(self):
        task = []
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    task.append(line.strip())
        except FileNotFoundError:
            task = []
        return task
        
    def save_task(self):
        
        with open(self.filename, 'w') as f:
            for t in self.task:
                f.write(t + "\n")
    
    def add_task(self, task):
        self.task.append(task)
        self.save_task()
        print('task added✔️')
        
    def remove_task(self, num):
        if 1 <= num <= len(self.task):
            removed = self.task.pop(num-1)
            self.save_task()
            print(f'Task "{removed}" removed ✔️')
        else:
            print('Task not found!!!')
    
    def show_task(self):
        if not self.task:
            print('no task have been added \n')
        
        else:
            for i,t in enumerate(self.task , 1):
                print(f'{i} {t}')

todo = todolist()
print('WELCOME TO TODO LIST APP') 

while True:

    print('\n select your choice')
    print('\n 1. ADD TASK \n 2. REMOVE TASK \n 3. SHOW TASKS \n 4. EXIT\n')
    choice = input("ENTER YOUR CHOICE : ")
    
    if choice == "1":
        add = input('Enter task to add : ')
        todo.add_task(add)
    
    elif choice == "2":
        num = int(input('Enter task no to remove : '))
        todo.remove_task(num)
        
    elif choice == "3":
        todo.show_task()
            
    elif choice == "4":
        exit()
    
    else:
        print(' "ERROR" ENTER VALID CHOICE')
    