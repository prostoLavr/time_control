d=`dirname "$0"` fullpath=`cd "$d"; pwd`/`basename "$0"`
echo $fullpath
source $d/venv/bin/activate
python $d/app.py

