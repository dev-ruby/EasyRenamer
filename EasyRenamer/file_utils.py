import os
from enum import Enum
from typing import List, Optional


class Folder:
    def __init__(self, path: str):
        self.path = path

    def get_file_relative_paths(self) -> List[str]:
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

    def get_file_absolute_paths(self) -> List[str]:
        return list(
            map(
                lambda file: os.path.join(self.path, file),
                self.get_file_relative_paths(),
            )
        )

    def get_folder_relative_paths(self) -> List[str]:
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

    def get_folder_absolute_paths(self) -> List[str]:
        return list(
            map(
                lambda file: os.path.join(self.path, file),
                self.get_folder_relative_paths(),
            )
        )


class Filter:
    @staticmethod
    def filter_file_size(path: str) -> int:
        return os.path.getsize(path)

    @staticmethod
    def filter_time(path: str) -> float:
        return os.path.getctime(path)


class Sort:
    @staticmethod
    def sort_file_size(files: list, is_reversed: Optional[bool] = False) -> List[str]:
        return sorted(files, key=Filter.filter_file_size, reverse=is_reversed)

    @staticmethod
    def sort_file_time(files: list, is_reversed: Optional[bool] = False) -> List[str]:
        return sorted(files, key=Filter.filter_time, reverse=is_reversed)

    @staticmethod
    def sort_file_name(files: list, is_reversed: Optional[bool] = False) -> List[str]:
        return sorted(files, reverse=is_reversed)


class SortType(Enum):
    NAME = 0
    TIME = 1
    SIZE = 2
