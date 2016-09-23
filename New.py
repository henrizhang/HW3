from flask import Flask, render_template
import random
import io
import csv
app=Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/occupations')
def hola():
    return render_template('Ninja.html', name="occupation", bruh=randOcc(), occs=occsRows)

f=open('occupations.csv', 'r')
file=f.read();
lines=file.splitlines()
del lines[0]
#deletes first line
prob={}
occsRows=[]


for n in  csv.reader(lines, quotechar='"', delimiter=',',
	quoting=csv.QUOTE_ALL, skipinitialspace=True):
 	a=n[0]
	b=float(n[1])
        c=[]
        c.append(a)
        c.append(b)
        occsRows.append(c)
	prob[a]=b
	#ignores comma in quotations and creates the dictionary
sorted(prob.values())
#sorts dict by value in ascending order

def randOcc():
	rand=random.randrange(0,998)
	counter=0
	for key, value in prob.iteritems():
		counter+=value*10
		#add by ascending numbers for ranges of probability
		if (rand<counter):
			return key
	return "None"



if __name__=="__main__":
    app.debug = True
    app.run()

    
