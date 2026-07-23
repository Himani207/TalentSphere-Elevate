import sqlite3

DB_NAME = "talentsphere.db"


# ---------------------------------------
# Database Connection
# ---------------------------------------
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------------------
# Save Student Profile
# ---------------------------------------
def save_profile(
    
    email,
    parent_email,
    age,
    class_name,
    school,
    interests,
    favorite_subject,
    dream_career,
    goals,
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT email
        FROM student_profile
        WHERE email=?
        """,
        (email,),
    )

    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE student_profile
            SET
                parent_email=?,
                age=?,
                class_name=?,
                school_name=?,
                interests=?,
                favourite_subject=?,
                dream_career=?,
                short_goal=?
            WHERE email=?
            """,
            (
                parent_email,
                age,
                class_name,
                school,
                interests,
                favorite_subject,
                dream_career,
                goals,
                email,
            ),
        )

    else:

        cursor.execute(
            """
            INSERT INTO student_profile(
                email,
                parent_email,
                age,
                class_name,
                school_name,
                interests,
                favourite_subject,
                dream_career,
                short_goal
            )
            VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                email,
                parent_email,
                age,
                class_name,
                school,
                interests,
                favorite_subject,
                dream_career,
                goals,
            ),
        )

    conn.commit()
    conn.close()


# ---------------------------------------
# Get Student Profile
# ---------------------------------------
def get_student_profile(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            email,
            parent_email,
            age,
            class_name,
            school_name,
            interests,
            favourite_subject,
            dream_career,
            short_goal
        FROM student_profile
        WHERE email=?
        """,
        (email,),
    )

    row = cursor.fetchone()

    conn.close()

    if row:

        return {
            "email": row["email"],
            "parent_email": row["parent_email"],
            "age": row["age"],
            "class": row["class_name"],
            "school": row["school_name"],
            "interests": row["interests"] if row["interests"] else "",
            "subject": row["favourite_subject"],
            "career": row["dream_career"],
            "goal": row["short_goal"],
        }

    return None
# ---------------------------------------
# Get Student By Parent Email
# ---------------------------------------
def get_student_by_parent(parent_email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            email,
            parent_email,
            age,
            class_name,
            school_name,
            interests,
            favourite_subject,
            dream_career,
            short_goal
        FROM student_profile
        WHERE parent_email=?
        """,
        (parent_email,),
    )

    row = cursor.fetchone()

    conn.close()

    if row:

        return {
            "email": row["email"],
            "parent_email": row["parent_email"],
            "age": row["age"],
            "class": row["class_name"],
            "school": row["school_name"],
            "interests": row["interests"] if row["interests"] else "",
            "subject": row["favourite_subject"],
            "career": row["dream_career"],
            "goal": row["short_goal"],
        }

    return None


# ---------------------------------------
# Get All Students
# ---------------------------------------
def get_all_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            email,
            parent_email,
            age,
            class_name,
            school_name,
            interests,
            favourite_subject,
            dream_career,
            short_goal
        FROM student_profile
        ORDER BY class_name
        """
    )

    students = cursor.fetchall()

    conn.close()

    return [
        {
            "email": student["email"],
            "parent_email": student["parent_email"],
            "age": student["age"],
            "class": student["class_name"],
            "school": student["school_name"],
            "interests": student["interests"],
            "subject": student["favourite_subject"],
            "career": student["dream_career"],
            "goal": student["short_goal"],
        }
        for student in students
    ]


# ---------------------------------------
# Total Students
# ---------------------------------------
def get_total_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM student_profile"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total