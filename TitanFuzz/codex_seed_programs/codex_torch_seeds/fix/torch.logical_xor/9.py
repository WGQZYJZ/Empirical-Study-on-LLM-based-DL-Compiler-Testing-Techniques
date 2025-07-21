'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 0, 0, 1], [1, 1, 0, 0]], dtype=torch.bool)
other = torch.tensor([[0, 1, 1, 0], [1, 0, 1, 1]], dtype=torch.bool)
out = torch.logical_xor(input, other)
print(out)