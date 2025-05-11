source_root="../../../data/processed"
target_file="../../../frontend/public/data/results.json"

rm -f $target_file

for file in $source_root/*.json; do
    cat $file >> $target_file
done
