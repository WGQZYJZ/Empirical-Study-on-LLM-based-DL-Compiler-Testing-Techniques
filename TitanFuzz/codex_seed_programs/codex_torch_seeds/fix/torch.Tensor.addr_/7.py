'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.rand(4, 4)
vec1 = torch.rand(4)
vec2 = torch.rand(4)
torch.Tensor.addr_(input_tensor, vec1, vec2)
print('input_tensor: ', input_tensor)
print('vec1: ', vec1)
print('vec2: ', vec2)