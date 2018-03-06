#!/bin/bash

echo 'fresh beginning...'

git fetch
ver=version.txt

version=`<$ver`
echo 'local :' $version

commit_id=`git rev-parse HEAD`
echo 'remote:' $commit_id

path=$(cd `dirname $0`;pwd)
echo $path

moveToPublish(){
    if [ ! -n $1];then
    	echo 'cp -rf . $1'
    	cd $1
    fi
}

if [[ ! -n $version || $commit_id != $version ]]; then
	echo $commit_id >$ver
	git pull origin master
	moveToPublish
else
    echo 'The local same as remote commit id.'
fi


echo 'fresh over.it was completed.Now,ready to publish ...'
echo '----------------------------------------------------'
echo 'sudo killall -9 uwsig'
echo 'sudo uwsig uwsig.ini'
echo 'sudo service nginx restart'
echo '----------------------------------------------------'
echo 'Publish was completed.'
