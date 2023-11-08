CREATE TABLE subjects (
    id_subject INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL,
    subject_description TEXT,
    hours INTEGER,
    semester_number INTEGER
);

INSERT INTO subjects (subject_name, subject_description, hours, semester_number) VALUES
    ('Математика', 'Основи математики', 60, 1),
    ('Фізика', 'Загальна фізика', 45, 1),
    ('Інформатика', 'Основи програмування', 75, 2),
    ('Історія', 'Всесвітня історія', 45, 1),
    ('Біологія', 'Основи біології', 60, 2),
    ('Хімія', 'Загальна хімія', 45, 2),
    ('Англійська мова', 'Англійська для інженерів', 60, 1),
    ('Економіка', 'Мікроекономіка', 30, 2);

SELECT subject_name, semester_number FROM subjects;
