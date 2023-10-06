# Eli Chen, Ryan Mona
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Global dictionary to store student registrations
# Key is the student name and value is their chosen organization
students = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    # List of available student organizations
    organizations = ["UNCC ITSC", "Code9"]
    
    # Handle form submission
    if request.method == 'POST':
        student_name = request.form.get('student_name')
        organization = request.form.get('organization')
        
        # Backend validation to check if student_name and organization are valid
        if not student_name or organization not in organizations:
            # Render the index page with an error if validation fails
            return render_template('index.html', organizations=organizations, error="Invalid input!")
        
        # Save the student's registration
        students[student_name] = organization
        
        # Redirect to the page showing all registered students
        return redirect(url_for('registered_students'))

    # Render the index page for GET requests or if POST submission is not yet done
    return render_template('index.html', organizations=organizations)

@app.route('/students', methods=['GET'])
def registered_students():
    # Render the page showing all registered students
    return render_template('students.html', students=students)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
