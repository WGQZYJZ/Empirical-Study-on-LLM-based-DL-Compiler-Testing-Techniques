'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.add\ntorch.add(input, other, *, alpha=1, out=None)\n'
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
output = torch.add(input, other)
print(output)