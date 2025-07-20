rm -r Results/torch
DOCKER_RUN=${1:-true}
if $DOCKER_RUN ; then
    bash scripts/copyfile.sh
    bash scripts/dockerrun.sh bash scripts/run.sh torch data/torch_valid_apis_100sample.txt
else
    echo "Warning: running in a non-docker environment!"
    start_time=$(date +%s%N)
    echo "Start time: $(date '+%Y-%m-%d %H:%M:%S.%3N')"

    handle_interrupt() {
        end_time=$(date +%s%N)
        elapsed_ms=$(( (end_time - start_time) / 1000000 ))
        echo -e "\nInterrupted! Time elapsed: ${elapsed_ms} ms"
        exit 1
    }
    
    trap handle_interrupt INT
    
    bash scripts/local_run.sh torch data/torch_valid_apis_100sample.txt
    
    end_time=$(date +%s%N)
    elapsed_ms=$(( (end_time - start_time) / 1000000 ))
    echo "Time elapsed: ${elapsed_ms} ms"
    
    trap - INT
fi
