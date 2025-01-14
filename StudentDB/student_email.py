import register_student

def search_student_by_email():
    if request.method == 'POST':
        student_id = request.form['student_id'].lower()