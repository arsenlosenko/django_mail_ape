"""gunicorn configuration"""
import os

bind = "0.0.0.0:{}".format(os.environ.get('PORT', 8000))
