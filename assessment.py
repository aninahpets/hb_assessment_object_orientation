class Student(object):
    def __init__ (self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    def __init__ (self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question
        answer = raw_input('>   ')
        if answer == self.correct_answer:
            return True
        return False


class Exam(object):
    def __init__ (self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        question = Question(question, correct_answer)
        self.questions.append(question)

    def administer(self, student):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        return score


class Quiz(Exam):
    def administer(self, student):
        score = super(Quiz, self).administer(student)
        if score * 2 >= len(self.questions):
            return True
        return False


def take_test(exam, student):
    student.score = exam.administer(student)


def example():
    midterm = Exam("Midterm")
    midterm.add_question("What color is the sky?", "Blue")
    midterm.add_question("What sport does Roger Federer play?", "Tennis")
    midterm.add_question("Are whales mammals?", "Yes")
    suzystudent = Student("Suzy", "Smith", "123 Main Street")
    take_test(midterm, suzystudent)
    return suzystudent.score
