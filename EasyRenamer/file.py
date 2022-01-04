import os


class Folder:
    def __init__(self, path: str):
        self.path = path

    def get_file_names(self) -> list:
        """Return the names of files (not the path)"""
        file_names = list()

        def search(path):
            files = os.listdir(path)
            for file in files:
                full_file_name = os.path.join(path, file)
                if os.path.isdir(full_file_name):
                    search(full_file_name)
                else:
                    file_names.append(full_file_name[(len(self.path) + 1):])

        search(self.path)

        return file_names

    def get_file_paths(self) -> list:
        """Return the paths of files"""
        return list(
            map(lambda file: os.path.join(self.path, file), self.get_file_names())
        )

    def get_folder_names(self) -> list:
        """Return the name of folders (not the path)"""
        folder_names = list()

        def search(path):
            files = os.listdir(path)
            for file in files:
                full_file_name = os.path.join(path, file)
                if os.path.isdir(full_file_name):
                    folder_names.append(full_file_name[(len(self.path) + 1):])
                    search(full_file_name)
                else:
                    continue

        search(self.path)

        return folder_names

    def get_folder_paths(self) -> list:
        """Return the paths of folders"""
        return list(
            map(lambda file: os.path.join(self.path, file), self.get_folder_names())
        )


def replace_name_order(files: list, first: int, last: int) -> None:
    for i in range(first, last + 1):
        if i - first == len(files):
            break
        path = "\\".join(files[i - first].split("\\")[:-1]) + "\\"
        ext = os.path.splitext(files[i - first].split("\\")[-1])[-1]
        path = path + str(i) + ext
        os.rename(files[i - first], path)


def replace_string(files: list, old: str, new: str) -> None:
    for file_name in files:
        path = "\\".join(file_name.split("\\")[:-1]) + "\\"
        ext = os.path.splitext(file_name.split("\\")[-1])[-1]
        name = os.path.splitext(file_name.split("\\")[-1])[0].replace(old, new)
        path = path + name + ext
        os.rename(file_name, path)
