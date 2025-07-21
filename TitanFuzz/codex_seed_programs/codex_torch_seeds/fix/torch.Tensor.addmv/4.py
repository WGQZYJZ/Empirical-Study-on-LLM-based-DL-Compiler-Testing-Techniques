'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
_input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 3)
vec = torch.randn(3)
result = torch.Tensor.addmv(_input_tensor, mat, vec)
print(result)