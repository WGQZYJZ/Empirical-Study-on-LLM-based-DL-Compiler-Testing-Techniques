'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.rand(3, 4)
vec1 = torch.rand(4)
vec2 = torch.rand(3)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)
print(input_tensor)