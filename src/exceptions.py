import sys

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        _, _, exc_tb = sys.exc_info()
        module_name = exc_tb.tb_frame.f_code.co_filename #if exc_tb else "Unknown"
        line_no = exc_tb.tb_lineno #if exc_tb else "Unknown"
        self.error_message = f'An error occurred in module {module_name} at line {line_no},error message: {error_message} '
    
    def __str__(self):
        return self.error_message   


if __name__ == "__main__":
    try:
        print(1 / 0)
    except Exception as e:
        raise CustomException(str(e))