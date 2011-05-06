import subprocess
import os.path
import sys

requiredFiles = [
    'sourcemod/addons/sourcemod/scripting/spcomp',
    'sourcemod/addons/sourcemod/extensions/curl.ext.so',
    'sourcemod/addons/sourcemod/scripting/include/cURL.inc',
    ]

if not all(os.path.exists(path) for path in requiredFiles):
    # I'm so lazy.  I should just download it for you.
    print "Please download sourcemod and put unpack it named 'sourcemod'."
    print "http://www.sourcemod.net/dl.php?filename=sourcemod-1.3.7-linux.tar.gz"
    print "Please also download the cURL extension and unpack it in to 'sourcemod'."
    print "https://code.google.com/p/sourcemod-curl-extension/downloads/list"
    sys.exit(2)

versionfile = file('version.inc', 'w')
version = subprocess.Popen(['git', 'describe'], stdout=subprocess.PIPE).communicate()[0].strip()
print >> versionfile, '#define PLUGIN_VERSION "{0}"'.format(version)
versionfile.write(file('config.inc').read())
versionfile.close()
subprocess.call(['./sourcemod/addons/sourcemod/scripting/spcomp', 'tf2mv.sp', '-pversion.inc'])
