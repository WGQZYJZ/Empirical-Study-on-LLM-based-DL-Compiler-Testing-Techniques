'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
import torch
a = torch.randint(0, 2, (3, 3), dtype=torch.bool)
b = torch.randint(0, 2, (3, 3), dtype=torch.bool)
print(a)
print(b)
print(torch.bitwise_or(a, b))