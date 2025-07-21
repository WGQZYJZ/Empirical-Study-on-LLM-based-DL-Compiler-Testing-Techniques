'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_tensor = torch.randn(5, 2)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None)
print('Output tensor: ', output_tensor)