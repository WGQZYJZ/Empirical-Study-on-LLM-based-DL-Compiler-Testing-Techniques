'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(x.nonzero())
torch.nonzero(x, as_tuple=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p=2, dim=None, keepdim=False, out=None, dtype=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(x.norm(p=2, dim=1))
torch.norm(x, p=2, dim=1)