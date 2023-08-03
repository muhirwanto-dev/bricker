import glob
import os
import sys
import json

import _config
import _utils

def override_source():
    source_list_dir = [
        os.path.join(_config.MASTER_SRC_PATH, 'Sources')
    ]
    
    target_list = [
        os.path.join(_config.SRC_PATH, 'Sources')
    ]
    
    for i in range(len(source_list_dir)):
        copy_tree(source_list_dir[i], target_list[i])
        
def clone_data2source():
    source_list = []
    target_list = []

    # copy animation
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_ANIM_PATH, 'xml', True), 'anim')
    target_list = [_config.RES_ANIM_PATH]
    
    _utils.copy_files(source_list, target_list)
    
    # copy color
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_COLOR_PATH, 'xml', True), 'color')
    target_list = [_config.RES_COLOR_PATH]
    
    _utils.copy_files(source_list, target_list)
    
    # copy drawable
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_DRAWABLE_PATH, 'xml', True), 'drawable')
    target_list = [_config.RES_DRAWABLE_PATH]
    
    _utils.copy_files(source_list, target_list)
    
    # copy drawable-night
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_DRAWABLE_PATH + '-night', 'xml', True), 'drawable-night')
    target_list = [_config.RES_DRAWABLE_PATH + '-night']
    
    _utils.copy_files(source_list, target_list)
    
    # copy layout
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_LAYOUT_PATH, 'xml', True), 'layout')
    target_list = [_config.RES_LAYOUT_PATH]
    
    _utils.copy_files(source_list, target_list)
    
    # copy layout-h720dp
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_LAYOUT_PATH + '-h720dp', 'xml', True), 'layout')
    target_list = [_config.RES_LAYOUT_PATH + '-h720dp']
    
    _utils.copy_files(source_list, target_list)

    # copy menu
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_MENU_PATH, 'xml', True), 'menu')
    target_list = [_config.RES_MENU_PATH]
    
    _utils.copy_files(source_list, target_list)

    # copy raw: drawable
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_RAW_PATH, 'xml', True), 'raw')
    target_list = [_config.RES_DRAWABLE_PATH]
    
    _utils.copy_files(source_list, target_list)
    
    # copy raw: image
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_RAW_PATH, 'png', True), 'raw')
    target_list = [_config.RES_RAW_PATH]
    
    _utils.copy_files(source_list, target_list)
        
    # copy values
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_VALUES_PATH, 'xml', True), 'values')
    target_list = [_config.RES_VALUES_PATH]
    
    _utils.copy_files(source_list, target_list)
        
    # copy values-h720dp
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_VALUES_PATH + '-h720dp', 'xml', True), 'values-h720dp')
    target_list = [_config.RES_VALUES_PATH + '-h720dp']
    
    _utils.copy_files(source_list, target_list)
        
    # copy values-h720dp-night
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_VALUES_PATH + '-h720dp-night', 'xml', True), 'values-h720dp-night')
    target_list = [_config.RES_VALUES_PATH + '-h720dp-night']
    
    _utils.copy_files(source_list, target_list)
    
    # copy values-night
    source_list = remove_excluded(_utils.get_file_list(_config.DATA_VALUES_PATH + '-night', 'xml', True), 'values-night')
    target_list = [_config.RES_VALUES_PATH + '-night']
    
    _utils.copy_files(source_list, target_list)
    
    # copy static DB
    source_list = [os.path.join(_config.DATA_DATABASE_PATH, 'Database.json')]
    target_list = [os.path.join(_config.ASSETS_PATH, 'Database')]
    
    _utils.copy_files(source_list, target_list)
    
