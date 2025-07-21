'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
a = torch.arange(1, 10, dtype=torch.float)
print(a)
b = torch.square(a)
print(b)