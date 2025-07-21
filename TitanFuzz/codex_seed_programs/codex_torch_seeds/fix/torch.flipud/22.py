'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
input = torch.randn(5, 5)
print(input)
print(torch.flipud(input))