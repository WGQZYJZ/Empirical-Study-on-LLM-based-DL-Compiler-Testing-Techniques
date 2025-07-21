'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.rand(5, 3)
mat = torch.rand(3, 5)
vec = torch.rand(5)
torch.Tensor.addmv(input_tensor, mat, vec)
print(input_tensor)