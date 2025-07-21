'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_tensor = torch.randn(4, 3)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.diff(dim=(- 1))
print('output_tensor:', output_tensor)