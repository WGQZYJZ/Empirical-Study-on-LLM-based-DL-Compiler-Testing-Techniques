$ python pytorch_model_generator/pytorch_model_generator.py -p conv,linear,mul,add,tanh,erf
$ torch --version
torch==0.9.0+cpu
numpy==1.22.0  # Use the latest version to match the current PyTorch version
$ python pytorch_model_generator/pytorch_model_generator.py -p conv,linear,mul,add,tanh,erf > results.txt; echo "torch==0.9.0+cpu" >> results.txt; echo "
