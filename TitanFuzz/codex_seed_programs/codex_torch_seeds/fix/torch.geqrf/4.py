'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
output = torch.geqrf(input)
print(output)