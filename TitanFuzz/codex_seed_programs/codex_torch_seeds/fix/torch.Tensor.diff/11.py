'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_tensor = torch.randn(3, 3, 3)
print('Input Tensor: ')
print(input_tensor)
output_tensor = torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None)
print('Output Tensor: ')
print(output_tensor)