from flask import Flask, request, url_for

import people_web_app.adapters.repository as repo
from people_web_app.domain.model import Person


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    with app.app_context():
        from people_web_app.people_blueprint.people import people_blueprint
        app.register_blueprint(people_blueprint)


    repo.repo_instance = repo.PeopleRepository(
        Person(74633, 'Julius', 'Caeser'),
        Person(88337, 'Genghis', 'Khan'),
        Person(92731, 'Winston', 'Churchill'),
        Person(12826, 'Mahatma', 'Ghandi'),
        Person(92213, 'Nelson', 'Mandela')
    )

    return app
