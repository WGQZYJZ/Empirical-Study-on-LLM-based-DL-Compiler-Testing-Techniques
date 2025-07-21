'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
a = torch.tensor([27, 3], dtype=torch.int32)
b = torch.tensor([9, 3], dtype=torch.int32)
print(torch.lcm(a, b))