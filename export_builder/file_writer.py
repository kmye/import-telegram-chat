import time
from shutil import make_archive

class FileWriter:
    def __init__(self, messages):
        self.output_messages = messages
        self.base_name = time.strftime("%Y%m%d%H%M%S")
        self.file_name = "exports/" + self.base_name + ".txt"

    def write(self):
        f = open(self.file_name, "w")
        for message in self.output_messages:
            f.write(message)
        f.close()

        make_archive(self.base_name, 'zip', root_dir='.', base_dir='backups')