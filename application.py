"""
Entry point for Azure App Service / Gunicorn
This file is required because Azure's Oryx builder looks for 'application:app'
"""
from app.main import app

__all__ = ["app"]
