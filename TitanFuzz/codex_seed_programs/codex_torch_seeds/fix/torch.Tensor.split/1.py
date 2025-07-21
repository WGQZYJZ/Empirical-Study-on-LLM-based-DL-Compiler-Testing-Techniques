'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
import torch
_input_tensor = torch.arange(0, 24).view(2, 3, 4)
print('Input tensor:\n', _input_tensor)
_splits = torch.Tensor.split(_input_tensor, split_size=2, dim=0)
print('Split tensors:\n', _splits)
_splits = torch.Tensor.split(_input_tensor, split_size=2, dim=1)
print('Split tensors:\n', _splits)
_splits = torch.Tensor.split(_input_tensor, split_size=2, dim=2)
print('Split tensors:\n', _splits)