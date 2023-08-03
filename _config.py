import os

APP_NAME                = 'my-app'

CRT_PATH                = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_PATH            = CRT_PATH
DATA_PATH               = os.path.abspath(CRT_PATH + '/../data')
SRC_PATH                = os.path.abspath(CRT_PATH + '/../source')

DATA_TEXTS_PATH         = os.path.abspath(DATA_PATH + '/Text')
DATA_DATABASE_PATH      = os.path.abspath(DATA_PATH + '/Database')
DATA_RESOURCES_PATH     = os.path.abspath(DATA_PATH + '/Resources')

DATA_ANIM_PATH          = os.path.abspath(DATA_RESOURCES_PATH + '/anim')
DATA_COLOR_PATH         = os.path.abspath(DATA_RESOURCES_PATH + '/color')
DATA_DRAWABLE_PATH      = os.path.abspath(DATA_RESOURCES_PATH + '/drawable')
DATA_LAYOUT_PATH        = os.path.abspath(DATA_RESOURCES_PATH + '/layout')
DATA_MENU_PATH          = os.path.abspath(DATA_RESOURCES_PATH + '/menu')
DATA_RAW_PATH           = os.path.abspath(DATA_RESOURCES_PATH + '/raw')
DATA_VALUES_PATH        = os.path.abspath(DATA_RESOURCES_PATH + '/values')

ASSETS_PATH             = os.path.abspath(SRC_PATH + '/' + APP_NAME + '/Assets')
PROPERTIES_PATH         = os.path.abspath(SRC_PATH + '/' + APP_NAME + '/Properties')
RESOURCES_PATH          = os.path.abspath(SRC_PATH + '/' + APP_NAME + '/Resources')

RES_ANIM_PATH           = os.path.abspath(RESOURCES_PATH + '/anim')
RES_COLOR_PATH          = os.path.abspath(RESOURCES_PATH + '/color')
RES_DRAWABLE_PATH       = os.path.abspath(RESOURCES_PATH + '/drawable')
RES_LAYOUT_PATH         = os.path.abspath(RESOURCES_PATH + '/layout')
RES_MENU_PATH           = os.path.abspath(RESOURCES_PATH + '/menu')
RES_RAW_PATH            = os.path.abspath(RESOURCES_PATH + '/raw')
RES_VALUES_PATH         = os.path.abspath(RESOURCES_PATH + '/values')

# Toggle feature on/ off
USE_CRASHLYTICS         = True