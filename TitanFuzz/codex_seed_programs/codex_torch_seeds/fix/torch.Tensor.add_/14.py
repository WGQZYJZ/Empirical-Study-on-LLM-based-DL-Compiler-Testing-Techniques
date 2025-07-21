'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(3, 1)
print('input_tensor:', input_tensor)
print('other:', other)
input_tensor.add_(other)
print('After add_:', input_tensor)