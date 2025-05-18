import json
import os
from datetime import datetime
import re

class Task:
    """Klase, kas reprezentē vienu uzdevumu"""
    def __init__(self, description, priority, deadline, completed=False):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = completed
    
    def to_dict(self):
        """Pārveido uzdevumu vārdnīcas formātā"""
        return {
            'description': self.description,
            'priority': self.priority,
            'deadline': self.deadline.strftime('%Y-%m-%d'),
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """Izveido uzdevumu no vārdnīcas datu struktūras"""
        deadline = datetime.strptime(data['deadline'], '%Y-%m-%d').date()
        return cls(data['description'], data['priority'], deadline, data['completed'])

class TaskPlanner:
    """Klase uzdevumu pārvaldīšanai"""
    def __init__(self, storage_file='tasks.json'):
        self.tasks = []
        self.storage_file = storage_file
        self.load_tasks()
    
    def add_task(self, description, priority, deadline):
        """Pievieno jaunu uzdevumu sarakstam"""
        task = Task(description, priority, deadline)
        self.tasks.append(task)
        self.save_tasks()
    
    def mark_task_as_completed(self, task_index):
        """Atzīmē uzdevumu kā pabeigtu"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, task_index):
        """Dzēš uzdevumu no saraksta"""
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
            return True
        return False
    
    def get_tasks_sorted_by_priority(self):
        """Atgriež uzdevumus, sakārtotus pēc prioritātes"""
        return sorted(self.tasks, key=lambda x: x.priority)
    
    def get_tasks_sorted_by_deadline(self):
        """Atgriež uzdevumus, sakārtotus pēc termiņa"""
        return sorted(self.tasks, key=lambda x: x.deadline)
    
    def save_tasks(self):
        """Saglabā uzdevumus failā"""
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=2)
    
    def load_tasks(self):
        """Ielādē uzdevumus no faila"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    task_data = json.load(f)
                    self.tasks = [Task.from_dict(data) for data in task_data]
            except (json.JSONDecodeError, FileNotFoundError):
                self.tasks = []
    
    def display_tasks(self, sort_by='priority'):
        """Parāda uzdevumu sarakstu konsolē"""
        if not self.tasks:
            print("\nUzdevumu saraksts ir tukšs.")
            return
            
        if sort_by == 'priority':
            tasks = self.get_tasks_sorted_by_priority()
        else:
            tasks = self.get_tasks_sorted_by_deadline()
        
        print("\nUzdevumu saraksts:")
        for i, task in enumerate(tasks):
            status = "✓" if task.completed else " "
            deadline = task.deadline.strftime('%d.%m.%Y')
            print(f"{i+1}. [{status}] {task.description} (Prioritāte: {task.priority}, Termiņš: {deadline})")

def parse_date(date_str):
    """Pārveido datuma tekstu datuma objektā"""
    if not date_str:
        raise ValueError("Datums ir obligāts!")
    
    normalized = re.sub(r'[\s\-/]', '.', date_str.strip())
    parts = [p for p in normalized.split('.') if p]
    
    if len(parts) < 2 or len(parts) > 3:
        raise ValueError("Izmantojiet formātu D.M.GGGG vai D.M")
    
    current_year = datetime.now().year
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2]) if len(parts) == 3 else current_year
    except ValueError:
        raise ValueError("Dienai, mēnesim un gadam jābūt skaitļiem")
    
    if month < 1 or month > 12:
        raise ValueError("Mēnesim jābūt no 1 līdz 12")
    
    max_day = 31
    if month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        max_day = 29 if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) else 28
    
    if day < 1 or day > max_day:
        raise ValueError(f"Nederīga diena {month}. mēnesim. Maksimums: {max_day}")
    
    return datetime.strptime(f"{year}-{month:02d}-{day:02d}", '%Y-%m-%d').date()

def get_valid_input(prompt, validator, error_msg=None):
    """Iegūst derīgu lietotāja ievadi"""
    while True:
        try:
            value = input(prompt).strip()
            return validator(value)
        except ValueError as e:
            print(f"Kļūda: {e}")
            if error_msg:
                print(error_msg)

def validate_description(description):
    """Pārbauda, vai uzdevuma apraksts ir derīgs"""
    if not description:
        raise ValueError("Apraksts nevar būt tukšs")
    return description

def validate_priority(priority_str):
    """Pārbauda, vai prioritāte ir derīga"""
    try:
        priority = int(priority_str)
        if priority < 1 or priority > 10:
            raise ValueError("Prioritātei jābūt no 1 līdz 10")
        return priority
    except ValueError:
        raise ValueError("Prioritātei jābūt veselam skaitlim no 1 līdz 10")

if __name__ == "__main__":
    planner = TaskPlanner()
    
    while True:
        print("\nIzvēlne:")
        print("1. Pievienot uzdevumu")
        print("2. Parādīt uzdevumus (pēc prioritātes)")
        print("3. Parādīt uzdevumus (pēc termiņa)")
        print("4. Atzīmēt uzdevumu kā pabeigtu")
        print("5. Dzēst uzdevumu")
        print("6. Iziet")
        
        choice = input("Izvēlieties darbību: ")
        
        if choice == "1":
            try:
                description = get_valid_input(
                    "Uzdevuma apraksts: ",
                    validate_description
                )
                
                priority = get_valid_input(
                    "Prioritāte (1-10): ",
                    validate_priority,
                    "Ievadiet skaitli no 1 līdz 10"
                )
                
                deadline = get_valid_input(
                    "Termiņš (D.M.GGGG vai D.M): ",
                    parse_date,
                    "Piemērs: 15.12.2023 vai 1.1 (pašreizējam gadam)"
                )
                
                planner.add_task(description, priority, deadline)
                print("Uzdevums veiksmīgi pievienots!")
                
            except Exception as e:
                print(f"Notika kļūda: {e}")
                continue
        
        elif choice == "2":
            planner.display_tasks('priority')
        
        elif choice == "3":
            planner.display_tasks('deadline')
        
        elif choice == "4":
            planner.display_tasks('priority')
            try:
                idx = int(input("Uzdevuma numurs atzīmēšanai: ")) - 1
                if planner.mark_task_as_completed(idx):
                    print("Uzdevums atzīmēts kā pabeigts!")
                else:
                    print("Nederīgs uzdevuma numurs")
            except ValueError:
                print("Lūdzu, ievadiet derīgu skaitli")
        
        elif choice == "5":
            planner.display_tasks('priority')
            try:
                idx = int(input("Uzdevuma numurs dzēšanai: ")) - 1
                if planner.delete_task(idx):
                    print("Uzdevums dzēsts!")
                else:
                    print("Nederīgs uzdevuma numurs")
            except ValueError:
                print("Lūdzu, ievadiet derīgu skaitli")
        
        elif choice == "6":
            print("Paldies, ka izmantojāt Uzdevumu plānotāju!")
            break
        
        else:
            print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")
