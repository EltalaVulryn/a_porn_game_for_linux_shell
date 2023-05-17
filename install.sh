echo "you sure you want to download? (y/N)"

read install

if [[ $install == 'y' ]]; then

	echo "giving the nescary files chmod"
	chmod +x ./pussy ./uninstall.sh
	echo "done"
	echo "installing"
	echo "copying pussy to /usr/bin"
	cp ./pussy /usr/bin/pussy
	echo "completed"
	echo "making new/copying to directy /Games/eroticnight~"
	mkdir /Games
	mkdir /Games/eroticnight~
	echo "completed"
	echo "copying files to /Games/eroticnight~"
	cp ./NSFW.py /Games/eroticnight~/NSFW.py
	cp ./pussy /Games/eroticnight~/pussy
	cp ./README.md /Games/eroticnight~/README.md
	cp ./uninstall.sh /Games/eroticnight~/uninstall.sh
	echo "completed"
	echo "install complete, type in pussy to play the game"
else
	echo "cancelled"
fi
