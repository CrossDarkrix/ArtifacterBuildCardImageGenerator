#!python3

import os, subprocess, urllib.request

script = "#!python3\n\nimport os\n\nos.system('python3 {}'.format(os.path.join(os.environ.get('HOME'), 'Library', 'bin', 'ArtifacterUI.py')))"

if os.path.exists(os.path.join(os.environ.get('HOME'), 'Library', 'bin')):
    with open(os.path.join(os.environ.get('HOME'), 'Library', 'bin', 'artifacter'), 'w', encoding='utf-8') as f:
        f.write(script)
    file = urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/ArtifacterBuildCardImageGenerator/master/iOS/a-Shell/ArtifacterUI.py').read()
    with open(os.path.join(os.environ.get('HOME'), 'Library', 'bin', 'ArtifacterUI.py'), 'wb') as a:
        a.write(file)
    print('Done! run "artifacter"!')
else:
    subprocess.run('pip install -UI pip', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open(os.path.join(os.environ.get('HOME'), 'Library', 'bin', 'artifacter'), 'w', encoding='utf-8') as f:
        f.write(script)
    file = urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/ArtifacterBuildCardImageGenerator/master/iOS/a-Shell/ArtifacterUI.py').read()
    with open(os.path.join(os.environ.get('HOME'), 'Library', 'bin', 'ArtifacterUI.py'), 'wb') as a:
        a.write(file)
    print('Done! run "artifacter"!')