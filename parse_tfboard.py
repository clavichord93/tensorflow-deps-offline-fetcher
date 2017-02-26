import os

tfboard_dep_dir = '/home/qz/tensorflow/tfboard_deps'
# if (os.path.exists(tfboard_dep_dir) == False):
    # os.system('mkdir %s' % tfboard_dep_dir)
if (os.path.exists('tfboard_deps') == False):
    os.system('mkdir tfboard_deps')

workspace = open('WORKSPACE', 'r')
input_lines = workspace.readlines()
output_lines = []

name = None
url = None
pahtname = None
for line in input_lines:
    tline = line.strip(' \n,')
    t = tline.split(' ')
    nline = line
    if (t[0] == 'name'):
        name = t[2].strip('"')
        dir = 'tfboard_deps' + os.sep + '%s' % name
        if (os.path.exists(dir) == False):
            os.system('mkdir %s' % dir)
    if (t[0] == 'url'):
        url = t[2].strip('"')
        filename = url.split('/')[-1]
        target = 'tfboard_deps' + os.sep + name + os.sep + filename
        nurl = tfboard_dep_dir + os.sep + name + os.sep + filename
        if (os.path.exists(target) == False):
            print(name + ' not found!')
            os.system('proxychains wget %s -O %s' % (url, target))
        nline = '  url = "file:///%s",\n' % nurl
    output_lines.append(nline)

open('_WORKSPACE', 'w').writelines(output_lines)
