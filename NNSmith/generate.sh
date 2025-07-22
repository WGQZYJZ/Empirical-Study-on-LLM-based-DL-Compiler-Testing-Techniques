#!/bin/bash

total_runs=2

output_dir="/home/yujunzhe/nnsmith/all_outputs"

# Find the maximum existing output number
last_num=$(find "$output_dir" -maxdepth 1 -type d -name 'output[0-9]*' -printf '%f\n' | 
           sed 's/output//' | 
           sort -n | 
           tail -n 1)

# Calculate start number
start=$((last_num + 1))
[ -z "$last_num" ] && start=1  # Handle first run

for ((i=start; i<start+total_runs; i++)); do
    echo "=============================="
    echo "Starting sequence $i"
    
    if ! python -m nnsmith.cli.model_gen model.type=torch debug.viz=true; then
        echo "Warning: Command failed on sequence $i"
        continue
    fi
    
    if [ -d "/home/yujunzhe/nnsmith/nnsmith_output/" ]; then
        target="${output_dir}/output${i}"
        
        if cp -r "/home/yujunzhe/nnsmith/nnsmith_output" "$target"; then
            echo "Copied to ${target}"
        else
            echo "Error: Failed to copy to ${target}"
        fi
        
        rm -rf "/home/yujunzhe/nnsmith/nnsmith_output"
    else
        echo "Warning: nnsmith_output directory not found"
    fi

    echo "Completed sequence $i"
done

echo "=============================="
echo "All sequences completed! Results saved in ${output_dir}/"