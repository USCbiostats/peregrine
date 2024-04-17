TARGET=$1

python tad/TADorder.py $TARGET
echo 'TADorder done'

python tad/bedtoolIntersect.py $TARGET
echo 'bedtoolIntersect done'

python tad/split.py $TARGET
echo 'split done'

python tad/bTADlinks.py $TARGET
echo 'bTADlinks done'

python tad/concatenate_linksbTAD.py $TARGET
echo 'concatenate_linksbTAD done'

python tad/tTADlinks.py $TARGET
echo 'tTADlinks done'

python tad/linksbTAD_tissueReplace.py $TARGET
echo 'linksbTAD_tissueReplace done'

python tad/final_concatenate.py $TARGET
echo 'final_concatenate done'

python tad/cutdowntad.py $TARGET
echo 'cutdowntad done'

python tad/orderlinks.py $TARGET
echo 'orderlinks done'