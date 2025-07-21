'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
torch.dist(input, other, p=2)