'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add\ntorch.Tensor.index_add(_input_tensor, dim, index, tensor2)\n'
import torch
import torch
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.randn(3, 4)
torch.Tensor.index_add(a, 0, torch.tensor([0, 2]), b)
torch.Tensor.index_add(a, 1, torch.tensor([0, 2]), c)
print(a)
print(b)
print(c)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy\ntorch.Tensor.index_copy(_input_tensor, dim, index, tensor2)\n'
import torch
import torch
a = torch.randn(3, 4)