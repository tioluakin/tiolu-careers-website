from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS =[
{
  'id': '1',
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
},
{
  'id': '2',
  'title': 'Data Scientist',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
},
  {
    'id': '3',
    'title': 'Frontend Developer',
    'location': 'Lagos, Nigeria',

  },
  {
    'id': '3',
    'title': 'Backend Developer',
    'location': 'Abuja, Nigeia',
    'salary': 'N10,00,000'
  },
]
  

@app.route("/")
def hello_lashe():
   return render_template('home.html', 
                          jobs=JOBS,
                         company_name='Practical')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)















