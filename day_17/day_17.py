class SafeFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
            self.file = open(self.filename, self.mode)
            print(f"Opened file: {self.filename}")
            return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("File closed safely.")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False
    

with SafeFileHandler('text.txt','w') as f:
     f.write('hello!')
     