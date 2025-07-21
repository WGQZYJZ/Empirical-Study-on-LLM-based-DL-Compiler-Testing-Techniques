'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 3, requires_grad=True)
vec1 = torch.randn(3, requires_grad=True)
vec2 = torch.randn(3, requires_grad=True)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=2, alpha=2)