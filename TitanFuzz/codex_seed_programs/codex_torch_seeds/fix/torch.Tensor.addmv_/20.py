'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
mat = torch.randn(4, 3)
vec = torch.randn(3)
out = torch.zeros(4)
torch.Tensor.addmv_(out, mat, vec)
print(out)
mat = torch.randn(4, 3)
vec = torch.randn(3)
out = torch.zeros(4)
torch.Tensor.addmv_(out, mat, vec, beta=2, alpha=0.5)
print(out)