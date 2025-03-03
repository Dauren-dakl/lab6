import os

def delete_file(path):

    if not os.path.exists(path):
        print(f"Файл {path} не существует.")
        return


    if not os.access(path, os.W_OK):
        print(f"Нет доступа к записи в файл {path}.")
        return


    try:
        os.remove(path)
        print(f"Файл {path} успешно удален.")
    except Exception as e:
        print(f"Произошла ошибка при удалении файла {path}: {e}")


specified_path = "/path/to/your/file"

delete_file(specified_path)