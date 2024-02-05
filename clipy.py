"""

pyclipboard

2024 maschhoff github.com/maschhoff

"""

from flask import Flask, redirect, render_template, request
import logging
import jdb
import random

app = Flask(__name__)


@app.route('/')
def shorti():
	return render_template('layout.html')

@app.route('/', methods=['POST'])
def shorti_save():
	short=request.form['short']
	db=jdb.loadDB()
	if short.isdigit():
		return redirectit(short)
	else:
		#if "http" not in short:
	#		short=""+short
		dbdict=db["shortlinks"]
		r = random.randint(1111,9999)
		logging.info("adding "+str(r)+" with "+short+" to db")
		dbdict[r]=short
		jdb.writeDB(db)
		return render_template('layout.html', message="Link saved: "+str(r), shorturl=request.base_url+str(r))

@app.route('/<string:short>')
def shorts(short):
	return redirectit(short)
	
@app.route('/api/<string:short>')
def shortsapi(short):

	db=jdb.loadDB()

	if short in db["shortlinks"].keys():
		return '{"cliptext":"'+db["shortlinks"].get(short)+'"}'
	else:
		return ""

def redirectit(short):
	#loadDB
	logging.info("load DB")
	db=jdb.loadDB()

	if short in db["shortlinks"].keys():
		logging.info("expose entry from "+db["shortlinks"].get(short))
		#return redirect(db["shortlinks"].get(short), code=302)
		return render_template('layout.html', message=db["shortlinks"].get(short), shorturl=db["shortlinks"].get(short))
	else:
		logging.error("no entry for that short")
		return render_template('layout.html', message="no entry saved for that shortcode")
	


if __name__ == '__main__':
	logging.basicConfig(filename='server.log',level=logging.INFO)

	#Server start
	logging.info("start Shortipy server...")
	print("start Shortipy server...")
	print(""" 
	
pyclipboard

	""")

	app.run(host='0.0.0.0',port=4321,debug=False)
