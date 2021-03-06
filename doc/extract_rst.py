import os
import ntpath

#-------------------------------------------------------------------------------

def extract_rst_blobs(s_in):
    s_out = []
    is_rst_line = False
    for line in s_in.split('\n'):
        if is_rst_line:
            if len(line) > 0:
                if line[0] != '#':
                    is_rst_line = False
            else:
                is_rst_line = False
        if is_rst_line:
            s_out.append(line[2:])
        if '#.rst:' in line:
            is_rst_line = True
    return '\n'.join(s_out)

def test_extract_rst_blobs():
    s_in = '''# a
# b
#.rst:
# c
#  d

# e
# f
g
h
# i
# j
#.rst:
# k
# l'''
    s_out = '''c
 d
k
l'''

    assert s_out == extract_rst_blobs(s_in)

#-------------------------------------------------------------------------------

def main():

    THIS_DIR = os.path.dirname(os.path.realpath(__file__))

    output = []
    output.append("Module reference")
    output.append("================")
    output.append("\n")

    module_path = os.path.join(THIS_DIR, '..', 'modules')

    modules = []
    for root, dirs, files in os.walk(module_path):
        relative_path = os.path.relpath(root, module_path)
        for f in files:
            modules.append((os.path.join(root, f), relative_path))
    modules = sorted(set(modules))

    for f, relative_path in modules:
        file_name = ntpath.basename(f)
        if relative_path != '.':
            full_file_name = '%s/%s' % (relative_path, file_name)
        else:
            full_file_name = file_name
        with open(f, 'r') as s:
            s_out = extract_rst_blobs(s.read())
            if s_out != '':
                output.append('\n\n%s' % file_name)
                output.append('-'*len(file_name))
                output.append('`[Source code] <https://github.com/dev-cafe/autocmake/blob/master/modules/%s>`__' % full_file_name)
                output.append(s_out)

    with open(os.path.join(THIS_DIR, 'module-reference.rst'), 'w') as f:
        f.write('\n'.join(output))

#-------------------------------------------------------------------------------

main()
