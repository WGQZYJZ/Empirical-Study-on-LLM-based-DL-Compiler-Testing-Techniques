'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
mat = torch.randn(4, 3)
vec = torch.randn(3)
torch.Tensor.addmv_(mat, mat, vec)
print(mat)