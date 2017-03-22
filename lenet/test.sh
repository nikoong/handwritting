

solver=/home/nikoong/Algorithm_test/handwritting/lenet/solver.prototxt
max_iter=$(grep 'max_iter' ${solver} | awk '{print $2}')
snapshot_prefix=$(grep 'snapshot' ${solver} | awk -F '"' '{print $2}') 
logname=${snapshot_prefix##*snapshots/}
echo ${logname}

