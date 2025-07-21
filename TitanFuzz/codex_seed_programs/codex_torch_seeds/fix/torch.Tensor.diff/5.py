'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
print('input_tensor:')
print(input_tensor)
print('torch.Tensor.diff(input_tensor, n=1, dim=-1, prepend=None, append=None):')
print(torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None))