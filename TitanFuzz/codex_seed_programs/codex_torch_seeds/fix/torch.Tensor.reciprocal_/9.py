'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal_\ntorch.Tensor.reciprocal_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
reciprocal_output = torch.Tensor.reciprocal_(input_tensor)
print('Output tensor: ', reciprocal_output)