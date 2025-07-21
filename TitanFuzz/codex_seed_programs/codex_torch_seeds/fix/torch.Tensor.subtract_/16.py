'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output_tensor = torch.Tensor.subtract_(input_tensor, other)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.sum(input_tensor)
print('input_tensor:', input_tensor)