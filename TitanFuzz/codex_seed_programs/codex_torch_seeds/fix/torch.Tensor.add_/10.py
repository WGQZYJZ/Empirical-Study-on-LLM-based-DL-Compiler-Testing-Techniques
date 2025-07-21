'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(1, 3)
other = torch.randn(1, 3)
output_tensor = torch.Tensor.add_(input_tensor, other)
print('input_tensor =', input_tensor)
print('other =', other)
print('output_tensor =', output_tensor)