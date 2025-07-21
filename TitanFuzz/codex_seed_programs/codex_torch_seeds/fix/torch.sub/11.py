'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
import torch
input = torch.randn(3, 2)
other = torch.randn(3, 2)
output = torch.sub(input, other)
print(output)