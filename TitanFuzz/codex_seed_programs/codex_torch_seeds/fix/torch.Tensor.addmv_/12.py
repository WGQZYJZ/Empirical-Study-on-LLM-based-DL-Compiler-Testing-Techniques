'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.ones(2, 3)
mat = torch.rand(3, 2)
vec = torch.rand(2)
input_tensor.addmv_(mat, vec)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.ones(2, 3)
mat = torch.rand(3, 2)
vec = torch.rand(2)
input_tensor.add