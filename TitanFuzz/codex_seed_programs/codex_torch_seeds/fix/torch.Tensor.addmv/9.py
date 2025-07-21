'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(4, 3)
mat = torch.randn(3, 5)
vec = torch.randn(5)
result = torch.Tensor.addmv(input_tensor, mat, vec, beta=1, alpha=1)
print(result)