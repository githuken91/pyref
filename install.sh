#!/bin/sh
echo Pyref v1 installer
while true; do
    printf "Are you sure you want to continue? (y/n, and press enter): "
    read yn < /dev/tty
    case "$yn" in
        [Yy]* ) 
            break
            ;;
        [Nn]* ) 
            echo "Operation canceled by user."
            exit 1
            ;;
        * ) 
            echo "Please answer yes (y) or no (n)."
            ;;
    esac
done
if [ ! -d "/opt/pyref/manuals/c-api" ]; then
  echo Downloading \& extracting default reference pages...
  curl -sSL http://pyref.alwaysdata.net/refpages.tar.gz -o /tmp/refpages.tar.gz
  mkdir /tmp/refpages
  tar -xf /tmp/refpages.tar.gz -C /tmp/refpages
  mkdir -p /opt/pyref/
  mv /tmp/refpages /opt/pyref/
  mv /opt/pyref/refpages /opt/pyref/manuals
  echo Done.
  echo Adding environment variables...
  target_user="${SUDO_USER:-$USER}"
  user_dir="/home/$target_user"
  set --
  for file in "$user_dir"/.*rc; do
    if [ -f "$file" ]; then
        set -- "$@" "$file"
    fi
  done
  for item in "$@"; do
    echo $item
    echo "export PYREF_MANUAL_DIR=\"/opt/pyref/manuals\"" >> $item
  done
else
  echo Pyref manuals are already installed, skipping installing manuals / environment variables.
fi
if [ ! -f "/bin/pyref" ]; then
  echo Installing pyref...
  curl -fsSL "https://github.com/githuken91/pyref/releases/latest/download/pyref-1.0.0-x86_64-linux.zip"  -o /tmp/pyref.zip
  unzip /tmp/pyref.zip -d /tmp/pyref
  mv /tmp/pyref/* /bin/
  echo Done.
else
  echo Pyref is already installed.
fi
echo Finished! Please refresh your shell\'s .rc file to finalize the installation.
