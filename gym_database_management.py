import mysql.connector

# Function to establish connection to the MySQL database
def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="hhouston823",
        password="Hous0374!",
        database="gym_database"
    )
    return connection

# Task 1: Add a Member
def add_member(id, name, age, trainer_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # SQL query to insert a new member into the Members table
        insert_query = "INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (id, name, age, trainer_id))
        connection.commit()
        print("Member added successfully!")
    except mysql.connector.Error as error:
        print("Failed to add member:", error)
    finally:
        if connection:
            connection.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # SQL query to insert a new workout session into the WorkoutSessions table
        insert_query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (member_id, date, duration_minutes, calories_burned))
        connection.commit()
        print("Workout session added successfully!")
    except mysql.connector.Error as error:
        print("Failed to add workout session:", error)
    finally:
        if connection:
            connection.close()

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # SQL query to update the age of a member
        update_query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(update_query, (new_age, member_id))
        if cursor.rowcount == 0:
            print("Member not found!")
        else:
            connection.commit()
            print("Member age updated successfully!")
    except mysql.connector.Error as error:
        print("Failed to update member age:", error)
    finally:
        if connection:
            connection.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # SQL query to delete a workout session based on session ID
        delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(delete_query, (session_id,))
        if cursor.rowcount == 0:
            print("Session ID not found!")
        else:
            connection.commit()
            print("Workout session deleted successfully!")
    except mysql.connector.Error as error:
        print("Failed to delete workout session:", error)
    finally:
        if connection:
            connection.close()

# Main function to test the implemented functions
def main():
    # Testing the functions
    add_member(1, 'John Doe', 30, 101)
    add_workout_session(1, '2024-06-01', 60, 300)
    update_member_age(1, 31)
    delete_workout_session(1)

if __name__ == "__main__":
    main()