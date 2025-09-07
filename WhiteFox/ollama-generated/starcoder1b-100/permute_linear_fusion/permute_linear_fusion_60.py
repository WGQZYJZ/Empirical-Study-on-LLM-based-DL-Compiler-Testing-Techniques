The above example of a class is not allowed because there's no class instance can be created. Therefore, you need to define the `Model` class outside. Note that it's recommended to initialize the `Model` class in __init__, since otherwise you will encounter the problem: "TypeError: __init__() missing 1 required positional argument: 'self'".

## How to run
The script will run `torch.nn.functional.linear` to verify whether the inputs and outputs are valid.

## Citation
Please cite our paper if you find it useful: https://arxiv.org/abs/2005.12847
