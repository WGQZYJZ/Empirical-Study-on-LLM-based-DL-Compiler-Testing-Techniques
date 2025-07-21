'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.dist(input, other, p=2)