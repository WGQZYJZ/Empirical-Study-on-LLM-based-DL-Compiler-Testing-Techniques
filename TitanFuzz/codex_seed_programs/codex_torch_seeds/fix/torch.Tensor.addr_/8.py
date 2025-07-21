'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 3)
vec1 = torch.rand(3)
vec2 = torch.rand(3)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)
print(input_tensor)