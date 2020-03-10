"""
Описать для каждой таблицы из домашки(lesson12) класс,
который позволяет взаимодействовать с конткретной таблицей

Пример:
class User:
    ...
    def get_users(user_id=None, username=None):
        ...
    def create_users(*users_list):
        ...

class Test:
    ...

и тд
"""
import psycopg2
from psycopg2.extras import execute_values


class Common:
    def __init__(self):
        self.cursor = cursor

    def get_table(self, table_name):
        self.cursor.execute("SELECT * FROM {};".format(table_name))
        return self.cursor.fetchall()


class User(Common):
    def get_user(self, user_id=None, username=None):
        if user_id:
            self.cursor.execute(
                "SELECT * FROM app_users WHERE id=%s;", (user_id,)
            )
        elif username:
            self.cursor.execute(
                "SELECT * FROM app_users WHERE username=%s;", (username,)
            )
        return self.cursor.fetchall()

    def create_users(self, *users_list):
        values = ((i,) for i in users_list)
        execute_values(
            self.cursor,
            "INSERT INTO app_users (username) VALUES %s;",
            values
        )

    def delete_user(self, user_id=None, username=None):
        if user_id:
            self.cursor.execute(
                "DELETE FROM app_users WHERE id=%s;", (user_id,)
            )
        elif username:
            self.cursor.execute(
                "DELETE FROM app_users WHERE username=%s;", (username,)
            )


class Tests(Common):
    def get_test(self, test_id=None, test_number=None):
        if test_id:
            self.cursor.execute(
                "SELECT * FROM tests WHERE id=%s;", (test_id,)
            )
        elif test_number:
            self.cursor.execute(
                "SELECT * FROM tests WHERE number=%s;", (test_number,)
            )
        return self.cursor.fetchall()

    def create_tests(self, *tests):
        insert_test = "INSERT INTO tests (number, text) VALUES %s"
        psycopg2.extras.execute_values(
            self.cursor, insert_test, tests, template=None)

    def delete_tests(self, test_id=None, test_number=None):
        if test_id:
            self.cursor.execute(
                "DELETE FROM tests WHERE id=%s;", (test_id,)
            )
        elif test_number:
            self.cursor.execute(
                "DELETE FROM tests WHERE number=%s;", (test_number,)
            )


class Questions(Common):
    def get_question(self, question_id=None, question_number=None):
        if question_id:
            self.cursor.execute(
                "SELECT * FROM questions WHERE id=%s;", (question_id,)
            )
        elif question_number:
            self.cursor.execute(
                "SELECT * FROM questions WHERE number=%s;", (question_number,)
            )
        return self.cursor.fetchall()

    def create_questions(self, *questions):
        insert_question = "INSERT INTO questions (number, text) VALUES %s"
        psycopg2.extras.execute_values(
            self.cursor, insert_question, questions, template=None)

    def delete_question(self, question_id=None, question_number=None):
        if question_id:
            self.cursor.execute(
                "DELETE FROM questions WHERE id=%s;", (question_id,)
            )
        elif question_number:
            self.cursor.execute(
                "DELETE FROM questions WHERE number=%s;", (question_number,)
            )


class Answers(Common):
    def get_answer(self, answer_id=None, question_id=None):
        if answer_id:
            self.cursor.execute(
                "SELECT * FROM answers WHERE id=%s;", (answer_id,)
            )
        elif question_id:
            self.cursor.execute(
                "SELECT * FROM answers WHERE question_id=%s;", (question_id,)
            )
        return self.cursor.fetchall()

    def create_answers(self, *answers):
        insert_answer = "INSERT INTO answers (text, is_correct, question_id) VALUES %s"
        psycopg2.extras.execute_values(
            self.cursor, insert_answer, answers, template=None)

    def delete_answer(self, answer_id=None, question_id=None):
        if answer_id:
            self.cursor.execute(
                "DELETE FROM answers WHERE id=%s;", (answer_id,)
            )
        elif question_id:
            self.cursor.execute(
                "DELETE FROM answers WHERE question_id=%s;", (question_id,)
            )


if __name__ == '__main__':
    connection = psycopg2.connect(
        dsn='postgres://ola:123@localhost:5432/shop_z25'
    )
    cursor = connection.cursor()

    my_user = User()
    my_user.create_users('inna', 'vera')
    my_user.delete_user(user_id=9)
    print(my_user.get_table('app_users'))
    print(my_user.get_user(user_id=2))
    my_tests = Tests()
    my_tests.create_tests((10, 'ten'), (11, 'eleven'))
    print(my_user.get_table('tests'))
    my_question = Questions()
    my_question.create_questions((1, 'first'), (2, 'second'))
    print(my_question.get_table('questions'))
    my_answer = Answers()
    my_answer.create_answers(('first', True, 1), ('second', False, 1))
    print(my_answer.get_table('answers'))

    connection.commit()
    connection.close()

