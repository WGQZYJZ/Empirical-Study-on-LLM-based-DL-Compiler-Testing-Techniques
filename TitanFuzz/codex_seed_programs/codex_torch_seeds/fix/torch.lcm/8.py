'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
a = torch.tensor(3)
b = torch.tensor(4)
print(torch.lcm(a, b))