# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
# list_tasks
tasks = []

# Thêm công việc
def add_task(task_name):
    tasks.append(task_name)
    print(f"Đã thêm công việc: {task_name}")

# Hiển thị danh sách công việc
def list_tasks():
    if not tasks:
        print("Không có công việc nào trong danh sách.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("---")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và Github")
    add_task("Làm bài tập thứ nhất")
    add_task("Làm bài tập thứ hai")
    list_tasks()