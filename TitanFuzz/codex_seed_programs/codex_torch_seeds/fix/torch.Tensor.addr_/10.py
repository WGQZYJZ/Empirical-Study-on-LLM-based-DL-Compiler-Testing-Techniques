'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
vec1 = torch.tensor([7, 8, 9])
vec2 = torch.tensor([10, 11, 12])
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)
print(input_tensor)