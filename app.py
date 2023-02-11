from flask import Flask
from typing import Optional, Any

from views import main_bp

def create_app() -> Optional[Any]:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
