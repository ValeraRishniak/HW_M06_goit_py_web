SELECT teachers.firstname AS firstname,
    teachers.lastname AS lastname,
    subjects.subject AS subject
FROM
    teachers AS teachers
    LEFT JOIN subjects AS subjects ON teachers.id = subjects.teacher_id
WHERE teachers.id = 3