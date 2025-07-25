#!/bin/bash

generate_dir=${1:-"Prompts-generated"}

template_dir="template-torch"

# Generate prompts for the NL generation.
for optim_name in 'inductor' 'group-batch'; do
    python3 prompt_gen.py --optpath=optim/inductor-${optim_name}.json --mode=src2nl --template=${template_dir}/starcoder-src2nl.txt --outdir=${generate_dir}/torch-inductor/req2test
done

for optim_name in 'postgrad' 'mkldnn' 'sfdp' 'bnfold' 'decompose' 'misc' 'split-cat'; do
    python3 prompt_gen.py --optpath=optim/inductor-${optim_name}.json --mode=src2nl --template=${template_dir}/starcoder-src2nl-pattern.txt --outdir=${generate_dir}/torch-inductor/req2test
done