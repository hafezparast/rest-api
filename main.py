from flask import Flask,render_template
from flask_restful import Api, Resource
from flask_cors import CORS

# here you can import diffrent packages can be year or grade
from questions import algebra

app = Flask(__name__)
CORS(app)
api = Api(app)

names = {
    "question": algebra.A_math_question,
    "q2": algebra.find_x_angel_in_qualdrilateral,
    "q3": algebra.simple_equation,
    "q4": algebra.sym_equation
}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]()

    def post(self):
        return {"data": "Posted"}


api.add_resource(HelloWorld, "/helloworld/<string:name>")

@app.route('/')
def index():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
