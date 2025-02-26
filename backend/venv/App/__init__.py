from flask import Flask
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    
     
    from blueprints import audience, goals, content, engagement, analytics, campaign, crisis, community, adaptation
    
    app.register_blueprint(audience.bp)
    app.register_blueprint(goals.bp)
    app.register_blueprint(content.bp)
    app.register_blueprint(engagement.bp)
    app.register_blueprint(analytics.bp)
    app.register_blueprint(campaign.bp)
    app.register_blueprint(crisis.bp)
    app.register_blueprint(community.bp)
    app.register_blueprint(adaptation.bp)

    return app