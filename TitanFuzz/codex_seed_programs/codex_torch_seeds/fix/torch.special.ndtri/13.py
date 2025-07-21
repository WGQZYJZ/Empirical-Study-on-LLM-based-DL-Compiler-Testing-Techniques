'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
torch.special.ndtri(input)
print(torch.special.ndtri(input))