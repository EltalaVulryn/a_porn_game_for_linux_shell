echo "you sure you want to download? (y/N)"

read install

if [[ $install == 'y' ]]; then

	chmod +x ./pussy ./uninstall.sh
	cp ./pussy /usr/bin/pussy
	mkdir /Games
	mkdir /Games/eroticnight~
	mkdir /Games/eroticnight~/animations
	mkdir /Games/eroticnight~/assets
	cp ./NSFW.py /Games/eroticnight~/NSFW.py
	cp ./pussy /Games/eroticnight~/pussy
	cp ./README.md /Games/eroticnight~/README.md
	cp ./uninstall.sh /Games/eroticnight~/uninstall.sh
	cp -r ./animations /Games/eroticnight~
        cp ./animations/cum.sh /Games/eroticnight~/animations/cum.sh
	cp ./animations/cump.sh /Games/eroticnight~/animations/cump.sh
	cp ./animations/rbutter.sh /Games/eroticnight~/animations/rbutter.sh
	cp ./animations/rbutterp.sh /Games/eroticnight~/animations/rbutterp.sh
	cp ./assets/repeatrbut.sh /Games/eroticnight~/assets/repeatrbut.sh  
	echo "completed"
else
	echo "cancelled"
	exit 1
fi
