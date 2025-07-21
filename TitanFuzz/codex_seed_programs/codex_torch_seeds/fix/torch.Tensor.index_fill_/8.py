'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor =\n', input_tensor)
torch.Tensor.index_fill_(input_tensor, 0, torch.tensor([0, 2]), 1)
print('input_tensor =\n', input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select_\ntorch.Tensor.index_select_(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor =\n', input_tensor)
torch