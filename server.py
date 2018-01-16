from flask import Flask, render_template, request, redirect

app = Flask(__name__)    
                         
@app.route('/')          
                                              
def landing_page():
  return render_template('index.html', name="Seth's")

@app.route('/ninjas')

def ninjas_page():
	return render_template('ninjas.html')

@app.route('/dojos/new')

def dojos_page():
	return render_template('dojos.html')



app.run(debug=True)      