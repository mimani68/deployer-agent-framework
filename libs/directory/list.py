import os

def get_sh_files(folder):
    sh_files = []
    for filename in os.listdir(folder):
        if filename.endswith('.sh'):
            sh_files.append(filename)
    return sh_files
