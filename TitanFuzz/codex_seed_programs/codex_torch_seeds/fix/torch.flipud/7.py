'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
input = torch.randn(3, 4)
print(input)
output = torch.flipud(input)
print(output)