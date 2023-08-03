import glob
import os
import shutil
import sys

from PIL import Image

def get_file_list(_path, _extension, _deep_search = False):
    if _deep_search:
        _extension = '**\*.' + _extension
    else:
        _extension = '*.' + _extension

    return glob.glob(os.path.join(_path, _extension), recursive = _deep_search)
    
    """
    return tuple data in w, h
    """
def get_image_size(_file):
    im = Image.open(_file)
    return im.size
    
def copy_tree(_source, _target, _ignored_filenames = []):
    if (os.path.isfile(_source)):
        _source = os.path.dirname(_source)
        
    if (os.path.isfile(_target)):
        _target = os.path.dirname(_target)
    
    def getIgnored(path, filenames):
        ignored_ = []
        for file in filenames:
            if (file in _ignored_filenames):
                ignored_.append(file)
        
        return ignored_
    
    print('Copy tree: [' + _source + ']')
    print('into path: [' + _target + ']')
    
    shutil.copytree(_source, _target, ignore = getIgnored, dirs_exist_ok = True)

def copy_file(_source_file, _target_path):
    file_name = os.path.basename(_source_file)
    
    create_path_if_not_exists(_target_path)
    
    if (os.path.isdir(_target_path)):
        _target_path = os.path.join(_target_path, file_name)
        
    print('Copy file: [' + _source_file + ']')
    print('into path: [' + _target_path + ']')
    
    shutil.copyfile(_source_file, _target_path)

def copy_files(_file_list, _target_path_list):
    if (_file_list):
        print('Copying (' + str(len(_file_list)) + ') files ...')
    else:
        print('Copying empty list, canceled ...')
        return
    
    for target_path in _target_path_list:
        create_path_if_not_exists(target_path)
        
        for i in range(len(_file_list)):
            copy_file(_file_list[i], target_path)
            
            print('-- progress: ' + str(round((i + 1) * 100 / len(_file_list))) + ' %', end = '\r')
            
        print('-- complete')
        
def copy_files_append_directory_name(_root_directory, _file_list, _target_path_list):
    if (_file_list):
        print('Copy & rename [' + str(len(_file_list)) + '] files ...')
    else:
        print('Copying empty list, canceled ...')
        return
        
    root_dir = os.path.basename(_root_directory)
    
    for target_path in _target_path_list:
        create_path_if_not_exists(target_path)
        
        for i in range(len(_file_list)):
            # the output will be dirs: ['', '\\path']
            dirs = os.path.dirname(_file_list[i]).split(root_dir)[1]
            dirs = [d for d in dirs.split('\\') if d]
            
            target_name = ''

            for d in dirs:
                target_name += d + '_'
                
            target_name += os.path.basename(_file_list[i])
        
            copy_file(_file_list[i], os.path.join(target_path, target_name))
            print('-- progress: ' + str(round((i + 1) * 100 / len(_file_list))) + ' %', end = '\r')
            
        print('-- complete')
        
def move_file(_source_file, _target_path):
    file_name = os.path.basename(_source_file)

    if (os.path.isdir(_target_path)):
        _target_path = os.path.join(_target_path, file_name)
        
    shutil.move(_source_file, _target_path)
    
def move_files(_source_files, _target_path):
    for file in _source_files:
        move_file(file, _target_path)
    
def create_path_if_not_exists(_path):
    if not os.path.exists(_path):
        os.makedirs(_path)