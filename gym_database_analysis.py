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

# Task 1: SQL BETWEEN Usage
def get_members_in_age_range(start_age, end_age):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # SQL query to retrieve members within the specified age range
        query = "SELECT name, age, trainer_id FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()
        if members:
            print("Members in the age range {} to {}:".format(start_age, end_age))
            for member in members:
                print("Name: {}, Age: {}, Trainer ID: {}".format(member[0], member[1], member[2]))
        else:
            print("No members found in the specified age range.")
    except mysql.connector.Error as error:
        print("Failed to retrieve members:", error)
    finally:
        if connection:
            connection.close()

# Main function to test the implemented functions
def main():
    # Testing the function
    get_members_in_age_range(25, 30)

if __name__ == "__main__":
    main()
