'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(input_tensor)
other = torch.randn(3, 2)
print('Other tensor:')
print(other)
print('Output tensor:')
print(input_tensor.view_as(other))