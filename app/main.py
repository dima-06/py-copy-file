import os


def copy_file(command: str) -> None:
    names_of_files = command.strip().split(" ")
    if len(names_of_files) != 3 or names_of_files[0] != "cp":
        return
    file, new_file = names_of_files[1], names_of_files[2]
    if not os.path.exists(file):
        return
    if file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
