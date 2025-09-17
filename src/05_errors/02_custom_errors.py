class MyCustomError(TypeError):
    def __init__(self, message, code):
        self.code = code
        error_message = f"""Error code {code}: 
{message}"""
        super().__init__(error_message)
        
raise MyCustomError('OUCH! An error happened.', 500)
