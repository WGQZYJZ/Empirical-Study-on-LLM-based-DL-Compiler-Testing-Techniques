'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
input = torch.randn(1, 3)
other = torch.randn(3)
print(torch.sub(input, other))
print(torch.sub(input, other, out=input))
print(input)