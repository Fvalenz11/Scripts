echo "Cleaning memory...:.."

 sync; echo 1 > /proc/sys/vm/drop_caches # clear PageCache
 sync; echo 2 > /proc/sys/vm/drop_caches # clear dentries and inodes
 sync; echo 3 > /proc/sys/vm/drop_caches # clear all 3
 
echo "Current Stats ...: .."
df
free
