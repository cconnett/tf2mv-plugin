all: tf2mv.smx

tf2mv.smx: tf2mv.sp sourcemod/addons/sourcemod/scripting/spcomp cURL.inc version.inc
	./sourcemod/addons/sourcemod/scripting/spcomp tf2mv.sp -pversion.inc

version.inc:
	echo -n "#define PLUGIN_VERSION $(git describe)" > version.inc

sourcemod/addons/sourcemod/scripting/spcomp: sourcemod.tar.gz
	mkdir -p sourcemod
	which pv > /dev/null && pv sourcemod.tar.gz | tar mxz -C sourcemod || tar mxzf sourcemod.tar.gz -C sourcemod

sourcemod.tar.gz:
	wget http://www.gsptalk.com/mirror/sourcemod/sourcemod-1.3.7-linux.tar.gz -O sourcemod.tar.gz

cURL.inc: curl.zip
	unzip -Dquod sourcemod/addons/sourcemod curl.zip

curl.zip:
	wget http://sourcemod-curl-extension.googlecode.com/files/curl_1.2.0.0.zip -O curl.zip