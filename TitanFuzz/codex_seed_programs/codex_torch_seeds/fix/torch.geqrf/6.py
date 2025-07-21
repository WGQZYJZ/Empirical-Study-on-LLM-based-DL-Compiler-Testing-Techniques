'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
output = torch.geqrf(input)
print(output)