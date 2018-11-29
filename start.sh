#!/bin/sh

echo 'Fefresh beginning...'

ver=version.txt

version=`<$ver`
echo 'local :' $version

git fetch
commit_id=`git rev-parse HEAD`
echo 'remote:' $commit_id

path=$(cd `dirname $0`;pwd)
movedir=$1
moveToPublish(){
    if [[ -n $movedir ]];then
    	if [[ -d $movedir ]];then
    		cp -rf . $movedir
    		cd $movedir
    	else
    		mkdir $movedir
    		moveToPublish
    	fi
    fi
}

if [[ ! -n $version || $commit_id != $version ]]; then
	echo $commit_id >$ver
	git pull origin master
else
    echo 'The local same as remote commit id.'
fi

moveToPublish


echo 'Fefresh over.it was completed.Now,ready to publish ...'
echo '----------------------------------------------------'
echo `sudo killall -9 uwsgi`
echo `sudo uwsgi uwsgi.ini`
echo `sudo service nginx restart`
echo '----------------------------------------------------'
echo 'Publish was completed.'
