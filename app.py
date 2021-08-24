from flask import Flask, render_template
import os

app = Flask(__name__)

data_file = os.path.abspath('/home/website/custom')
#data_file = os.path.abspath('/home/dadamski/test')

lines = ""

with open(data_file, "r") as file:
    lines = file.read().replace('\n','')

@app.route("/")
def hello():
#    return "Hello world " + lines +" !"
    return render_template('/home/dadamski/flask_environment/ansible-community-example/index.html', custom_text=lines)

if __name__ == "__main__":
    app.run()
