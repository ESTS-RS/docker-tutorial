from dataclasses import dataclass
from flask import Flask, request, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class TaskList(db.Model):
    __tablename__ = "tasklists"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String)

    def __init__(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()


lists = Blueprint("lists", __name__)


@lists.route("/", methods=["GET", "POST"])
def lists_route():
    if request.method == "GET":
        task_lists = TaskList.query.all()
        return jsonify(task_lists)

    elif request.method == "POST":
        task_list_name = request.json["name"]
        task_list = TaskList(task_list_name)
        return jsonify(task_list)


def create_app():
    app = Flask(__name__.split(".")[0])
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/tasklists.db'
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:foobar@db/tasklists"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:foobar@app-db-statefulset/tasklists"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(lists)
    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True)