def clone_source2data():
    source_list = []
    target_list = []
    
    # copy animation
    source_list = _utils.get_file_list(_config.RES_ANIM_PATH, 'xml', True)
    target_list = [_config.DATA_ANIM_PATH]
    
    _utils.copy_files(source_list, target_list)

    # copy color
    source_list = _utils.get_file_list(_config.RES_COLOR_PATH, 'xml', True)
    target_list = [_config.DATA_COLOR_PATH]
    
    _utils.copy_files(source_list, target_list)
    
    # copy drawable
    source_list = _utils.get_file_list(_config.RES_DRAWABLE_PATH, 'xml', True)
    
    # https://github.com/leapfrogtechnology/android-guidelines/blob/master/ResourcesGuidelines.md
    for drawable in source_list:
        if ('ab_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'actionbar'))
        elif ('bg_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'background'))
        elif ('btn_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'button'))
        elif ('dialog_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'dialog'))
        elif ('divider_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'divider'))
        elif ('ic_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'icon'))
        elif ('menu_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'menu'))
        elif ('notification_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'notification'))
        elif ('tab_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH, 'tabs'))
        else:
            _utils.copy_file(drawable, _config.DATA_DRAWABLE_PATH)
    
    # copy drawable-night
    source_list = _utils.get_file_list(_config.RES_DRAWABLE_PATH + '-night', 'xml', True)
    
    # https://github.com/leapfrogtechnology/android-guidelines/blob/master/ResourcesGuidelines.md
    for drawable in source_list:
        if ('ab_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'actionbar'))
        elif ('bg_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'background'))
        elif ('btn_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'button'))
        elif ('dialog_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'dialog'))
        elif ('divider_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'divider'))
        elif ('ic_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'icon'))
        elif ('menu_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'menu'))
        elif ('notification_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'notification'))
        elif ('tab_' in drawable):
            _utils.copy_file(drawable, os.path.join(_config.DATA_DRAWABLE_PATH + '-night', 'tabs'))
        else:
            _utils.copy_file(drawable, _config.DATA_DRAWABLE_PATH + '-night')
            
    # copy layout
    source_list = _utils.get_file_list(_config.RES_LAYOUT_PATH, 'xml', True)
    
    # https://github.com/leapfrogtechnology/android-guidelines/blob/master/ResourcesGuidelines.md
    for layout in source_list:
        if ('activity_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH, 'activity'))
        elif ('appbar_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH, 'appbar'))
        elif ('dialog_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH, 'dialog'))
        elif ('fragment_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH, 'fragment'))
        elif ('list_item_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH, 'list-item'))
        elif ('partial_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH, 'partial'))
        else:
            _utils.copy_file(layout, _config.DATA_LAYOUT_PATH)
            
    # copy layout-h720dp
    source_list = _utils.get_file_list(_config.RES_LAYOUT_PATH + '-h720dp', 'xml', True)
    
    # https://github.com/leapfrogtechnology/android-guidelines/blob/master/ResourcesGuidelines.md
    for layout in source_list:
        if ('activity_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH + '-h720dp', 'activity'))
        elif ('appbar_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH + '-h720dp', 'appbar'))
        elif ('dialog_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH + '-h720dp', 'dialog'))
        elif ('fragment_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH + '-h720dp', 'fragment'))
        elif ('list_item_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH + '-h720dp', 'list-item'))
        elif ('partial_' in layout):
            _utils.copy_file(layout, os.path.join(_config.DATA_LAYOUT_PATH + '-h720dp', 'partial'))
        else:
            _utils.copy_file(layout, _config.DATA_LAYOUT_PATH + '-h720dp')
            
    # copy menus
    source_list = _utils.get_file_list(_config.RES_MENU_PATH, 'xml', True)
    target_list = [_config.DATA_MENU_PATH]
    
    _utils.copy_files(source_list, target_list)

    # copy values
    source_list = _utils.get_file_list(_config.RES_VALUES_PATH, 'xml', True)
    target_list = [_config.DATA_VALUES_PATH]
    
    _utils.copy_files(source_list, target_list)

    # copy values-h720dp
    source_list = _utils.get_file_list(_config.RES_VALUES_PATH + '-h720dp', 'xml', True)
    target_list = [_config.DATA_VALUES_PATH + '-h720dp']
    
    _utils.copy_files(source_list, target_list)

    # copy values-h720dp-night
    source_list = _utils.get_file_list(_config.RES_VALUES_PATH + '-h720dp-night', 'xml', True)
    target_list = [_config.DATA_VALUES_PATH + '-h720dp-night']

    _utils.copy_files(source_list, target_list)
    
    # copy values-night
    source_list = _utils.get_file_list(_config.RES_VALUES_PATH + '-night', 'xml', True)
    target_list = [_config.DATA_VALUES_PATH + '-night']
    
    _utils.copy_files(source_list, target_list)
    
def remove_excluded(files, json_key):
    data = {}
    
    with open(os.path.join(_config.DATA_RESOURCES_PATH, 'exclude.json'), 'r') as f:
        data = json.load(f)
        
    if (json_key not in data):
        return files
        
    excluded = data[json_key]
    
    return [i for i in files if os.path.basename(i) not in excluded]