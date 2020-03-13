"""Описать таблицы из lesson12/homework.sql при помощи sqlalchemy"""

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgres://ola:123@localhost:5432/shop_z25'
)


metadata = MetaData()
BaseModel = declarative_base(bind=engine)


class Users(BaseModel):
    __tablename__ = 'app_users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)

    def __str__(self):
        return f'{self.id}  {self.username}'
    __repr__ = __str__


class Tests(BaseModel):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __str__(self):
        return f'{self.id} {self.number} {self.text}'
    __repr__ = __str__


class Questions(BaseModel):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __str__(self):
        return f'{self.id} {self.number} {self.text}'
    __repr__ = __str__


class Testsquestions(BaseModel):
    __tablename__ = 'tests_questions'
    id = Column(Integer, primary_key=True)
    test_id = Column(ForeignKey('tests.id'), unique=True)
    question_id = Column(ForeignKey('questions.id'), unique=True)

    def __str__(self):
        return f'{self.id} {self.test_id} {self.question_id}'
    __repr__ = __str__


class Answers(BaseModel):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(ForeignKey('questions.id'))

    def __str__(self):
        return f'{self.id} {self.text} {self.is_correct} {self.question_id}'
    __repr__ = __str__


class UsersAnswer(BaseModel):
    __tablename__ = 'users_answers'
    id = Column(Integer, primary_key=True)
    tests_questions_id = Column(ForeignKey('tests_questions.id'), unique=True)
    user_id = Column(ForeignKey('app_users.id'), unique=True)
    answer_id = Column(ForeignKey('answers.id'))

    def __str__(self):
        return f'{self.id} {self.tests_questions_id} {self.user_id} {self.answer_id}'
    __repr__ = __str__


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

