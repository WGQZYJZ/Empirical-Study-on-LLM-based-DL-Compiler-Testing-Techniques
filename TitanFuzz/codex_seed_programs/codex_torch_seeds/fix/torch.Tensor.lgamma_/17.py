'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma_\ntorch.Tensor.lgamma_(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', torch.Tensor.lgamma_(input_tensor))