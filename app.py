from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('SymptomsForm.html')

@app.route('/toFile', methods=['POST'])
def to_file():
    if request.method == 'POST':
        with open('symptoms.txt', 'w') as file:
            file.write("Figure out what disease or sickness the dog has based on the description of appearance.\n")
            for key, value in request.form.items():
                file.write(f"{key}: {value}\n")
        subprocess.run(["python", "diseasedetector.py"], check=True)
        return 'Form submitted successfully and data written to symptoms.txt.'

if __name__ == '__main__':
    app.run(debug=True)
