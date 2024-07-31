import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URLs for the API
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    
    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Filter completed and total tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_tasks = todos_data
    
    # Display the results
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(total_tasks)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")

