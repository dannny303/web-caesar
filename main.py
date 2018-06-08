from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                postion: center;
                background-color: #eee;
                padding: 20px;
                margin: 0 auto; 
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                postion: center;
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label> Rotate by:</label>
            <input type = "text" name="rot" placeholder="0"/>
            <br>
            <textarea name="text" placeholder="{0}"></textarea>
            <input type = "submit"/>
           
        </form>

    </body>
</html>

"""


@app.route("/")
def index ():
    return form.format('encrypt message here:')

@app.route("/encrypt", methods=['GET', 'POST'])
def encrypt ():
    rot = int(request.form['rot'])
    text = request.form['text']
    #print(text)
    #print(rot)
    caesar = rotate_string(text, rot)

    print(caesar)

    return form.format(caesar)


app.run()
