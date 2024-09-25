class Memory:
    def __init__(self, max_size=5):
        self.questions = []
        self.max_size = max_size

    def add_question(self, question):
        if len(self.questions) >= self.max_size:
            self.questions.pop(0)  # Remove the oldest question
        self.questions.append(question)

    def get_memory(self):
        return self.questions
