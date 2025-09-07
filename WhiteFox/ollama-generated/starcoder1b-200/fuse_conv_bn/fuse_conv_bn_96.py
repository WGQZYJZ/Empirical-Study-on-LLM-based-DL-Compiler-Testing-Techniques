This pattern characterizes scenarios where a convolution layer (`torch.nn.Conv2d`) and a batch normalization layer (`torch.nn.BatchNorm2d`) are followed by the functional API `torch.nn.functional.conv2d` or `torch.nn.functional.batch_norm`. The output of the convolution layer is used as input to the batch normalization layer, and vice versa. 

The optimization applies to the functional API equivalent of the above pattern, where the module API `torch.nn.ConvXd` and `torch.nn.BatchNormXd` are used instead of the functional API `conv2d`, `batch_norm`, etc.

# Implementation
The PyTorch code to perform the analysis is under `main.cpp`. The Python script to perform the analysis is under `tools/pytorch/pytorch_fuser.py`.

# Example usage: 
## Output example: 
## Input: 
![Input](/data/images/conv-bn/example1.png)


# Example usage: 
The configuration file should contain:
- `graph`: the list of modules connected together as a directed graph, like [A -> B -> C]
- `inputs`: the name of the input nodes of the graph, including all input/output nodes
- `outputs`: the names of the output nodes, including all input/output nodes

The PyTorch model example is generated using `tools/pytorch/generate_model.py`, it should be identical to the one provided by this tool. 
