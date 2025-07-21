'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:', input_tensor)
dim = 1
index = torch.tensor([0, 2])
tensor = torch.tensor([0.1, 0.2])
input_tensor.index_add_(dim, index, tensor)
print('input_tensor:', input_tensor)
dim = 1
index = torch.tensor([0, 2])
tensor = torch.tensor([0.1, 0.2])
input_tensor.index_add_(dim, index, tensor, alpha=0.5)
print('input_tensor:', input_tensor)
dim = 0
index = torch