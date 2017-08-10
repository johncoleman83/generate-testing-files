#!/usr/bin/env bash
# executes tests based on file type

function begintest {
    echo "initializing tests..."
    sleep 1
}

echo -ne "\033[37m"
echo "* *********************************************************** *"
echo "*                                                             *"
echo "*  Please Select Testing File Type:                           *"
echo -n "*             "
echo -ne "\033[30m(1) PYTHON                                      "
echo -e "\033[37m*"
echo -n "*             "
echo -ne "\033[30m(2) PYTHON + SQL                                "
echo -e "\033[37m*"
echo -n "*             "
echo -ne "\033[30m(3) C                                           "
echo -e "\033[37m*"
echo -n "*             "
echo -ne "\033[30m(4) C Header (.h) file                          "
echo -e "\033[37m*"
echo "*                                                             *"
echo "* *********************************************************** *"
echo -ne "\033[30m"
read -p "Type your choice number or anything else to quit " -n 1 -r REPLY
echo

case "$REPLY" in
        1)
            begintest
	    ./generate_pyfile.py
            ;;
        2)
            begintest
	    ./generate_sqlfile.py
            ;;
        3)
            begintest
	    ./generate_cfile.py
            ;;
        4)
            begintest
	    ./generate_cheader.py
            ;;
        *)
	    echo "...Goodbye"
	    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
esac
