from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

from config import Config
from models import Base, User, Order

app = Flask(__name__)
CORS(app)

# Database setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# JWT secret
SECRET_KEY = Config.SECRET_KEY


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = session.query(User).filter_by(username=data["username"]).first()

    if user and check_password_hash(user.password_hash, data["password"]):
        token = jwt.encode(
            {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            },
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({"status": "ok", "data": {"token": token}})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"})


@app.route("/orders", methods=["GET"])
def get_orders():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)
    orders = session.query(Order).filter_by(user_id=user_id).all()

    return jsonify({
        "status": "ok",
        "data": [
            {
                "id": o.id,
                "product": o.product,
                "quantity": o.quantity,
                "total_price": str(o.total_price)
            }
            for o in orders
        ]
    })


@app.route("/orders", methods=["POST"])
def create_order():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)

    data = request.json

    order = Order(
        user_id=user_id,
        product=data["product"],
        quantity=data["quantity"],
        total_price=data["total_price"]
    )

    session.add(order)
    session.commit()

    return jsonify({"status": "ok", "message": "Order created"})


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

