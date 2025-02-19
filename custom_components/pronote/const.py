"""Constants for the Pronote integration."""

from homeassistant.const import Platform

DOMAIN = "pronote"
EVENT_TYPE = "pronote_event"

LESSON_MAX_DAYS = 15
HOMEWORK_MAX_DAYS = 15

GRADES_TO_DISPLAY = 11
EVALUATIONS_TO_DISPLAY = 15

HOMEWORK_DESC_MAX_LENGTH = 125

# default values for options
DEFAULT_REFRESH_INTERVAL=15
DEFAULT_ALARM_OFFSET=60
DEFAULT_LUNCH_BREAK_TIME='13:00'

PLATFORMS = [Platform.SENSOR]
