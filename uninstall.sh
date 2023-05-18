echo "would you like to removing the /Games directory too? (y/N)"

read option

if [[ $option == "y" ]]; then
	echo "removed /Games directory"
	rm /usr/bin/pussy
	rm -rf /Games
else
	echo "keeping /Games directory"
	rm /usr/bin/pussy
	rm -rf /Games/eroticnight~
fi
