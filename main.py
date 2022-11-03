from flask import Flask,request
from datetime import datetime

app=Flask('my first application')

@app.route('/')
def index():
    return """
    <h1> NLP Fellowship</h1>
    <h2>My Name is Martine Grace</h2>
    <p> Questions, comments or improvements? Please create an issue on Github, tweet at @corydolphin or send me an email.
     I do my best to include every contribution proposed in any way that I can.</p>"""

@app.route('/contacts')
def contacts():
    return 'do you need my contact panda'
@app.route('/date')
def datepage():
    date=str(datetime.now())
    return f'to day is {date}' 
@app.route('/birthdaytime',methods=['GET','POST'])
def calc_brithdaytime():
    if request.method == 'POST':
          return f"""
        <form ation='/birthdaytime' method='POST'>
            <input type="number"  name="birthdaytime" placeholder="Birthyear eg 2020">
            <button type="submit">submit</button>
        </form>
        From  your submission  age is  {2022 - int(request.form.get('birthdaytime'))}"""
    elif request.method == 'GET':
        return"""
        <form method='POST' action='/birthdaytime'>
           <input type="number" name='birthdaytime' placeholder="number of ages"/>
          <input type="submit" value="submit" />
        </form>"""

if __name__ == '__main__':
        app.run()

 