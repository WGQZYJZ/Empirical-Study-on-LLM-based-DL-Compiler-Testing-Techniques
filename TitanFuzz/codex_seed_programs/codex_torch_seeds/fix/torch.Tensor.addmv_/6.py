'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
mat = torch.rand(3, 4)
vec = torch.rand(4)
torch.Tensor.addmv_(mat, vec, beta=1, alpha=1)
print(mat)