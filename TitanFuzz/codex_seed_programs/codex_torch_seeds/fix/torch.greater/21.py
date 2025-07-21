'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
import torch
input = torch.rand(4, 4)
other = torch.rand(4, 4)
out = torch.greater(input, other)
print(out)