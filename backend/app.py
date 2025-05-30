from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables BEFORE importing routes
load_dotenv()

# Verify key was loaded
api_key = os.environ.get('GOOGLE_API_KEY')
if not api_key:
    print("WARNING: GOOGLE_API_KEY not found in environment!")
else:
    print("GOOGLE_API_KEY loaded successfully")

# Now import routes that use the API key
from routes.RandomPassNo_route import rpn_bp
from routes.CsvExcelTools_route import cet_bp
from routes.ImageGen_route import ig_bp
from routes.NetworkTools_route import nt_bp
from routes.ApiTools_route import at_bp
from routes.CodeFormatters_route import cfv_bp
from routes.OCR_route import ocr_bp
from routes.RegexBuilder_route import regex_bp
from routes.UnitConverter_route import uc_bp
from routes.UserFeedback_routes import feedback_bp
from routes.SqlConverter_route import sql_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(rpn_bp)
app.register_blueprint(cet_bp)
app.register_blueprint(ig_bp)
app.register_blueprint(nt_bp)
app.register_blueprint(at_bp)
app.register_blueprint(cfv_bp)
app.register_blueprint(ocr_bp)
app.register_blueprint(regex_bp)
app.register_blueprint(uc_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(sql_bp)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Welcome to the API!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5050)


