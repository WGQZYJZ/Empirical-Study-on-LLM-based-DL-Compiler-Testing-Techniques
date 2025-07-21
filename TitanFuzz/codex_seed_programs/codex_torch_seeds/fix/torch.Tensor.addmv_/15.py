'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, requires_grad=True)
mat = torch.randn(2, 3, requires_grad=True)
vec = torch.randn(3, requires_grad=True)
torch.Tensor.addmv_(input_tensor, mat, vec, beta=1, alpha=1)
print(input_tensor)