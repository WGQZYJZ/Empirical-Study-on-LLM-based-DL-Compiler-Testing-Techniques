'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
output = torch.greater(input, other)
print(output)