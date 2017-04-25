import os

def replace(fpath, old_str, new_str):
    for path, subdirs, files in os.walk(fpath):
        for name in files:
            if(old_str.lower() in name.lower()):
                os.rename(os.path.join(path,name), os.path.join(path,
                                            name.replace(old_str,new_str)))