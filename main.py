from user_crud import *
from task_crud import *

print('Все пользователи: ', get_users())

while True:
    print(f'\n1. Добавить задачу. \n'
          f'2. Показать все задачи. \n'
          f'3. Обновить задачу. \n'
          f'4. Удалить задачу. \n'
          f'0. Выход.\n')
    action = int(input("Действие: "))
    if action == 1:
        print("Добавление задачи")
        title = input(str("Title: "))
        description = input(str("Description: "))
        status = input(str("Status (todo, in_progress, done): "))
        new_task = create_task(title=title, description=description, status=status, user_id=11)
    elif action == 2:
        print("Все задачи: ", get_all_tasks())
    elif action == 3:
        print("Обновление задачи")
        title = input(str("Title: "))
        description = input(str("Description: "))
        update_task(task_id=new_task, title="Python", description="Нужно сделать CRUD для tasks")
    elif action == 4:
        print("Удаление задачи")
        delete_task(new_task)
    elif action == 0:
        break