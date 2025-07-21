'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
a = torch.tensor([2, 4, 6, 8])
b = torch.tensor([1, 3, 5, 7])
print(torch.lcm(a, b))