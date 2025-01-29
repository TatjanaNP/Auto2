from serializers import AutomobilisSchema
from models import db, Automobilis
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/api/automobiliai")
def api_automobiliai():
    all_cars = Automobilis.query.all()
    car_data = [{
        "id": car.id,
        "make": car.gamintojas,
        "model": car.modelis,
        "color": car.gamintojas,
        "country": car.salis,
        "price": car.kaina,
    } for car in all_cars]

    return jsonify(car_data)


@app.route("/api2/automobiliai")
def api2_automobiliai():
    all_cars = Automobilis.query.all()
    car_data = [AutomobilisSchema.model_validate(car).model_dump() for car in all_cars]
    return jsonify(car_data)


@app.route("/frontend")
def frontend():
    return render_template("cars.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
