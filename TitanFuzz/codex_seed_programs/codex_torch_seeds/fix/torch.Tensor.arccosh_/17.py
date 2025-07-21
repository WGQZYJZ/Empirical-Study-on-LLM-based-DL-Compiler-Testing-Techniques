'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh_\ntorch.Tensor.arccosh_(_input_tensor, )\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
arccosh_tensor = torch.Tensor.arccosh_(input_tensor)
print('arccosh_tensor: ', arccosh_tensor)