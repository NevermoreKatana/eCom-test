from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
import re

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/forms_db'
mongo = PyMongo(app)


def validate_fields(fields):
    for field_name, field_value in fields.items():
        if field_name == "order_date":
            try:
                datetime.strptime(field_value, "%d.%m.%Y")
                return field_value
            except ValueError:
                pass
        elif field_name == "phone_number":
            if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', field_value):
                return field_value
        elif field_name == "lead_email":
            if re.match(r'^\S+@\S+\.\S+$', field_value):
                return field_value
    return field_name


@app.route('/get_form', methods=['POST'])
def get_form():
    fields = request.form.to_dict()

    templates = mongo.db.forms.find()

    for template in templates:
        template_fields = {key: template[key] for key in template.keys() if key != '_id'}
        if all(template_fields.get(field) == fields.get(field) for field in template_fields):
            return jsonify({"template_name": template['name']})

    field_types = {}
    for field_name, field_value in fields.items():
        field_type = validate_fields({field_name: field_value})
        field_types[field_name] = field_type

    return jsonify(field_types)


if __name__ == '__main__':
    app.run(debug=True)
