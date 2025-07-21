'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input = torch.randn(1, 3)
print(input)
output = torch.unbind(input, dim=0)
print(output)
output = torch.unbind(input, dim=1)
print(output)