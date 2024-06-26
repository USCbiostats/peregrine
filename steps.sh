#!/bin/bash

if [ $# -eq 0 ]; then
 echo "ERROR: Please specify target folder path"
 exit 1
fi
TARGET=$1

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo 'venv done'

python eQTL/eqtl.py $TARGET/eQTL
echo 'eQTL done'

python heirarchicalTAD/heirarchicalTAD.py $TARGET/heirarchicalTAD
echo 'heirarchical TAD done'

./tad/tad.sh $TARGET/tad
echo 'TAD done'

# cd ../chia_pet
# python ChIA_PET.py

deactivate