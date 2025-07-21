'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
vec1 = torch.rand(4, 4)
vec2 = torch.rand(4, 4)
torch.Tensor.addr_(vec1, vec2, beta=1, alpha=1)
print('vec1 = ', vec1)
print('vec2 = ', vec2)