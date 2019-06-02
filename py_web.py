from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry():
  return render_template('entry.html',the_title='welcome to my first python web project')

@app.route('/search',methods=['POST'])
def search ():
  pharse = request.form['phrase']
  letter = request.form['letter']
  result = getVowel(pharse,letter)
  log_request(pharse,letter,result)
  return render_template('results.html',the_title='welcome to my first python web project',the_phrase=pharse,the_letters=letter,the_result=result)

def log_request(pharse,letter, res):
  dbconfig = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'lsf19941026@!',
    'database':'test'
  }
  con = mysql.connector.connect(**dbconfig)
  mycursor = con.cursor()
  
  _SQL = """insert into vsearchlogDB
    (phrase, letter, results)
    values (%s, %s, %s)"""

  mycursor.execute(_SQL,(
    pharse,
    letter,
    res,
   
  ))
  con.commit()
  mycursor.close()
  con.close()


def getVowel(pharses, letters):
  return ','.join(set(letters).intersection(set(pharses)))

if __name__ == "__main__":
  app.run(
  port= 5004,
  debug=True)



