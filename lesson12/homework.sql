CREATE TABLE app_user (
    id SERIAL PRIMARY KEY,
    name VARCHAR (60) NOT NULL,
    email VARCHAR(60) NOT NULL UNIQUE,
    password VARCHAR (60) NOT NULL
);

CREATE TABLE test_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR (100) NOT NULL UNIQUE
);

CREATE TABLE tests (
    id SERIAL PRIMARY KEY,
    name VARCHAR (60) NOT NULL UNIQUE,
    test_category_id INTEGER references test_category(id)
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question VARCHAR (250) NOT NULL,
    test_id INTEGER references tests(id)
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER references questions(id),
    answer VARCHAR (250) NOT NULL,
    is_right_answer BOOLEAN  NOT NULL
);

CREATE TABLE user_answers (
    user_id INTEGER references app_user(id),
    question_id INTEGER references questions(id),
    answer_id INTEGER references answers(id),
    PRIMARY KEY (user_id, question_id, answer_id)
 );

INSERT INTO app_user (name, email, password)
VALUES
('first_name', 'first@gmail.com', '123'),
('second_name', 'second@gmail.com', '321'),
('third_name', 'third@gmail.com', '654');

INSERT INTO test_category (name)
VALUES
('first_test_category'),
('second_test_category');

INSERT INTO tests (name, test_category_id)
VALUES
('first_test', 1),
('second_test', 1);

INSERT INTO questions (question, test_id)
VALUES
('first_question', 1),
('second_question', 1),
('third_question', 1),
('fourth_question', 1);

INSERT INTO answers (question_id, answer, is_right_answer)
VALUES
(1, 1, FALSE),
(1, 2, TRUE),
(2, 3, TRUE),
(2, 4, FALSE),
(3, 5, FALSE),
(3, 6, TRUE),
(4, 7, TRUE),
(4, 8, FALSE);

INSERT INTO user_answers (user_id, question_id, answer_id)
VALUES
(1, 1, 2),
(1, 2, 3),
(1, 3, 6),
(1, 4, 7);
