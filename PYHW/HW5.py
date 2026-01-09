# Create sets of students
frontend_students = {"Alice", "Bob", "Charlie", "Diana"}
backend_students = {"Charlie", "Diana", "Ethan", "Fiona"}

# Add a new student to Backend
backend_students.add("George")

# Remove a student from Frontend
frontend_students.remove("Bob")

# Students enrolled in both courses
both_courses = frontend_students & backend_students

# Students enrolled only in Backend
backend_only = backend_students - frontend_students

# Total number of unique students
total_unique_students = len(frontend_students | backend_students)

# Create a dictionary of course enrollments
course_enrollments = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

# Print each course with number of students
for course, count in course_enrollments.items():
    print(f"{course}: {count} students")

# Dictionary comprehension to add Fullstack course
course_enrollments_with_fullstack = {
    **course_enrollments,
    "Fullstack": sum(course_enrollments.values())
}

# Output results
print("\nStudents in both courses:", both_courses)
print("Students only in Backend:", backend_only)
print("Total unique students:", total_unique_students)
print("Updated course enrollments:", course_enrollments_with_fullstack)
