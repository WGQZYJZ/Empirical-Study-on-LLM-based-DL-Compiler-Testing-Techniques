'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_floating_point\ntorch.is_floating_point(input)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float)
print(input)
output = torch.is_floating_point(input)
print(output)