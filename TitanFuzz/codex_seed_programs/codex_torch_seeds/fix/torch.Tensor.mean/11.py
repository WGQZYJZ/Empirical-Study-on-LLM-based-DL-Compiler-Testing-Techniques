'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input Tensor: ')
print(_input_tensor)
_mean = torch.Tensor.mean(_input_tensor, dim=1)
print('Mean: ')
print(_mean)
_mean = torch.Tensor.mean(_input_tensor, dim=1, keepdim=True)
print('Mean: ')
print(_mean)
_mean = torch.Tensor.mean(_input_tensor, dim=0, keepdim=True)
print('Mean: ')
print(_mean)