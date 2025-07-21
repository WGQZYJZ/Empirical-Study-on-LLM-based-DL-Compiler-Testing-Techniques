'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma_\ntorch.Tensor.lgamma_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
print('Output tensor: ', torch.Tensor.lgamma_(input_tensor))