if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

echo -e "\nUpdating system packages...\n"

apt update
apt upgrade -y && apt autoremove -y

echo -e "\nUpdating firmware...\n"

fwupdmgr update
