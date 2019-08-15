from . import apii
from .import views

apii.add_resource(views.Attrs, '/attr')
