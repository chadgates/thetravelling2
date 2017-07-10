
from dynamic_preferences.types import BooleanPreference, StringPreference, Section
from dynamic_preferences.registries import global_preferences_registry


# we create some section objects to link related preferences together

general = Section('general')

# We start with a global preference
@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general
    name = 'title'
    default = 'The Travelling 2'

@global_preferences_registry.register
class MaintenanceMode(BooleanPreference):
    section = general
    name = 'maintenance_mode'
    default = False

@global_preferences_registry.register
class PostEventMode(BooleanPreference):
    section = general
    name = 'postevent_mode'
    default = False



