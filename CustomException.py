class DemoException(Exception):
    def __init__(self, code=0, message=''):
        self.message = message
        self.code = code
        
    def __str__(self):
        return f'{self.code} -> {self.message}'
        
message = "Exception Triggered! Something went wrong."
raise DemoException(code=101, message='test again')
