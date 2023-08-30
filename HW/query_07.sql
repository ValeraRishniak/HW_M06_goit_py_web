SELECT students.firstname AS firstname,
    students.lastname AS lastname,
    grades.grade AS grade
FROM students AS students
    INNER JOIN grades AS grades ON students.id = grades.student_id
WHERE students.group_id = 1
    AND grades.subject_id = 2