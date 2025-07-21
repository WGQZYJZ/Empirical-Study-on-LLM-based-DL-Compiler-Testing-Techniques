'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.geometric_\ntorch.Tensor.geometric_(_input_tensor, p, *, generator=None)\n'
import torch
input = torch.rand(1, 1, dtype=torch.float64)
p = torch.rand(1, 1, dtype=torch.float64)
torch.Tensor.geometric_(input, p)
print(input)