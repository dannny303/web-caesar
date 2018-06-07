from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto; 
                width: 540 px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height:12-px;
            }
        </style>
    </head>
    <body>
        <form class="caesar", action="/, method['post']>
            <lable for = "rot">Rotate by:</lable>
            <input type="text name" placeholder="0"/>
            <textarea name="text"></textarea>
            <input type = "submit"/>
           
        </form>

    </body>
</html>

"""

@app.route("/")

def index ():
    return form

app.run()